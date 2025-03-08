from django.contrib import admin
from .models import Lesson, LessonContent

# Register your models here.
admin.site.register(Lesson)
admin.site.register(LessonContent)