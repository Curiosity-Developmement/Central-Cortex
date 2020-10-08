import discord
from discord.ext import commands
import json
import time
from datetime import datetime
from pytz import timezone
now_utc = datetime.now(timezone('UTC'))


class General(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def test(self, ctx):
    await ctx.send("lmao test is succesful idotcom")

  @commands.command()
  async def set(self, ctx, cmd=''): 
    if cmd == 'status':
      with open('afk.json', 'r') as f:
        afkDict = json.load(f)
      helper = 0
      for roles in ctx.author.roles:
        if roles.id == 710191407578480731:
            afkDict[str(ctx.author.id)] = {}
            l = ctx.content.split()
            string = ''
            l.pop(0)
            l.pop(0)
            for i in range(0, len(l)):
              string = string + str(l[i]) + " "
            afkDict[str(ctx.author.id)]["afk"] = string
            await ctx.send("Status has successfully been set as \"" + string +"\"")
            helper = 1
      if helper == 0:
        await ctx.send("This is a Helper only command!")
      with open('afk.json', 'w') as f:
        json.dump(afkDict, f)

  @commands.command()
  async def helper(self,ctx,cmd=''):
    if cmd == 'status':
      result = ""
      for value in afkDict:
        val = str(afkDict[value]["afk"])
        result += "<@!" + str(value) + ">: " + val + "\n"
      embed = discord.Embed(title = 'Helper Status\'s', description = result, color = 0x00ff00)
      await message.channel.send(embed = embed)
    

        


def setup(client):
  client.add_cog(General(client))
  print('---> GENERAL LOADED')
