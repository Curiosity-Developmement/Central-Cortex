import discord
from discord.ext import commands
import time

class Message_Events(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.Cog.listener()
    async def on_message(self,message):
        
        cnt = message.content.lower()
        if cnt=='frick':
            await message.channel.send("aw hecking heck on the fricking smeck, what the flecking fleck boi")
        if cnt=='wrong channel':
            time.sleep(0.2)
            await message.delete()
            await message.channel.send("Hello! You were sent this message because you are most likely using the wrong channel. If you cannot see the help channels, please go to <#708702679148527657> to get your roles!")
        if cnt=='no mass pings':
            time.sleep(0.2)
            await message.delete()
            await message.channel.send("Hello! You were sent this message because you most likely sent mass pings.")
        if message.channel.id == 713088442824654940:
            await message.add_reaction(emoji = "\U0001F44D")
            time.sleep(0.2)
            await message.add_reaction(emoji = "\U0001F44E")
        if cnt=='just post':
            time.sleep(0.2)
            await message.delete()
            await message.channel.send("No need to ask for help...just post the question and someone will come and ping you and help you through it")
    

def setup(client):
    client.add_cog(Message_Events(client))
    print('---> MESSAGE EVENTS LOADED')
