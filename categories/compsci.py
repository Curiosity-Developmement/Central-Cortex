import io
import contextlib
import discord
from discord.ext import commands
import platform

import asyncio

class compSci(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command()
  async def compsci(self,ctx):
    await ctx.send("ready for further development -A1 (this is comp sci and coding and tech and computers etc)")

  @commands.command()
  async def python(self,ctx,*,q=''):
    if q=='':
      embed = discord.Embed(
        title = "Python Documentation", description = """Python is a versitile language that is easy for beginners to pick up. Although python is slow, it makes up for its speed in its versatility and its compatibility. 
      WIP""", colour = 0xFFCC00)
    else:
      out=io.StringIO()
      with contextlib.redirect_stdout(out):
        help(q)
      text=out.getvalue()
      embed = discord.Embed(title=f'help on {q}',description=text[:2000],colour = 0xFFCC00)
      embed.add_field(name=f"sent help using help({q})",value=f"python version {platform.python_version()}")
      if len(text)>2000: await ctx.send("**sending help upto the first 2000 characters coz thats the limit**")
    await ctx.send(embed = embed)
    

  @commands.command()
  async def java(self,ctx):
    embed = discord.Embed(
      title = "Java Documentation", description = """Java is the original JVM programming language. It gets a fair bit of its syntax from C++ and C, but it's simpler to use and it uses object-oriented programming. 
    WIP""", colour = 0xFFCC00)
    await ctx.send(embed = embed)

  @commands.command()
  async def code(self,ctx):
    await ctx.send('hmm')

  # @commands.command()
  # async def help_python(self,ctx):
  #   await ctx.send("ok")


def setup(client):
    client.add_cog(compSci(client))
    print('---> COMP SCI LOADED')