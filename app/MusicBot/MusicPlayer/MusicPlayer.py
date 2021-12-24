import discord
import os
import asyncio

from MusicBot.MusicQueue.MusicQueue import MusicQueue

# Initiate a MusicPlayer for each server
class MusicPlayer:
    # Initialise Music player
    def __init__(self, musicPath):
        self.voiceClient = None
        self.musicQueue = MusicQueue()
        self.musicPath = musicPath
        self.isPlaying = False

    # If not connected, connect, if connected, move
    async def connect(self, message):
        if hasattr(message.author.voice, 'channel'):
            # Get users voice channel
            voice_channel = message.author.voice.channel
            # If not connected, connect
            if not self.isConnected():
                self.voiceClient = await voice_channel.connect()
            # If connected, move
            elif self.voiceClient.channel != voice_channel:
                await self.voiceClient.move_to(voice_channel)
        else:
            await message.channel.send("Please enter a voice channel")

    # Disconnect the bot from the voice channel
    async def disconnect(self):
        if self.isConnected():
            self.isPlaying = False
            await self.voiceClient.disconnect()

    # Return if connected
    def isConnected(self):
        if self.voiceClient is None:
            return False
        return self.voiceClient.is_connected()

    # Pause
    async def pauseVoice(self):
        if self.voiceClient.is_paused():
            self.voiceClient.resume()
        else:
            self.voiceClient.pause()

    # Play audio
    def playAudio(self, streamurl):
        if not self.isConnected():
            raise Exception("Connect to voice channel before playing")
        if self.voiceClient.is_playing():
            raise Exception("Stop playing before playing audio")
        self.voiceClient.play(discord.FFmpegPCMAudio(streamurl), after=lambda e: print())

    # Start playing music
    async def startAudio(self):
        # If paused, unpause and return
        if self.voiceClient.is_paused():
            await self.pauseVoice
            return

        if self.isPlaying == False:
            self.isPlaying = True
            # If the bot is not paused, i.e. not playing
            # while the queue is not empty
            while self.musicQueue.size() != 0 and self.isPlaying:
                # If playing, wait 5 seconds and try again
                if self.voiceClient.is_playing() or self.voiceClient.is_paused():
                    await asyncio.sleep(3)
                else:
                    # Take song from queue and play
                    newSong = self.musicQueue.dequeue()
                    if self.checkOnDisk(newSong):
                        streamurl = self.musicPath + newSong + '.mp3'
                        self.playAudio(streamurl)
            self.isPlaying = False

    # Stop playing music (stop current song and dont go to next)
    async def stopAudio(self):
        if self.isConnected():
            self.isPlaying = False
            self.voiceClient.stop()

    # Check if song is on disk
    def checkOnDisk(self, songName):
        for root, dirs, files in os.walk(self.musicPath):
            if str(songName + '.mp3') in files:
                return True
        return False

    # Add song to queue (if file exists on disk)
    async def addSong2Queue(self, songName):
        if self.checkOnDisk(songName):
            self.musicQueue.enqueue(songName)
            return True
        return False

    # Remove first match
    def removeMatchFromQueue(self, songName):
        if str(songName) in self.musicQueue.queue:
            idx = self.musicQueue.index(songName)
            self.musicQueue.removeIdx(idx)
            return True
        return False

    # Remove first fuzzy
    def removeFirstFromQueue(self, songName):
        return self.musicQueue.remove(songName)

