from MusicBot.BaseClass.BaseCommandHandler import *

# Importing commands
from MusicBot.AdminCommands.addSongCommand import AddSongCommand
from MusicBot.AdminCommands.moveSongCommand import MoveSongCommand
from MusicBot.AdminCommands.copySongCommand import CopySongCommand
from MusicBot.AdminCommands.deleteSongCommand import DeleteSongCommand

class AdminCommandHandler(BaseCommandHandler):
    # On initialisation, define all commands in the command handler
    def __init__(self):
        BaseCommandHandler.__init__(self)
        self.addCommand('add', AddSongCommand())
        self.addCommand('mv', MoveSongCommand())
        self.addCommand('cp', CopySongCommand())
        self.addCommand('rm', DeleteSongCommand())