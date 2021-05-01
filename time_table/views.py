from django.db.models import Count
# from django.shortcuts import render, get_object_or_404
# from school_time_table.time_table.models import Class, Lessons, Organization, TimeTable, ClassRoom
# import random
# from users.models import Users
#
#
# def index(request):
#     organization = Organization.objects.all()
#     return render(request, 'index.html', organization)
#
#
# def class_name(request, class_name):
#     title = get_object_or_404(Class.objects.select_related('title'))
#     return render(request, 'class_name.html',title)
#
#
# def class_teacher(request, self, username): # группировать данные предмет-учитель
#     teacher = Users.objects.filter(role__is=self.TECHER)
#     lessons = Lessons.objects.filter('teacher')
#     lessons_teacher = Lessons.objects.filter(teacher__is=lessons.teacher)
#     return lessons_teacher
#
# def class_teacher_room(request, lessons_teacher):
#     class_room = ClassRoom.o
#
# 
# def lessons_class(request, lessons_id):
#     lessons = Lessons.objects.all() # получаем все уроки
#     class_room = ClassRoom.objects.all() # получаем все доступные кабинеты
#     # lessons_room =  # Объединения данных (какой урок будет проводиться в каком кабинете)
#     # class_lessons = Class.objects.filter(lessons_class__name__in=lessons)
#     class_lessons = Class.objects.filter(less__name__in=lessons).ordered_by('?')[:7] # сортируем в рандомном порядке по 7 предметов
#     numder_lessons = get_object_or_404( # получаем количество уроков на день
#         TimeTable.objects.select_related('numers'),
#         id=lessons_id
#     )
#     context = {
#         'numbers': numder_lessons,
#         'class_lessons': class_lessons
#     }
#     return render(request, 'class_name.html', context)