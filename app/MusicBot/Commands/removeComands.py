from MusicBot.BaseClass.BaseCommand import *

class RemoveNextExactCommand(BaseCommand):
    async def execute(self, message, player):
        argv = message.content.split(' ')
        for arg in argv:
            player.removeMatchFromQueue(arg)

    def help(self):
        return '<songname> ... <songname: Removes next instance of <songname> from the queue'

class RemoveAllExactCommand(BaseCommand):
    async def execute(self, message, player):
        argv = message.content.split(' ')
        for arg in argv:
            while player.removeMatchFromQueue(arg):
                1

    def help(self):
        return '<songname> ... <songname>: Removes all instances of <songname> from the queue'

class RemoveNextFuzzyCommand(BaseCommand):
    async def execute(self, message, player):
        argv = message.content.split(' ')
        for arg in argv:
            player.removeFirstFromQueue(arg)

    def help(self):
        return '<string> ... <string>: Removes next instance containing <string> from the queue'

class RemoveAllFuzzyCommand(BaseCommand):
    async def execute(self, message, player):
        argv = message.content.split(' ')
        for arg in argv:
            while player.removeFirstFromQueue(arg):
                1

    def help(self):
        return '<string> ... <string>: Removes all instances containing <string> from the queue'