from django.contrib import admin
from .models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'cv')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'image')
    list_per_page = 20

admin.site.register(About, AboutAdmin)