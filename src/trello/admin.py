from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'name')


class TaskAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'due_date', 'description')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)

