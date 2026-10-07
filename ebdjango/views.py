"""Views for the assignment demo."""

from django.http import HttpResponse


def home(request):
    return HttpResponse(
        """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Django on Elastic Beanstalk</title>
    <style>
      body { font: 16px/1.5 system-ui, sans-serif; margin: 0; background: #f3f6fa; color: #17212b; }
      main { max-width: 720px; margin: 12vh auto; padding: 2rem; background: white; border-radius: 16px; box-shadow: 0 12px 36px #18304b18; }
      h1 { margin-top: 0; color: #142f4c; }
      code { background: #eef3f8; padding: .2rem .4rem; border-radius: 4px; }
    </style>
  </head>
  <body>
    <main>
      <h1>Your Django app is running</h1>
      <p>This starter app is configured for AWS Elastic Beanstalk.</p>
      <p>Framework: <code>Django</code> · Platform: <code>Python</code></p>
    </main>
  </body>
</html>""",
        content_type="text/html; charset=utf-8",
    )
