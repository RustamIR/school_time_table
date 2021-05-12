
from django.core.validators import MinValueValidator
from django.db import models

from users.models import Users


class Specification(models.Model):
    title = models.TextField(
        max_length=255,
        verbose_name='Название спецификации'
        # related_name='specification'
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Спецификация'
        verbose_name_plural = 'Спецификации'
        ordering = ['title']


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название урока')
    # spec_of_lesson = models.ForeignKey(Specification, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Спецификация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['title']


class Room(models.Model):
    number = models.CharField(max_length=10, verbose_name='Номер урока')
    capacity = models.PositiveIntegerField(
        'Количество учеников',
        validators=[MinValueValidator(1)]
    )
    spec_of_room = models.ForeignKey(Specification, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Спецификация кабинета')
    description = models.TextField(max_length=100, blank=True, verbose_name='Описание')

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'
        ordering = ['number']


class Para(models.Model):
    less = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Уроки')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Кабинет')
    teacher = models.ManyToManyField('Teacher', verbose_name='Учитель')

    # def __str__(self):
    #     return self.less

    class Meta:
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'


# class Journal(models.Model):
#     student = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Студенты')
#     less = models.ForeignKey(Lesson, on_delete=models.PROTECT, verbose_name='Уроки')
#     # Журнал! Заявка на будущее :)
#
#     def __str__(self):
#         return self.student.username
#
#     class Meta:
#         verbose_name = 'Журнал'
#         verbose_name_plural = 'Журналы'



class TimeTable(models.Model):
    MN = 'Monday'
    TU = 'Tuesday'
    WN = 'Wednesday'
    TH = 'Thursday'
    FR = 'Friday'
    ST = 'Saturday'
    DAYS = [(MN, MN),(TU, TU), (WN, WN), (TH, TH), (FR, FR), (ST,ST)]

    day = models.CharField(
        max_length=40,
        choices=DAYS,
        default="",
        verbose_name='Дни недели',
        # related_name='days'
    )

    number_lessons = models.PositiveIntegerField(
        verbose_name='Количество уроков',
        validators=[MinValueValidator(1)]
    )
    smena = models.PositiveIntegerField(
        verbose_name='Смена',
        validators=[MinValueValidator(1)],
    )
    para = models.ForeignKey(Para, on_delete=models.CASCADE, verbose_name='урок-класс-учитель')   # следует преобразовать в список с несколькими парами в админке
    # para = models.ForeignKey(
    #     Couple,
    #     on_delete=models.CASCADE,
    #     verbose_name='Уроки'
    # )

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
        ordering = ['day', 'number_lessons']

    # def __str__(self):
    #     return self.para


class Class(models.Model):
    title = models.CharField(
        'Название класса',
        max_length=200,
        unique=True
    )
    # jurn = models.ForeignKey(
    #     Journal,
    #     on_delete=models.CASCADE,
    #     related_name="jurn",
    #     verbose_name='Журнал'
    # )
    timetable = models.ForeignKey(
        TimeTable,
        on_delete=models.CASCADE,
        related_name="timetable",
        verbose_name='Расписание класса'
    )
    less = models.ForeignKey(Lesson, on_delete=models.PROTECT, verbose_name='Уроки', blank=True, null=True, related_name='class_less')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        ordering = ['title']


class Teacher(models.Model):
    teacher = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name='Учителя'
    )
    spec_teacher = models.ForeignKey(
        Lesson,
        on_delete=models.PROTECT,
        verbose_name='Специализация учителя'
    )
    class_name = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        verbose_name='Классы'
    )
    number_lessons = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    day_lessons = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    lessons = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name='Уроки учителя',
        related_name='teacher_lessons'
    )

    def str(self):
        return self.teacher

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
        ordering = ['teacher']

class Organization(models.Model):
    addr = models.TextField(max_length=255)
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
        related_name='class_org',
        verbose_name='Название классов'
    )

    def str(self):
        return self.title

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['title']

