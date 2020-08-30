import asyncio
from datetime import datetime
import time
import json
import os
from pytz import timezone
from webserver import keep_alive

import discord
from discord.ext import commands
"""
from frenchCommands import runFrench
from mathCommands import runMath
from generalCommands import runGeneral
from scienceCommands import runScience
#from debateCommands import runDebate
#from compSciCommands import runCompSciCommands"""

print("---> BOT is waking up\n")

client = commands.Bot(command_prefix="[",case_insensitive=True)
now_utc = datetime.now(timezone('UTC'))
client.remove_command('help')




def load_cogs():
  for file in os.listdir('./categories'):
        if file.endswith('.py'):
            client.load_extension(f'categories.{file[:-3]}')


@client.event
async def on_ready():
    #await client.change_presence(activity=discord.Game(name='Undergoing Development'))
    await client.wait_until_ready()
    load_cogs()
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, name="your questions."))
    print("Brain Cell 1 operational, not sure about number 2 tho")


@client.event
async def on_member_join(member):
    channel1 = client.get_channel(708292001715716187)
    await channel1.send(
        f"Hey <@&710546419882262619>! Welcome {member.mention} to Curiosity, visit <#708702679148527657> to get your custom roles and see other channels."
    )


@client.event
async def on_member_remove(member):
    channel1 = client.get_channel(708292001715716187)
    await channel1.send(f"""We have lost {member.mention}...""")
    time.sleep(0.5)
    await channel1.send("*Server Curiosity has dropped by 1*")

""""
@client.event
async def on_message(message):

    if message.author == client.user:
        return
    await runFrench(message)
    await runMath(message)
    await runGeneral(message)
    await runScience(message)
    #await runDebate(message)
    #await runCompSciCommands(message)
    await client.process_commands(message)"""


keep_alive()
TOKEN = "BOT_TOKEN"
client.run(TOKEN)
