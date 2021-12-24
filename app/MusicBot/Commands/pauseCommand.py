from MusicBot.BaseClass.BaseCommand import *

class PauseCommand(BaseCommand):
    async def execute(self, message, player):
        await player.pauseVoice()

    def help(self):
        return 'Pause the song'