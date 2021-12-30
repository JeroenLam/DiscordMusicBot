from MusicBot.BaseClass.BaseCommandHandler import *

# Importing commands
from MusicBot.Commands.connectCommand import ConnectCommand
from MusicBot.Commands.disconnectCommand import DisconnectCommand
from MusicBot.Commands.add2QueueCommand import Add2QueueCommand
from MusicBot.Commands.playCommand import PlayCommand
from MusicBot.Commands.PrintQueueCommand import PrintQueueCommand
from MusicBot.Commands.pauseCommand import PauseCommand
from MusicBot.Commands.stopCommand import StopCommand
from MusicBot.Commands.removeComands import *
from MusicBot.Commands.skipCommand import SkipCommand
from MusicBot.Commands.addRandomCommand import AddRandom2QueueCommand
from MusicBot.Commands.listMusicCommand import ListMusicCommand
from MusicBot.Commands.addStreamCommand import AddStreamCommand

class CommandHandler(BaseCommandHandler):
    # On initialisation, define all commands in the command handler
    def __init__(self):
        BaseCommandHandler.__init__(self)
        self.addCommand('c', ConnectCommand())
        self.addCommand('connect', ConnectCommand())
        self.addCommand('d', DisconnectCommand())
        self.addCommand('disconnect', DisconnectCommand())
        self.addCommand('a', Add2QueueCommand())
        self.addCommand('add', Add2QueueCommand())
        self.addCommand('ar', AddRandom2QueueCommand())
        self.addCommand('addr', AddRandom2QueueCommand())
        self.addCommand('s', PlayCommand())
        self.addCommand('start', PlayCommand())
        self.addCommand('q', PrintQueueCommand())
        self.addCommand('queue', PrintQueueCommand())
        self.addCommand('p', PauseCommand())
        self.addCommand('pause', PauseCommand())
        self.addCommand('stop', StopCommand())
        self.addCommand('rm', RemoveNextExactCommand())
        self.addCommand('rmall', RemoveAllExactCommand())
        self.addCommand('rmf', RemoveNextFuzzyCommand())
        self.addCommand('rmfall', RemoveAllFuzzyCommand())
        self.addCommand('skip', SkipCommand())
        self.addCommand('l', ListMusicCommand())
        self.addCommand('list', ListMusicCommand())
