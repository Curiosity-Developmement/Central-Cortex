import discord
from discord.ext import commands

class Help(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.command()
  async def help(self,ctx,help='',*,q=''):
    help=help.lower()

    # if user asks for python help, call the python help command with q as argument
    if help=='python':
      await ctx.invoke(self.client.get_command('python'),q=q)
    else:
      embed = discord.Embed(title = '**Help**', description = """
  **Prefix** : ``[``
  `[math` - Math commands can be found here
  `[french` - French commands can be found here
  `[debate` - Debate commands can be found here
  `[python` - Python help
  `[java` - java help"""
      , color = 0x00ff000)
      await ctx.send(embed = embed)



def setup(client):
    client.add_cog(Help(client))
    print('---> HELP LOADED')
