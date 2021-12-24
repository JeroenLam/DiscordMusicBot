from MusicBot.BaseClass.BaseCommand import *
import os

class ListMusicCommand(BaseCommand):
    async def execute(self, message, player):
        musicpath = player.musicPath

        for root, dirs, files in os.walk(musicpath):
            retMessage = '```\n'
            counter = 0
            for name in sorted(files):
                # Add name to the retMessage without the .mp3
                retMessage += name[:-4] + '\n'
                counter = counter + 1
                if counter > 99:
                    retMessage += '```'
                    await message.author.send(retMessage)
                    retMessage = '```\n'
                    counter = 0
            retMessage += '```'
        await message.author.send(retMessage) 
        return

    def help(self):
        return 'List all songs'