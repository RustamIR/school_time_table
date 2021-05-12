from urllib import request
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from school_time_table.time_table.forms import TimeTableForm, RoomForm, ClassForm, TeacherForm
from school_time_table.time_table.models import Class, Lesson, Organization, TimeTable, Room
import random
from users.models import Users
from django.views.generic import CreateView


def index(request):
    organization = Organization.objects.all()
    return render(request, 'index.html', organization)


def class_lessons(request):
    class_name = Class.objects.filter('class_less').ordered_by('?') # рандомим список уроков класса
    lessons = []
    for class_less in class_name:
        # как пройтись по списку и разбить  уроков на 6 других списков?


@method_decorator(login_required, name='dispatch')
class RoomNew(CreateView):
    form = RoomForm()
    success_url = reverse_lazy("index")
    template_name = "newRoom.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.admin = self.request.user
        self.object.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
def new_class(request):
    form = RoomForm()
    success_url = reverse_lazy("index")
    template_name = "newLessons.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.admin = self.request.user
        self.object.save()
        return super().form_valid(form)

def new_teacher(request):
    class_name = get_object_or_404(Class, pk=id)
    lessons = get_object_or_404(Lesson, pk=id)
    room = get_object_or_404(Room, pk=id)



# def new_teacher(request):
#     form = TeacherForm(request.POST or None, files=request.FILES or None)
#     if form.is_valid():
#         try:
#             teacher = form.save(commit=False)
#             teacher.save()
#         except forms.ValidationError as e:
#             return render(
#                 request,
#                 'formTeacher.html',
#                 {'form': form,
#                  'errortext': str(e)}
#             )
#         return redirect()
#
#     return render(
#         request,
#         'formTeacher.html',
#         {'form': form}
#     )

# def save_shedule(request): # функция для объединения списков уроков по дням
#     #if
#     class_shedule = Class.objects.order_by('?')
#
#
# def TimeTableNew(CreateView):
#     form = TimeTableForm
#
#     if form.is_valid():
#         try:
#             time_table = save_shedule(request, form)
#         except form.ValidationError as e:
#             return render(
#                 request,
#                 'formRecipe.html',
#                 {'form': form,
#                  'errortext': str(e)}
#             )




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

