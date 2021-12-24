from MusicBot.BaseClass.BaseCommand import *

class StopCommand(BaseCommand):
    async def execute(self, message, player):
        await player.stopAudio()

    def help(self):
        return 'Stop playing songs from the queue'