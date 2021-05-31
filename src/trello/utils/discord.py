from discord_webhook import DiscordWebhook
from core.celery import app


@app.task
def added_manager(url, manager):
    webhook = DiscordWebhook(url=url, content=f'New manager in project {manager}')
    webhook.execute()


@app.task
def deleted_manager(url, manager):
    webhook = DiscordWebhook(url=url, content=f'{manager} manager delete from project')
    webhook.execute()


@app.task
def move_task(url, username, task, from_column, to_column):
    webhook = DiscordWebhook(url=url,
                content=f'"{username}", move "{task}" from "{from_column}", to "{to_column}"')
    webhook.execute()


@app.task
def remove_task(url, username, task):
    webhook = DiscordWebhook(url=url, content=f'"{username} remove task {task}')
    webhook.execute()


@app.task
def complete_task(url, username, task):
    webhook = DiscordWebhook(url=url, content=f'"{username} complete task "{task}"')
    webhook.execute()


@app.task
def created_task(url, username, task):
    webhook = DiscordWebhook(url=url, content=f'"{username} added task "{task}"')
    webhook.execute()
