from django.contrib import admin
from .models import Organization, ClassRoom, Lessons, TimeTable, Class

#
# @admin.register(Organization)
# class OrganizationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title',)
    # list_filter = ('title', 'title_class')

#     ist_display = ('id', 'title')
#     # list_display_links = ('id', )
#     # save_as = True
#
#
# @admin.register(ClassRoom)
# class ClassRoomAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'count_students', 'projector')
# #     list_display_links = ('id', 'title')
#     list_filter = ('title', 'count_students')
#     search_fields = ('title',)
#     save_on_top = True
#     save_as = True
#     fieldsets = (
#         (None, {
#             "fields": (("title", "count_students", "projector"), 'text', )
#         }),
#     )
#
# @admin.register(Lessons)
# class LessonsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'lessons', 'room', 'teacher')
#     list_display_links = ('id', 'lessons')
#     search_fields = ('lessons',)
#     save_on_top = True
#     save_as = True
#     fieldsets = (
#         (None, {
#             "fields": ("lessons", "room", "teacher", )
#         }),
#     )
#
# @admin.register(TimeTable)
# class TimeTableAdmin(admin.ModelAdmin):
#     list_display = ('id', 'class_name', 'lessons')
#     list_display_links = ('id', 'class_name')
#     search_fields = ('lessons',)
#     save_on_top = True
#     save_as = True
#     fieldsets = (
#         (None, {
#             "fields": ("class_name", "lessons", "number_lessons", "smena")
#         }),
#     )
#
# @admin.register(Class)
# class ClassAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', )
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True
#     save_as = True
#     fieldsets = (
#         (None, {
#             "fields": ("organization", "title", "time_table", )
#         }),
#     )