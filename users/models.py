from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    USER = 'user'
    PARENTS = 'parents'
    TEACHER = 'teacher'
    ADMIN = 'admin'
    ROLE = [
        (USER, USER),
        (PARENTS, PARENTS),
        (TEACHER, TEACHER),
        (ADMIN, ADMIN),
    ]

    role = models.CharField(max_length=40, choices=ROLE,
                            default=ROLE,
                            verbose_name='Роль', )
    bio = models.TextField(max_length=250, blank=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=250,
                                blank=True,
                                null=True,
                                unique=True,
                                db_index=True)
    # confirm_code = models.CharField(max_length=5)

    class Meta:
        ordering = ["username"]

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_admin

    @property
    def is_teacher(self):
        return self.role == self.TEACHER or self.is_teacher

    @property
    def is_parents(self):
        return self.role == self.PARENTS or self.is_parents
