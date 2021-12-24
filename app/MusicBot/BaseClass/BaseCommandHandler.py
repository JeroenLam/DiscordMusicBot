# Include all other commands
from MusicBot.BaseClass.BaseCommand import *


class BaseCommandHandler:
    # Dict containing all commands
    def __init__(self):
        self.commands = {}

    # Adds the command to the command handler
    def addCommand(self, name, function):
        self.commands[name] = function

    async def run(self, message, player):
        # Tokenize message to get first entry
        argv = message.content.split(' ')
        command = argv[0].lower()

        # Remove command from the input string and remove leading whitespaces
        message.content = message.content[len(command):].lstrip()

        # If command == help, send all commands and their descriptions to the user
        if command == 'help':
            retMessage = '```\n'
            for com_name in self.commands:
                retMessage += f'{com_name.ljust(10)}: {self.commands[com_name].help()}\n'
            retMessage += '```'
            await message.author.send(retMessage)
            return

        com = BaseCommand()
        # Attempt to run the command from the list of commands
        try:
            com = self.commands[command]
        except:
            print('ERROR: Invalid command ' + str(message.author) + ' - ' + command + ' - ' + message.content)
            await message.channel.send("Invalid command!")
            return

        # Run the command in case it exists
        await com.execute(message, player)
        print('  executed ' + str(message.author) + ' - ' + command + ' - ' + message.content)

    # Prints the content of the commandhandler, used for debugging
    def print(self):
        print(self.commands)
