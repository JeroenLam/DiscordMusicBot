from MusicBot.BaseClass.BaseCommand import *

class SkipCommand(BaseCommand):
    async def execute(self, message, player):
        await player.stopAudio()
        await player.startAudio()

    def help(self):
        return 'Skip the current song'