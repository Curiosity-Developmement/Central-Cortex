import asyncio
from datetime import datetime
import time
import json
import os
from pytz import timezone
from webserver import keep_alive
from decouple import config

import discord
from discord.ext import commands

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
    print("All modules loaded!")


@client.event
async def on_member_join(member):
    channel1 = client.get_channel(708292001715716187)
    await channel1.send(
        f"Hey <@&710546419882262619>! Welcome {member.mention} to Curiosity, visit <#708702679148527657> to get your custom roles and see other channels."
    )


@client.event
async def on_member_remove(member):
    channel1 = client.get_channel(708292001715716187)
    await channel1.send(f"We have lost {member.name} ...What a pity.")


@client.event
async def on_message(message):
    if (message.channel.id == 712726793785704610 or message.channel.id == 713088442824654940):
      await message.add_reaction('\N{THUMBS UP SIGN}')
      await message.add_reaction('\N{THUMBS DOWN SIGN}')
    await client.process_commands(message)
     
@client.command(pass_context=True)
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)

keep_alive()
TOKEN = config("BOT_TOKEN")
client.run(TOKEN)
