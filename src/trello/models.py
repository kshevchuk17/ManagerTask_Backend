from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch.dispatcher import receiver
from .utils.discord import DiscordHook


User = get_user_model()


class Project(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='owner_projects')
	managers = models.ManyToManyField(User, related_name='manager_project', blank=True)
	name = models.CharField(verbose_name='Name', max_length=255)
	discord_url = models.URLField(verbose_name='Disckord URL', default=None)


class Column(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, related_name='columns')
	name = models.CharField(verbose_name='Name', max_length=255)


@receiver(post_save, sender=Project)
def create_columns(sender, instance, created, **kwargs):
	if created:
		Column.objects.create(project=instance, name='To do')
		Column.objects.create(project=instance, name='In testing')
		Column.objects.create(project=instance, name='Done')


@receiver(post_save, sender=Project)
def add_manager_in_project(sender, instance, created, **kwargs):
	DiscordMessage = DiscordHook(url=instance.discord_url, username=instance.owner.username, manager=list(i.username for i in instance.managers.all()))
	DiscordMessage.added_manager()


class Task(models.Model):
	owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tasks')
	column = models.ForeignKey(Column, on_delete=models.CASCADE, null=False, related_name='tasks')
	assignee = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='assigned_task')
	title = models.CharField(verbose_name='Title', max_length=255)
	due_date = models.DateField(verbose_name='Due date',  null=True, blank=True)
	created_at = models.DateField(verbose_name='Due date', auto_now_add=True)
	is_complete = models.BooleanField(verbose_name='Is_Complete', default=False)
	description = models.TextField(verbose_name='Description')
	_old_column = None

	def __init__(self, *args, **kwargs):
		super(Task, self).__init__(*args, **kwargs)
		self._old_column = self.column

	def save(self, *args, **kwargs):
		super(Task, self).save(*args, **kwargs)
		self._old_column = self.column


@receiver(post_save, sender=Task)
def create_update_move_task(sender, instance, created, *args, **kwargs):
	if created:
		DiscordMessage = DiscordHook(url=instance.column.project.discord_url, username=instance.assignee, task=instance.title)
		DiscordMessage.created_task()

	if instance._old_column != instance.column:
		DiscordMessage = DiscordHook(url=instance.column.project.discord_url, username=instance.assignee, task=instance.title, from_column=instance._old_column.name,
									 to_column=instance.column.name)
		DiscordMessage.move_task()
	elif instance.is_complete:
		DiscordMessage = DiscordHook(url=instance.column.project.discord_url, username=instance.assignee, task=instance.title)
		DiscordMessage.complete_task()


@receiver(post_delete, sender=Task)
def delete_task(sender, instance, *args, **kwargs):
	if instance.id:
		DiscordMessage = DiscordHook(url=instance.column.project.discord_url, username=instance.assignee, task=instance.title)
		DiscordMessage.remove_task()


class Subtask(models.Model):
	task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False, related_name='subtasks')
	title = models.CharField(verbose_name='Title', max_length=255)
	created_at = models.DateField(verbose_name='Due date', auto_now_add=True)
	due_date = models.DateField(verbose_name='Due date', null=True, blank=True)
	is_complete = models.BooleanField(verbose_name='Is_Complete', default=False)
	description = models.TextField(verbose_name='Description')


class Attachment(models.Model):
	task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False, related_name='attachments')
	file = models.FileField(verbose_name='File')


class Comment(models.Model):
	owner = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='comments')
	task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False, related_name='comments')
	comment = models.TextField(verbose_name='Comment')
