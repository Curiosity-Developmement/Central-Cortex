import discord
from discord.ext import commands


class Science(commands.Cog):
    def __init__(self, client):
        self.client = client

    # WE HAVE TO USE on_message() FOR COMMANDS WITH SPACES
    # DISCPRD.PY DOESNOT SUPPORT COMMANDS WITH SPACES
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.startswith("["):
            cmd = msg.content[1:].lower()

            # IONIC BONDING
            if cmd == 'ionic bonding':
                embed = discord.Embed(
                    title="**Ionic Bonding**",
                    description='''
Ionic Bonding is when 2 atoms bond through electromagnetic attraction
''',
                    color=000000)
                await msg.channel.send(embed=embed)


def setup(client):
    client.add_cog(Science(client))
    print('---> SCIENCE LOADED')
