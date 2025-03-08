from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from courses.models import Course


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LessonContent(models.Model):
    """ Join model for lessons and content """
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')





class ItemBase(models.Model):
    """ Abstract Base class for all content models """
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Text(ItemBase):
    content = models.TextField()

    def render(self):
        return self.content

class Image(ItemBase):
    file = models.FileField(upload_to='images')

    def render(self):
        return f'<img src="{self.file.url}" />'