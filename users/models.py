from django.contrib.auth.models import AbstractUser
from django.db import models


USER = 'user'
PARENTS = 'parents'
TEACHER = 'teacher'
ADMIN = 'admin'
ROLE = [USER, PARENTS, TEACHER, ADMIN]


class Role(models.Model):
    role = models.CharField(
        "Роль",
        # choices=ROLE,
        # default=ROLE,
        max_length=50,
        db_index=True
    )
    text = models.TextField(
        max_length=50
    )
    levels = models.CharField(max_length=100)

    class Meta:
        verbose_name='роль'
        verbose_name_plural='роли'

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_admin

    @property
    def is_teacher(self):
        return self.role == self.TEACHER or self.is_teacher

    @property
    def is_parents(self):
        return self.role == self.PARENTS or self.is_parents

    def __str__(self):
        return self.role


class Users(AbstractUser):
    role = models.CharField(
        max_length=40,
        #choices=ROLE,
        #default=ROLE,
        verbose_name='Роль'
    )
    bio = models.TextField(max_length=250, blank=True)
    email = models.EmailField(unique=True, verbose_name='Почта')
    username = models.CharField(max_length=250,
                                blank=True,
                                null=True,
                                unique=True,
                                db_index=True,
                                verbose_name='Имя')
    # confirm_code = models.CharField(max_length=5)

    class Meta:
        ordering = ["username"]

