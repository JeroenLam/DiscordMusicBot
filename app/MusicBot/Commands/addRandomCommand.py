from MusicBot.BaseClass.BaseCommand import *
import os
import random

class AddRandom2QueueCommand(BaseCommand):
    async def execute(self, message, player):
        # Set number of random songs to pick and the filter
        argv = message.content.split(' ')
        if len(argv) == 0:
            num = 1
            filter = ""
        elif len(argv) == 1:
            num = int(argv[0])
            filter = ""
        else:
            num = int(argv[0])
            filter = argv[1]

        retMsg = ""

        # Apply filter and get of resulting indeces
        for root, dirs, files in os.walk(player.musicPath):
            idx_arr = [idx for idx, elem in enumerate(files) if filter in elem]
            # If nothing fits the filter, return
            if len(idx_arr) == 0:
                await message.channel.send("No songs with that filter are available")
                return
            # Otherwise, pick 'num' random tracks
            for iter in range(num):
                idx = random.randint(0, len(idx_arr)-1)
                await player.addSong2Queue(files[idx_arr[idx]][:-4])
                retMsg += str("Added " + files[idx_arr[idx]][:-4] + " to the queue\n")
        await message.channel.send(retMsg)

    def help(self):
        return '<num> <filter>: Add <num> songs to the queue containing <filter> in their name'