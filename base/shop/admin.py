from django.contrib import admin
from . import models
from shop.models import Category, Course

admin.site.site_header = "Courses Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "WELCOME TO THE Courses ADMIN AREA!!"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')


class CourseInline(admin.TabularInline):
    model = Course
    exclude = ['created_at']
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]
    inlines = [CourseInline]


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Course, CourseAdmin)
