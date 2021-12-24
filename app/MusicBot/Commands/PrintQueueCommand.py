from MusicBot.BaseClass.BaseCommand import *

class PrintQueueCommand(BaseCommand):
    async def execute(self, message, player):
        retMessage = '```\n'
        for idx in range(player.musicQueue.size()):
            retMessage += f'{player.musicQueue.at(idx)}\n'
        retMessage += '```'
        await message.channel.send(retMessage)
        return

    def help(self):
        return 'Prints the current queue.'