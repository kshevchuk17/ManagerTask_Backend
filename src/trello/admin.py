from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
	list_display = ('id', 'owner', 'name')
	list_filter = ('owner', )
	search_fields = ('id', 'name')


admin.site.register(Project, ProjectAdmin)
