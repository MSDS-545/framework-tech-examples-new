# demo/models.py

from django.db import models


class Student(models.Model):
    """
    Represents a student stored in the database.

    Django converts this Python model into a
    corresponding database table through migrations.
    """

    # Store the student's name.
    name = models.CharField(max_length=100)

    # Store the student's university email address.
    email = models.EmailField()