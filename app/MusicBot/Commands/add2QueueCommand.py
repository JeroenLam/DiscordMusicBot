from MusicBot.BaseClass.BaseCommand import *

class Add2QueueCommand(BaseCommand):
    async def execute(self, message, player):
        # Split message content by spaces
        songList = message.content.split(' ')
        # Add each song to the queue in order
        for song in songList:
            if not await player.addSong2Queue(song):
                await message.channel.send("Not a valid song: *" + song + "*")
            #else:
                #await message.channel.send("Added *" + song + "* to the queue")
        await message.channel.send("Added song(s) to the queue")

    def help(self):
        return '<song-1> ... <song-n>: Add songs to the queue'