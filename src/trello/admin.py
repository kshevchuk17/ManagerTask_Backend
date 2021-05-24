from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'email', 'first_name', 'last_name')


class ProjectAdmin(admin.ModelAdmin):
	list_display = ('id', 'owner', 'name')
	list_filter = ('owner', )
	search_fields = ('id', 'name')


class ColumnAdmin(admin.ModelAdmin):
	list_display = ('project', 'name')


class TaskAdmin(admin.ModelAdmin):
	list_display = ('id', 'owner', 'title', 'assignee', 'due_date', 'created_at', 'is_complete', 'description')
	list_filter = ('owner', 'assignee', 'due_date', 'created_at', 'is_complete')
	search_fields = ('title', 'description')


class SubtaskAdmin(admin.ModelAdmin):
	list_display = ('task', 'title', 'created_at', 'due_date', 'is_complete', 'description')
	search_fields = ('title', 'description')
	list_filter = ('due_date', 'created_at', 'is_complete')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Subtask, SubtaskAdmin)


