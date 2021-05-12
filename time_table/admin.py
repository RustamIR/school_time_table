from django.contrib import admin
from .models import Organization, Room, Lesson, TimeTable, Class, Specification, Para, Teacher


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'addr', 'class_name')
    list_filter = ('title',)

#     ist_display = ('id', 'title')
#     # list_display_links = ('id', )
#     # save_as = True


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'capacity', 'spec_of_room', 'description')
    list_display_links = ('id', 'number')
#     list_filter = ('title', 'count_students')
#     search_fields = ('title',)
#     save_on_top = True
#     save_as = True
#     fieldsets = (
#         (None, {
#             "fields": (("title", "count_students", "projector"), 'text', )
#         }),
#     )

# class CoupleInline(admin.TabularInline):
#     model = Teacher
#     verbose_name = 'Учитель'

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'spec_teacher', 'class_name')
    list_display_links = ('id', 'teacher')


@admin.register(Para)
class CoupleAdmin(admin.ModelAdmin):
    # inlines = CoupleInline
    list_display = ('id', 'less', 'room') # следует преобразовать в список с несколькими парами
    list_display_links = ('id', 'room')

    # model = Couple
    # min_num = 1
    # extra = 0
# model = RecipeIngredient
#     min_num = 1
#     extra = 0
#     verbose_name = 'ингредиент'

# @admin.register(Journal)
# class JournalAdmin(admin.ModelAdmin):
#     list_display = ('id', 'student', 'less')
#     list_display_links = ('id', 'student',)
#     search_fields = ('students',)


@admin.register(Lesson)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
#     save_on_top = True
#     save_as = True
#     fieldsets = (
#         (None, {
#             "fields": ("lessons", "room", "teacher", )
#         }),
#     )


@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    # inlines = [CoupleAdmin]
    list_display = ('id', 'day', 'number_lessons', 'smena', 'para')
    list_display_links = ('id', 'day')
    # search_fields = ('id', 'number_lessons')
#     save_on_top = True
#     save_as = True
#     fieldsets = (
#         (None, {
#             "fields": ("class_name", "lessons", "number_lessons", "smena")
#         }),
#     )


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'timetable')
    # list_display_links = ('id')
    search_fields = ('id', 'title',)
#     save_on_top = True
#     save_as = True
#     fieldsets = (
#         (None, {
#             "fields": ("organization", "title", "time_table", )
#         }),
#     )