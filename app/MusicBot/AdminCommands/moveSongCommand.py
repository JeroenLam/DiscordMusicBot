from MusicBot.BaseClass.BaseCommand import *
import os

class MoveSongCommand(BaseCommand):
    async def execute(self, message, player):
        # Storing path to soundboard files
        musicpath = player.musicPath
        argv = message.content.split(' ')
        if len(argv) != 2:
            await message.channel.send('Please provide 2 arguments as explained in the help function')
            return
        
        bool_found = 0
        name_old = argv[0] + '.mp3'
        name_new = argv[1] + '.mp3'
        for root, dirs, files in os.walk(musicpath):
            for name in files:
                if name == name_old:
                    os.rename(musicpath + name, musicpath + name_new)
                    bool_found = 1
                    await message.channel.send('Renamed ' + name_old + ' to ' + name_new)
        if not bool_found:
            await message.channel.send('No file found named: ' + name_old) 


    def help(self):
        return '<old name> <new name> : Rename a song on the server'