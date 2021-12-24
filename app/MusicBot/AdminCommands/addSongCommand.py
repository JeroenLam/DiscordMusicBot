from MusicBot.BaseClass.BaseCommand import *
from MusicBot.Support.download import download

class AddSongCommand(BaseCommand):
    async def execute(self, message, player):
        argv = message.content.split(' ')

        if len(message.attachments): 
            url = message.attachments[0].proxy_url
            if url[-4:] == '.mp3':                                          # verify the extension
                fileName = url[url.rfind('/') + 1:]                             # scrape the filename
                data = download(url)                                            # Download the data
                with open(player.musicPath + fileName, 'wb') as output:             # Safe the data on disk
                    output.write(data.read())

                await message.channel.send('Added ' + fileName)
            else:
                await message.channel.send('We only accept .mp3 files')
        else:
            await message.channel.send('No valid attachments!')

    def help(self):
        return '<name> : Add a song to the server'