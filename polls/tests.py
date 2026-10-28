import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


class PollsTests(TestCase):
    def setUp(self):
        Question.objects.all().delete()
        self.question = Question.objects.create(
            question_text="Which CI tool?", pub_date=timezone.now()
        )
        self.choice = self.question.choice_set.create(choice_text="Travis CI")

    def test_root_redirects_to_polls(self):
        self.assertRedirects(self.client.get("/"), reverse("polls:index"))

    def test_index_shows_published_question(self):
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, self.question.question_text)

    def test_future_question_is_hidden(self):
        future = Question.objects.create(
            question_text="Future question",
            pub_date=timezone.now() + datetime.timedelta(days=1),
        )
        self.assertNotContains(
            self.client.get(reverse("polls:index")), future.question_text
        )
        for route in ("polls:detail", "polls:results"):
            self.assertEqual(
                self.client.get(reverse(route, args=[future.pk])).status_code, 404
            )
        self.assertFalse(future.was_published_recently())

    def test_vote_updates_count_and_redirects(self):
        response = self.client.post(
            reverse("polls:vote", args=[self.question.pk]), {"choice": self.choice.pk}
        )
        self.assertRedirects(
            response, reverse("polls:results", args=[self.question.pk])
        )
        self.choice.refresh_from_db()
        self.assertEqual(self.choice.votes, 1)

    def test_vote_requires_post(self):
        response = self.client.get(reverse("polls:vote", args=[self.question.pk]))
        self.assertEqual(response.status_code, 405)

    def test_missing_or_invalid_choice_does_not_vote(self):
        for data in ({}, {"choice": 999999}):
            response = self.client.post(
                reverse("polls:vote", args=[self.question.pk]), data
            )
            self.assertContains(
                response, "Choose an option before submitting your vote."
            )
        self.choice.refresh_from_db()
        self.assertEqual(self.choice.votes, 0)

    def test_question_recent_date_and_labels(self):
        self.assertTrue(self.question.was_published_recently())
        self.question.pub_date = timezone.now() - datetime.timedelta(days=2)
        self.assertFalse(self.question.was_published_recently())
        self.assertEqual(str(self.question), "Which CI tool?")
        self.assertEqual(str(self.choice), "Travis CI")
