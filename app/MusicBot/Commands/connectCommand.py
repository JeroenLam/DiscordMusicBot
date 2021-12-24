from MusicBot.BaseClass.BaseCommand import *

class ConnectCommand(BaseCommand):
    async def execute(self, message, player):
        await player.connect(message)

    def help(self):
        return 'Connect the bot to your voice channel'