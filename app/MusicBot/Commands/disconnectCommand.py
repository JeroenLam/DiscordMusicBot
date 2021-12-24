from MusicBot.BaseClass.BaseCommand import *

class DisconnectCommand(BaseCommand):
    async def execute(self, message, player):
        if hasattr(message.author.voice, 'channel'):
            await player.disconnect()
            

    def help(self):
        return 'Disconnect the bot from your voice channel'