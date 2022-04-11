from django.contrib import admin
from .models import Technology


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'image')
    list_per_page = 20

admin.site.register(Technology, TechnologyAdmin)