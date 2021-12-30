from MusicBot.BaseClass.BaseCommand import *

class AddStreamCommand(BaseCommand):
    async def execute(self, message, player):
        player.playAudio(message)

    def help(self):
        return '<SteamUrl>: Play Stream'