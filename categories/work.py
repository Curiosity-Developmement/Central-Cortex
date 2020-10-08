import discord
from discord.ext import commands, tasks
from discord.utils import get
from datetime import datetime
import asyncio

msg_channel = 708443507131416606

class Misc(commands.Cog):
  def __init__(self,client):
    self.client=client
    self.working = {}
    self.onbreak = {}
    self.remove_work_role.start()
    self.remove_break_role.start()

  @tasks.loop(seconds=30)
  async def remove_work_role(self):
    if len(self.working)>0:
      t=datetime.now().minute
      #print(t)
      #print(self.working)
      for user_id in self.working:
        x=self.working[user_id][0]
        if x>59:
          x=x-60
        if t>=x:
          user = self.working[user_id][1]
          guild = self.client.get_guild(707698452066205867)
          role = get(guild.roles, name="I am Working Role")
          await user.remove_roles(role)
          
          
          role = get(user.guild.roles, name="I am on Break Role")
          await user.add_roles(role)
          self.onbreak[user.id]=[datetime.now().minute+self.working[user.id][2],user]
          
   
          channel = self.client.get_channel(msg_channel)
          #e=discord.Embed(title="",description=f"{user.mention} your working period ended.\nYou have {break_mins} minutes of rest.")
          #await channel.send(embed=e)
          await channel.send(f"{user.mention} your working period ended.\nYou have {self.working[user.id][2]} minutes of break time.")
          del self.working[user_id]

  @tasks.loop(seconds=30)
  async def remove_break_role(self):
    if len(self.onbreak)>0:
      t=datetime.now().minute
      #print(t)
      #print(self.onbreak)
      for user_id in self.onbreak:
        x=self.onbreak[user_id][0]
        if x>59:
          x=x-60
        if t>=x:
          user = self.onbreak[user_id][1]
          guild = self.client.get_guild(707698452066205867)
          role = get(guild.roles, name="I am on Break Role")
          await user.remove_roles(role)
          del self.onbreak[user_id]
          channel = self.client.get_channel(msg_channel)
          #e=discord.Embed(title="",description=f"{user.mention} your break period is over.")
          #await channel.send(embed=e)
          await channel.send(f"{user.mention} your break period is over.")

  @commands.command()
  async def work(self,ctx,work=None,breakt=None):
    if (work<=0 or breakt<=0):
      await self.client.get_channel(msg_channel).send(f"{ctx.author.mention} Either work or break time was less than equal to 0, please enter a positive number")
      return
    if work==None or breakt==None:
      await self.client.get_channel(msg_channel).send(f"{ctx.author.mention} invalid input\n`[work <work time> <break time>`")
      return
    else:
      member = ctx.message.author
      role = get(member.guild.roles, name="I am Working Role")
      await member.add_roles(role)
      role = get(member.guild.roles, name="I am on Break Role")
      await member.remove_roles(role)
      self.working[member.id]=[datetime.now().minute+work,member,breakt]
      try:
        self.remove_work_role.start()
      except:
        pass
      channel = self.client.get_channel(msg_channel)
      #e=discord.Embed(title="",description=f"> {ctx.author.mention} gave you the work role for {work_mins} minutes")
      #await channel.send(embed=e)
      await channel.send(f"{ctx.author.mention} gave you the work role for {work} minutes")




  


def setup(client):
  client.add_cog(Misc(client))
  print('---> MISC LOADED')
 