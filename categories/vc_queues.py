import discord
from discord.ext import commands

import asyncio

class VC_Queues(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command()
  async def vcQueues(self,ctx):
    await ctx.send("ready for further development -A1")

  # @commands.command() 
  # async def queue(self,ctx, *args):
  #   await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

  @commands.command() 
  async def queue( self,ctx, *args, ):

    



    argument = ""
    for i in range(len(args)):
      argument += args[i] + " "
    argument = argument.strip()
    print (argument == "vc help regular")
    print (argument)
    print ("vc help regular")
    if (argument == "vc help regular"):
      await ctx.send(argument)
    elif (argument == "vc help priority"):
      await ctx.send("[vc help priority is not valid please enter the prioritry queue number after the command in this form: '[queue vc help priority `queue#`'")
    elif (argument == "vc help priority 1"):
      await ctx.send("wip")
    else:
      await ctx.send(ctx.author)
      await ctx.send("Queue Not Found")


def setup(client):
    client.add_cog(VC_Queues(client))
    print('---> VCQueues LOADED')