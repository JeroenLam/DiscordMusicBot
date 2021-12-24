# Discord Music Bot

This repository contains the code for a music bot. Feel free to clone or fork the code for your own use.

To extend the bot you can derive a new command object from the existing `BaseCommand` and overwrite the `async def execute(self, message)` function with the actual functionallity of the command. Also overwrite the `async def help(self)` that returns the command discription for the help function.

The current framework support admin users. These can be set in the `.env` file (for an example see `ex-.env-file`). These commands can be defined in the `AdminCommands/` forlder and are defined in the same way as normal commands.

# Instalation manual
Before you start please make sure you have the following packages installed: \
`discord.py[voice]`

To use the bot you will need to clone the repository. Then you need to configure a `.env` file with all the parameters. An example `.env` file is included. To run the bot use the command `python3 main.py`. The bot should work on all operating systems supporting python.

To remove functionality from the bot or if you want to change the command names that trigger a command, then change the lines in `Commands/CommandHandler.py` or `Admin/AdminCommandHandler.py`.

If you wish to add your own functions to the bot, then derive a new command class from `BaseCommand` (located in `Support/BaseCommand`) and overwrite the corresponding functions. Also do not forget to include the newly created command in the corresponding command handler.

# Installation Docker
To run the bot in docker, update the `docker-compose.yaml` to include a path to the music folder you want to use. Create a `.env` file with your credentials, an example is included. To start the bot, run: \
`docker-compose up --build -d`

# Commands (everyone)
The following list is generated using the `help` command. Note that the appropriate profix should be added to these commands.
```c         : Connect the bot to your voice channel
connect   : Connect the bot to your voice channel
d         : Disconnect the bot from your voice channel
disconnect: Disconnect the bot from your voice channel
a         : <song-1> ... <song-n>: Add songs to the queue
add       : <song-1> ... <song-n>: Add songs to the queue
ar        : <num> <filter>: Add <num> songs to the queue containing <filter> in their name
addr      : <num> <filter>: Add <num> songs to the queue containing <filter> in their name
s         : Start playing songs from the queue
start     : Start playing songs from the queue
q         : Prints the current queue.
queue     : Prints the current queue.
p         : Pause the song
pause     : Pause the song
stop      : Stop playing songs from the queue
rm        : <songname> ... <songname: Removes next instance of <songname> from the queue
rmall     : <songname> ... <songname>: Removes all instances of <songname> from the queue
rmf       : <string> ... <string>: Removes next instance containing <string> from the queue
rmfall    : <string> ... <string>: Removes all instances containing <string> from the queue
skip      : Skip the current song
l         : List all songs
list      : List all songs
```
  
# Commands (admins)
The following list is generated using the `help` command. Note that the appropriate profix should be added to these commands.
```
add       : <name> : Add a song to the server
mv        : <old name> <new name> : Rename a song on the server
cp        : <old name> <new name> : Copy a song
rm        : <song name> ... <song name> : Delete song(s) from the server
```
