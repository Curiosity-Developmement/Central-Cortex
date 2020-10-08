import discord
from discord.ext import commands


class French(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def french(self, ctx):
        embed = discord.Embed(
            title='**French Commands**',
            description='''
[conjugate `er`, `ir`''',
            color=0x00ff000)
        await ctx.send(embed=embed)

    @commands.command()
    async def conjugate(self, ctx, c=''):
        if c == 'er':
            embed = discord.Embed(
                title='**__-er verb conjugations__**',
                description=
                '''**Example:** `danser` *(infinitive)* To dance\n''',
                color=0x00ff00)
            embed.add_field(
                name="Singular Pronouns",
                value=
                "**Je** *danse* `-e`\n**Tu** *danses* `-es`\n**Il/Elle/On** *danse* `-e`",
                inline=True)
            #petition for multi line commenting
            #aye
            #petition to space things out so my head doesnt hurt and delte the spaces later
            #ew
            embed.add_field(
                name="Plural Pronouns",
                value=
                "**Nous\*** *dansons* `-ons`\n**Vous** *dansez* `-ez`\n**Ils/Elles** *dansent* `-ent`",
                inline=True)
            embed.add_field(
                name="\***Note: **",
                value=
                "*For verbs that end with -ge, such as **mange** (to eat) and **nager** (to swim), the \"nous\" ending is `-eons` instead of the standard `-ons` ending. Eg. `mangeons`.*",
                inline=False)
            embed.set_footer(text='For help with pronouns, use [prenom')
            embed.set_thumbnail(
                url=
                'https://media.discordapp.net/attachments/707699849549709362/713514115410296903/baguette-arrow-png-1.png'
            )
            await ctx.send(embed=embed)
        elif c == 'ir':
            embed = discord.Embed(
                title='**__-ir verb conjugations__**',
                description=
                '''**Example:** `finir` *(infinitive)* To finish\n''',
                color=0x00ff00)
            embed.add_field(
                name="Singular Pronouns",
                value=
                "**Je** *finis* `-is`\n**Tu** *finis* `-is`\n**Il/Elle/On** *finit* `-it`",
                inline=True)
            #petition for multi line commenting
            #aye
            #aye
            embed.add_field(
                name="Plural Pronouns",
                value=
                "**Nous** *finissons* `-issons`\n**Vous** *finissez* `-issez`\n**Ils/Elles** *finissent* `-issent`",
                inline=True)
            embed.add_field(
                name="**Irregular -ir Verbs: **",
                value=
                "*Several -ir verbs, such as **partir** (to go), **offrir** (to offer), and **devenir** (to become), are part of irregular -ir verb groups and have different conjugations. An introduction can be found [here](https://www.lawlessfrench.com/grammar/irregular-ir-verbs/ 'Irregular -ir Conjugations').*",
                inline=False)
            embed.set_footer(text='For help with pronouns, use [prenom')
            embed.set_thumbnail(
                url=
                'https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/1200px-Flag_of_France.svg.png'
            )
            await ctx.send(embed=embed)
        else:
          await ctx.invoke(self.client.get_command('french'))


def setup(client):
    client.add_cog(French(client))
    print('---> FRENCH LOADED')
