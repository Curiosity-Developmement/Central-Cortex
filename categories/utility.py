import discord
from discord.ext import commands
from googletrans import Translator

trans = Translator()

class Template(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.command(prefixes=["trans","tr"])
  async def translate(self,ctx,sentence=None,i=None,u=None):
    if sentence==None:
      await ctx.send(f"{ctx.author.mention} correct usage : `[translate <text> <source language> <translated language>`")
      return
    if i==None and u==None:
      tred = trans.translate(sentence)
    elif i!=None and u==None:
      try:
        tred = trans.translate(sentence,src=i)
      except Exception as e:
        await ctx.send(f"ERROR\n```{e}```")
    elif i!=None and u!=None:
      try:
        tred = trans.translate(sentence,i,dest=u)
      except Exception as e:
        await ctx.send(f"ERROR\n```{e}```")
        
    emb = discord.Embed(title=f"Translated {sentence} from {tred.src} to {tred.dest}",description=f"requested by {ctx.author.mention}\n**__Translation__**{tred.text}\n**__Pronounciation__**\n{tred.pronunciation}")
    await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Template(client))
    print('---> TEMPLATE LOADED')