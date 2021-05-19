from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

User = get_user_model()


class Project(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='projects')
	name = models.CharField(verbose_name='Name', max_length=255)


class Column(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, related_name='columns')
	name = models.CharField(verbose_name='Name', max_length=255)


@receiver(post_save, sender=Project)
def create_columns(sender, instance, created, **kwargs):
	if created:
		Column.objects.create(project=instance, name='To do')
		Column.objects.create(project=instance, name='In testing')
		Column.objects.create(project=instance, name='Done')


class Task(models.Model):
	owner = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='tasks')
	column = models.ForeignKey(Column, on_delete=models.CASCADE, null=False, related_name='tasks')
	assignee = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='assigned_task')
	title = models.CharField(verbose_name='Title', max_length=255)
	due_date = models.DateField(verbose_name='Due date')
	description = models.TextField(verbose_name='Description')


class Subtask(models.Model):
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
