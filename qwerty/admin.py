from django.contrib import admin
from .models import Course, Grade, Topic, Lesson, LessonStatus

# Регистрация моделей в административном интерфейсе

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'level', 'course')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'num_topic', 'grade')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'num_lesson', 'title')

@admin.register(LessonStatus)
class LessonStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'lesson', 'status')

# Добавьте этот код в ваш файл admins.py

