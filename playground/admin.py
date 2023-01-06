from django.contrib import admin
from . import models

@admin.register(models.School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['school_name', 'school_location', 'school_email', 'school_website']
    list_per_page = 3
    search_fields = ['school_name__istartswith', 'school_location__istartswith']

    @admin.display(ordering='website')
    def school_website(self, website):
        website = 'school@gmail.com'
        return website


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'age', 'date_birth', 'gender_choices', 'school_id']
    list_editable = ['gender_choices']
    list_per_page = 3
    search_fields = ['first_name__istartswith', 'last_name__istartswith', 'gender_choices__istartswith']
    list_filter = ['first_name', 'last_name', 'gender_choices']


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'course_code', 'course_description', 'course_status', 'school_id', 'student_id']
    list_editable = ['course_status']
    list_per_page = 2
    search_fields = ['course_name__istartswith', 'course__code__istartswith']


@admin.register(models.Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['score', 'grade', 'course', 'student']
    list_per_page = 2
    search_fields = ['score__istartswith', 'grade__istartswith']
