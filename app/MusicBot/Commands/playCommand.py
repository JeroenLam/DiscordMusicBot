from MusicBot.BaseClass.BaseCommand import *

class PlayCommand(BaseCommand):
    async def execute(self, message, player):
        await player.startAudio()

    def help(self):
        return 'Start playing songs from the queue'