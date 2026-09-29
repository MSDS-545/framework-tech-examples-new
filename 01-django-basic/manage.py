#!/usr/bin/env python
"""Django command-line entry point. Django normally generates this file."""
import os
import sys
import django

def main():
    # Tell Django which settings module belongs to this project.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    from django.core.management import execute_from_command_line
    # Forward commands such as runserver, migrate, and test to Django.
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
