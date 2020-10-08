import discord
from discord.ext import commands

class helper(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.command() 
  async def give(self,ctx, *,args):
    print(args)



def setup(client):
    client.add_cog(helper(client))
    print('---> HELPER LOADED')
