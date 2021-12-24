from MusicBot.BaseClass.BaseCommand import *
import os

class DeleteSongCommand(BaseCommand):
    async def execute(self, message, player):
        musicpath = player.musicPath

        argv = message.content.split(' ')
        for arg in argv:
            arg += '.mp3'
            for root, dirs, files in os.walk(musicpath):
                for name in files:
                    if name == arg:
                        os.remove(musicpath + name)
                        await message.channel.send('Removed ' + name)       

    def help(self):
        return '<song name> ... <song name> : Delete song(s) from the server'