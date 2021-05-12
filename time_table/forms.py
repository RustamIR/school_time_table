from django import forms

from .models import Class, TimeTable, Lesson, Room, Para, Teacher, Specification, Organization


class TimeTableForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = {
            'day',
            'number_lessons',
            'smena',
            'para'
        }


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = {
            'number',
            'capacity',
            'description',
            'spec_of_room',
        }


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = {
            'title',
            'less',
            'timetable'
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
