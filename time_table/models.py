
from django.core.validators import MinValueValidator
from django.db import models

from users.models import Users


class ClassRoom(models.Model):
    title = models.CharField(
        max_length=100,
        # related_name="class_room"
    )
    count_students = models.PositiveIntegerField(
        'Количество учеников',
        validators=[MinValueValidator(1)]
    )
    projector = models.BooleanField()
    text = models.TextField()


class Lessons(models.Model):
    lessons = models.CharField(max_length=100)
    room = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE,
        related_name='office'
    )
    teacher = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='teachers',
        verbose_name='Учитель'
    )
    spec = models.BooleanField()


class TimeTable(models.Model):
    class_name = models.CharField(max_length=100)
    lessons = models.ForeignKey(
        Lessons,
        on_delete=models.CASCADE,
        related_name='les'
    )
    number_lessons = models.PositiveIntegerField(
        'Количество уроков',
        validators=[MinValueValidator(1)]
    )
    smena = models.PositiveIntegerField(
        'Смена',
        validators=[MinValueValidator(1)]
    )


class Class(models.Model):
    # organization = models.ForeignKey(
    #     Organization,
    #     on_delete=models.CASCADE,
    #     related_name='org',
    #     verbose_name='Организация',
    # )
    title = models.CharField(
        'Название класса',
        max_length=200,
        unique=True
    )
    lessons_class = models.ForeignKey(
        Lessons,
        on_delete=models.CASCADE,
        related_name='less',
        null=True,
        default='',
    )

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        ordering = ['title']


class Organization(models.Model):
    title = models.CharField(
        'Название организыции',
        max_length=100,
        # db_index=True,
        # unique=True,
        blank=True,
        null=True,
        default='',
        # editable=False
    )
    class_name = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name='class_org'
    )
    class_room = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE,
        related_name='org',
        verbose_name='Организация',
    )

    def str(self):
        return self.title

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['title']

