import discord
from discord.ext import commands
import json
import asyncio       


async def daily_task():
    with open('debate.json', 'r') as f:
        topics = json.load(f)
    await asyncio.sleep(24 * 60 * 60)
    with open('debate.json', 'w') as f:
        json.dump(topics, f)



class Debate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def debate(self, ctx, cmd='', *, sug=''):
        # DEBATE
        if cmd == '':
            embed = discord.Embed(
                title="**Debate Help**",
                description=
                "``[debate suggest <suggestion>`` - suggest a debate motion to be added into our database(must follow BP motion format)\n\n``[debate list`` - list of all current debate motions",
                color=0x00ff00)
            await ctx.send(embed=embed)

        # DEBATE LIST
        elif cmd.lower() == 'list':
            with open('debate.json', 'r') as f:
                topics = json.load(f)
            for i in range(0, len(topics)):
                await ctx.channel.send(topics[i])
            with open('debate.json', 'w') as f:
                json.dump(topics, f)

        # DEBATE SUGGEST
        elif cmd.lower() == 'suggest':
            if sug == '':
                await ctx.send(
                    f"{ctx.author.mention}``[debate suggest <suggestion>`` - suggest a debate motion to be added into our database(must follow BP motion format)"
                )
            else:
                string = sug[:]
                print(string)
                channel1 = ctx.guild.get_channel(707699849549709362)
                await channel1.send(f">> **{ctx.author.name}** **NEW Debate Suggestion**\n> {string}")
                await ctx.send(f"Successfully submitted debate motion\n`{string}`")


def setup(client):
    client.add_cog(Debate(client))
    print('---> DEBATE LOADED')
