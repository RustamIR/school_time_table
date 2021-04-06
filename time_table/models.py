from django.core.validators import MinValueValidator
from django.db import models

from users.models import User

class Organization(models.Model):
    name = models.CharField(
        'Название организыции',
        max_length=100,
        db_index=True,
        unique=True
    )


class ClassRoom(models.Model):
    name = models.CharField(
        'Название кабинета',
        max_length=50,
        db_index=True,
        unique=True
    )
    count_seats = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    specifications = models.CharField(
        'Спецификация кабинета',
        max_length=50,
        db_index=True,
    )
    projector = models.BooleanField(
        'Наличие проектора',
        max_length=50,
        db_index=True,
    )


class Lessons(models.Model):
    name = models.CharField(
        'Название урока',
        max_length=50,
        db_index=True,
        unique=True
    )


class Class(models.Model):
    name = models.CharField(
        'Имя класса/группы',
        max_length=50,
        db_index=True,
        unique=True
    )
    students =  models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='class_people',
        verbose_name='Ученики'
    )
    count_students = models.PositiveIntegerField(
        'Количество учеников',
        validators=[MinValueValidator(1)]
    )


class TimeTable(models.Model):
    name = models.CharField(
        Class,
        'Имя класса/группы',
        max_length=50,
        db_index=True,
        unique=True
    )
    # day_week =
    number_lessons = models.CharField(
        on_delete=models.CASCADE,
        related_name='numbers',
        verbose_name='Номер урока'
    )
    class_room = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE,
        related_name='rooms',
        verbose_name='Кабинет'
    )
    lessons = models.ForeignKey(
        Lessons,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name='Название урока'
    )
    teachers = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='teachers',
        verbose_name='Учитель'
    )