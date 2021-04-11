from django.shortcuts import render
from school_time_table.time_table.models import Class
import random

# def index(request):
#     name_organization = Organizations.objects.all()

USER = 'user'
PARENTS = 'parents'
TEACHER = 'teacher'
ADMIN = 'admin'
ROLE = [ USER, PARENTS, TEACHER, ADMIN]


# def lessons_class(request):
#     class_name = Class.objects.all()
#     lessons = LessonsClass.objects.filter(lessons__name__in=class_name)
#     lessons_count = lessons.count()
#     print(lessons_count)