from django.core.validators import MinValueValidator
from django.db import models

from users.models import Users


class Organization(models.Model):
    title = models.CharField(
        'Название организыции',
        max_length=100,
        db_index=True,
        unique=True,
    )
    # time_table = models.ForeignKey(
    #     TimeTable,
    #
    # )


class Classroom(models.Model):
    title = models.CharField(max_length=100)
    count_students = models.PositiveIntegerField(
        'Количество учеников',
        validators=[MinValueValidator(1)]
    )
    projector = models.BooleanField()
    text = models.TextField()


class Lessons(models.Model):
    lessons = models.CharField(max_length=100)
    room = models.PositiveIntegerField(
        'Название кабинета',
        validators=[MinValueValidator(1)]
    )
    teacher = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='teachers',
        verbose_name='Учитель'
    )


class TimeTable(models.Model):
    class_name = models.CharField(max_length=100)
    lessons = models.ForeignKey(
        Lessons,
        on_delete=models.CASCADE,
        related_name='les'
    )
    number_lessons = models.PositiveIntegerField(
        max_length=10,
        # related_name='numbers',
        # verbose_name='Номер урока'
        validators=[MinValueValidator(1)]
    )
    smena = models.PositiveIntegerField(
        'Смена',
        validators=[MinValueValidator(1)]
    )


class Class(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='org',
        verbose_name='Организация',
    )
    title = models.CharField(
        'Название класса',
        max_length=200,
        db_index=True,
        unique=True
    )
    time_table = models.ForeignKey(
        TimeTable,
        on_delete=models.CASCADE,
        related_name='time_table_class',
        verbose_name = 'Расписание класса'
    )


# class Organization(models.Model):
#     title = models.CharField(
#         'Название организыции',
#         max_length=100,
#         db_index=True,
#         unique=True,
#     )
#
#
# class ClassRoom(models.Model):
#     name = models.CharField(
#         'Название кабинета',
#         max_length=50,
#         db_index=True,
#         unique=True,
#     )
#     count_seats = models.PositiveIntegerField(
#         validators=[MinValueValidator(1)],
#         verbose_name='Количество мест в классе'
#     )
#     specifications = models.CharField(
#         'Спецификация кабинета',
#         max_length=50,
#         default='',
#         db_index=True,
#     )
#     projector = models.BooleanField(
#         'Наличие проектора',
#         max_length=50,
#         default=False,
#         db_index=True,
#     )
#
#
# class Lessons(models.Model):
#     name = models.CharField(
#         'Название урока',
#         max_length=50,
#         db_index=True,
#         unique=True,
#     )
#
#
# class Class(models.Model):
#     name = models.CharField(
#         'Имя класса/группы',
#         max_length=50,
#         db_index=True,
#         unique=True,
#     )
#     students =  models.ForeignKey(
#         Users,
#         on_delete=models.CASCADE,
#         related_name='class_people',
#         verbose_name='Ученики'
#     )
#     count_students = models.PositiveIntegerField(
#         'Количество учеников',
#         validators=[MinValueValidator(1)]
#     )
#
# class LessonsClass(models.Model):
#     lessons = models.ForeignKey(
#         Lessons,
#         on_delete=models.CASCADE,
#         related_name='les'
#     )
#     class_name = models.ForeignKey(
#         Class,
#         on_delete=models.CASCADE,
#         related_name='class_name'
#     )
#     quantity = models.PositiveIntegerField(
#         validators=[MinValueValidator(1)]
#     )
#
#
#
# class TimeTable(models.Model):
#     name = models.CharField(
#         Class,
#         'Имя класса/группы',
#         max_length=50,
#         db_index=True,
#         unique=True,
#     )
#     # day_week =
#     number_lessons = models.CharField(
#         # related_name='numbers',
#         max_length=10,
#         verbose_name='Номер урока'
#     )
#     class_room = models.ForeignKey(
#         ClassRoom,
#         on_delete=models.CASCADE,
#         related_name='rooms',
#         verbose_name='Кабинет'
#     )
#     # lessons = models.ForeignKey(
#     #     Lessons,
#     #     on_delete=models.CASCADE,
#     #     related_name='lessons',
#     #     verbose_name='Название урока'
#     # )
#     lessons = models.ManyToManyField(
#         LessonsClass,
#         # through='LessonsClass',
#         related_name='lessons_title',
#         verbose_name='Название урока'
#     )
#     teachers = models.ForeignKey(
#         Users,
#         on_delete=models.CASCADE,
#         related_name='teachers',
#         verbose_name='Учитель'
#     )
#
