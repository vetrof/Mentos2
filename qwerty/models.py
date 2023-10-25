from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=255)
    info = models.TextField()

    def __str__(self):
        return f'{self.title}'


class Grade(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    level = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course} G{self.level}'


class Topic(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=255)
    num_topic = models.FloatField()
    info = models.TextField()
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.grade} N{self.num_topic} {self.title}'


class Lesson(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    num_lesson = models.FloatField()
    title = models.CharField(max_length=255)
    info = models.TextField()
    info_hide = models.TextField()
    description = models.TextField(null=True)


class LessonStatus(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)

# Внешний ключ LessonStatus.lesson > Lesson.id
# ref: LessonStatus.lesson > Lesson.id

# Внешний ключ "Course"."id" < "Grade"."course"
# Ref: "Course"."id" < "Grade"."course"

# Внешний ключ "Grade"."id" < "Topic"."grade"
# Ref: "Grade"."id" < "Topic"."grade"

# Внешний ключ "Topic"."id" < "Lesson"."topic"
# Ref: "Topic"."id" < "Lesson"."topic"
