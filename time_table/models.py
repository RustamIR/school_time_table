
from django.core.validators import MinValueValidator
from django.db import models

from users.models import Users



class Specification(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Спецификация'
        verbose_name_plural = 'Спецификации'
        ordering = ['title']


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    specoflesson = models.ForeignKey(Specification, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['title']


class Room(models.Model):
    number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField(
        'Количество учеников',
        validators=[MinValueValidator(1)]
    )
    specofroom = models.ForeignKey(Specification, on_delete=models.CASCADE)
    description = models.TextField(max_length=100)

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'
        ordering = ['number']


class Couple(models.Model):
    less = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'


class Journal(models.Model):
    student = models.ForeignKey(Users, on_delete=models.PROTECT)
    less = models.ForeignKey(Lesson, on_delete=models.PROTECT)
    # Журнал! Заявка на будущее :)

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'



class TimeTable(models.Model):
    PN = 'Monday'
    VT = 'Tuesday'
    SR = 'Wednesday'
    CH = 'Thursday'
    PT = 'Friday'
    SB = 'Saturday'
    DAYS = [PN, VT, SR, CH, PT, SB]

    day = models.CharField(
        max_length=40,
        choices=DAYS,
        default="",
        verbose_name='Дни недели',
        related_name='days'
    )

    number_lessons = models.PositiveIntegerField(
        'Количество уроков',
        validators=[MinValueValidator(1)]
    )
    smena = models.PositiveIntegerField(
        'Смена',
        validators=[MinValueValidator(1)]
    )
    para = models.ForeignKey(Couple, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
        ordering = ['day']




class Class(models.Model):
    title = models.CharField(
        'Название класса',
        max_length=200,
        unique=True
    )
    jurn = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name="jurn")
    timetable = models.ForeignKey(TimeTable, on_delete=models.CASCADE, related_name="timetable")

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        ordering = ['title']


class Organization(models.Model):
    addr = models.CharField(max_length=255)
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

    def str(self):
        return self.title

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['title']

