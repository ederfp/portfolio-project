from django.contrib import admin
from .models import Project, Skill, Contact

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technology', 'created_at']
    search_fields = ['title', 'description', 'technology']
    list_filter = ['created_at', 'technology']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'description']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_filter = ['created_at']