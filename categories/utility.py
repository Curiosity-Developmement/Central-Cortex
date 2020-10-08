import discord
from discord.ext import commands

class Template(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.command()
  async def template(self,ctx):
    # Stuff 2 send goes here
    await ctx.send("template")



def setup(client):
    client.add_cog(Template(client))
    print('---> TEMPLATE LOADED')