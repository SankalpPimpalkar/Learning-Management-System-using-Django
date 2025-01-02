from django.contrib import admin
from .models import Course, EnrolledCourse, Lesson, LessonFile

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'category', 'is_approved', 'price', 'isFree')
    search_fields = ('name', 'description', 'owner__name')
    list_filter = ('category', 'is_approved', 'isFree')
    
    fields = ('name', 'description', 'owner', 'category', 'price', 'is_approved', 'thumbnail', 'isFree')
    ordering = ('-is_approved', 'name')

class EnrolledCourseAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date')
    search_fields = ('student__name', 'course__name')
    list_filter = ('course',)
    ordering = ('-enrollment_date',)

class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'order')
    search_fields = ('name', 'course__name')
    list_filter = ('course',)
    ordering = ('course', 'order')
    list_editable = ('order',)

class LessonFileAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'file', 'custom_name')
    search_fields = ('lesson__name', 'file', 'custom_name')
    list_filter = ('lesson',)
    ordering = ('lesson',)

admin.site.register(Course, CourseAdmin)
admin.site.register(EnrolledCourse, EnrolledCourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonFile, LessonFileAdmin)
