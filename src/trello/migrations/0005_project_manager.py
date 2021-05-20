# Generated by Django 3.2.3 on 2021-05-19 11:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trello', '0004_alter_task_assignee'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='manager',
            field=models.ManyToManyField(related_name='project', to=settings.AUTH_USER_MODEL),
        ),
    ]
