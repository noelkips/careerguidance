from re import search
from django.contrib import admin
from .models import Course, University, Category, Entry


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('Univ_no', 'name', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_no', 'name',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_no', 'name', 'category')


class EntryAdmin(admin.ModelAdmin):
    list_display = ('entry_no', 'course', 'cut_off', 'university')
    # search_fields = ('course','university')


admin.site.register(Course, CourseAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(University, UniversityAdmin)

admin.site.register(Entry, EntryAdmin)

