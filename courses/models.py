from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey('profiles.Teacher',
                                on_delete=models.CASCADE,
                                related_name='courses')


    def __str__(self):
        return self.name