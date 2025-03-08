from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Student(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)

    # Override groups to avoid conflict
    groups = models.ManyToManyField(Group,
                                    related_name="student_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission,
                                              related_name="student_permissions",
                                              blank=True)

    def __str__(self):
        return self.username


class Teacher(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)

    groups = models.ManyToManyField(Group,
                                    related_name="teacher_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission,
                                              related_name="teacher_permissions",
                                              blank=True)

    def __str__(self):
        return self.username
