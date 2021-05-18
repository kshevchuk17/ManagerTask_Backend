from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Project(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, related_name='projects')
	name = models.CharField(verbose_name='Name', max_length=255)


class Column(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, related_name='columns')
	name = models.CharField(verbose_name='Name', max_length=255)


class Task(models.Model):
	owner = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='tasks')
	column = models.ForeignKey(Column, on_delete=models.CASCADE, null=False, related_name='tasks')
	title = models.CharField(verbose_name='Title', max_length=255)
	due_date = models.DateField(verbose_name='Due date')
	description = models.TextField(verbose_name='Description')


class Subtask(models.Model):
	owner = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='subtasks')
	task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False, related_name='subtasks')
	title = models.CharField(verbose_name='Title', max_length=255)
	due_date = models.DateField(verbose_name='Due date')
	description = models.TextField(verbose_name='Description')


class Attachment(models.Model):
	task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False, related_name='attachments')
	file = models.FileField(verbose_name='File')


class Comment(models.Model):
	owner = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='comments')
	task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False, related_name='comments')
	comment = models.TextField(verbose_name='Comment')
