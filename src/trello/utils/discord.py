from discord_webhook import DiscordWebhook


class DiscordHook:
    def __init__(self, url, username='', from_column='', to_column='', task='', manager=''):
        self.username = username
        self.from_column = from_column
        self.to_column = to_column
        self.task = task
        self.manager = manager
        self.url = url

    def added_manager(self):
        for manager in self.manager:
            webhook = DiscordWebhook(url=self.url, content=f'New manager in project {manager}')
            webhook.execute()

    def move_task(self):
        webhook = DiscordWebhook(url=self.url,
                    content=f'"{self.username}", move "{self.task}" from "{self.from_column}", to "{self.to_column}"')
        webhook.execute()

    def remove_task(self):
        webhook = DiscordWebhook(url=self.url, content=f'"{self.username} remove task {self.task}')
        webhook.execute()

    def complete_task(self):
        webhook = DiscordWebhook(url=self.url, content=f'"{self.username} complete task "{self.task}"')
        webhook.execute()

    def created_task(self):
        webhook = DiscordWebhook(url=self.url, content=f'"{self.username} added task "{self.task}"')
        webhook.execute()
