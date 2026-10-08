from django.db import migrations
from django.utils import timezone


def add_sample_poll(apps, schema_editor):
    Question = apps.get_model("polls", "Question")
    Choice = apps.get_model("polls", "Choice")

    question = Question.objects.create(
        question_text="What's up?",
        pub_date=timezone.now(),
    )
    Choice.objects.bulk_create(
        [
            Choice(question=question, choice_text="Not much"),
            Choice(question=question, choice_text="The sky"),
            Choice(question=question, choice_text="Just hacking again"),
        ]
    )


def remove_sample_poll(apps, schema_editor):
    Question = apps.get_model("polls", "Question")
    Question.objects.filter(question_text="What's up?").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_sample_poll, remove_sample_poll),
    ]
