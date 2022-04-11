from django.contrib import admin
from .models import Project, Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

admin.site.register(Tag, TagAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'url', 'image')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'image')
    list_per_page = 20

admin.site.register(Project, ProjectAdmin)