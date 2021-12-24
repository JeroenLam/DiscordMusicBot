# Base command to derive from for other commands

class BaseCommand:
    async def execute(self, message, player):
        print("ERROR: base command not overwriten")

    def help(self):
        return 'ERROR: command explination not defined by programmer'