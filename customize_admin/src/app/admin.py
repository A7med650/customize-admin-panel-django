from django.contrib import admin
from .models import student, std
from django.utils.html import format_html

# Register your models here.

admin.site.site_header = 'Books'
admin.site.site_title = 'Books'


class stdinline(admin.StackedInline):
    model = std
    extra = 1
    max_num = 10


@admin.register(student)
class student_admin(admin.ModelAdmin):
    list_display = ['name', 'address', 'image_tag', 'active']
    list_display_links = ['name']
    list_filter = ['date']
    search_fields = ['name', 'address']
    # fields = ['name', 'phone']
    inlines = [stdinline]


@admin.register(std)
class std_admin(admin.ModelAdmin):
    pass
