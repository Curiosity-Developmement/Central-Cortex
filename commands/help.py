import discord
from discord.ext import commands

class Help(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.command()
  async def help(self,ctx):
    embed = discord.Embed(title = '**Help**', description = """
`[math` - Math commands can be found here
`[french` - French commands can be found here"""
    , color = 0x00ff000)
    await ctx.send(embed = embed)



def setup(client):
    client.add_cog(Help(client))
    print('---> HELP LOADED')
