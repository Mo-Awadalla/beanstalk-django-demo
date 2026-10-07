#!/usr/bin/env python3
"""Django management entry point for the Elastic Beanstalk demo."""

import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ebdjango.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
