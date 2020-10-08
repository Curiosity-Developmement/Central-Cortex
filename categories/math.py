import discord
from discord.ext import commands
        

class Math(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.command()
  async def math(self,ctx):
    embed = discord.Embed(title = "Math Commands", description = """
[formula `area`, `volume`, `special`, `trig`, `surface area` - returns fomrulas for each category
[trig - Conventional Trigonometry(sine, cosine, tangent)
[poi - Point of Intersection
[`pi`, `theta` - Special math characters
[vertical line test, `vlt` - info about vlt
""", color = 0x00ff00)
    await ctx.send(embed = embed)

  @commands.command()
  async def pi(self,ctx):
    await ctx.send("`π` is 3.1415... and is the ratio of Circumference over diameter")
  
  @commands.command()
  async def theta(self,ctx):
    await ctx.send("`θ` is theta, it usally represents an unknown value (in degrees or radians)")

  @commands.command()
  async def trig(self,ctx):
    embed = discord.Embed(title = "**Trigonometry with right triangles**", description = '''
Pre-Requisites for using conventional trigonometry(sin, cos, tan):
    *Must be a right triangle with the angle indicated
    If you want to find an unknown angle, you must have a known side lengths
    If you want to find an unknown side length, you must know an angle and 1 other side length*
    
Trig works on finding the ratio of 2 measurements and using an operator to determine the unknown. ''', color = 0x00ff00)
    embed1 = discord.Embed(title = "", description = '''
In trig, all sides are relative to the unknown angle, or,in the case of an unknown side, the known angle:

Let's say that the bottom left angle is unknown.
The flat side with the dashes(---) is adjacent(a) because it is right beside the angle. The hypotenuse(h) is the side opposite the right angle in the bottom right. The remaining side is opposite because it is opposite to the angle. 
Remember, this is all in relation to the bottom left angle.abs

Now that we have the sides labelled, remember this acronym:
**soh cah toa**
Say it with me:
**soh cah toa**
Pronounced: SO-KA-toe-A

This acronym produces your relation. 'soh' means *sin opposite hypotenuse*, what this means is sin of theta(unknown angle) is opposite over hypotenuse:
sinθ = opp/hyp
Follwing this trend we can see that:
cosθ = adj/hyp
tanθ = opp/adj
Plug in your knowns, then to solve for sin/cos/tan, do the inverse trig function. Which is the function to the exponent -1(e.g. sin^-1, cos^-1, tan^-1):
θ = tan^-1(opp/adj)]

And that is conventional trignomentry for you''', color = 0x00ff00)
    await ctx.send(embed = embed)
    await ctx.send("https://media.discordapp.net/attachments/708443507131416606/711240893335732264/right3.gif")
    await ctx.send(embed = embed1)



  @commands.command()
  async def vlt(self,ctx):
    embed = discord.Embed(title = '**The Vertical Line Test**', description = '''
The vertical lien test is a test conducted to check if a specific line on a cartesian plane is a function or not

It is used by taking a vertical line (parellell to the y-axis) and extending it infinitely. And if the line in question(the line you are checking ot see if it is a function) intersects(crosses) this vertical line more than once, it is not a function''', color = 0x00ff00)
    await ctx.send(embed=embed)
    await ctx.send("https://bit.ly/2XPKH2d")

  # FORMULA
  @commands.command()
  async def formula(self,ctx,*,query=''):
    query=query.lower()

    # FORMULA AREA
    if query == 'area':
      embed = discord.Embed(title = '**Area Formulas**', description = '''
Square - **A = s^2**
Rectangle - **A = lw**
Circle - **A = πr^2**
Triangle - **A = bh/2**''', color = 0x00ff000)
      await ctx.send(embed=embed)
    
    # FORMULA VOLUME
    elif query == 'volume':
      embed = discord.Embed(title = '**Area Formulas**', description = '''
Cube - **Volume = s^3**
Regular Prism - **Volume = Bh** (Where "B" is the area of the base)
Cone - **πr^2*(h/3)**
''', color = 0x00ff000)
      await ctx.send(embed=embed)

    # FORMULA SPECIAL
    elif query == 'special':
      embed = discord.Embed(title = '**Area Formulas**', description = '''
**(a+b)^2 = a^2 + 2ab + b^2
(a-b)^2 = a^2 - 2ab + b^2
(a+b)(a+b) = a^2 + b^2'
(a+b)(a-b) = a^2 - b^2**''', color = 0x00ff000)
      await ctx.send(embed=embed)

    # FORMULA TRIG
    elif query == 'trig':
      embed = discord.Embed(title = '**Trig Formulas**', description = '''
soh cah toa:
    **sinθ = opposite/hypotenuse
    cosθ = adjacent/hypotenuse
    tanθ = opposite/adjacent**
Sine Law: **a/sinA = b/sinB = c/sinC**
Cosine Law: **c^2 = a^2 + b^2 − 2abcos(C)**
    ''', color = 0x00ff000)
      await ctx.send(embed=embed)

    # FORMULA SURFACE AREA
    elif query == 'surface area':
      embed = discord.Embed(title = '**Surface Area Formulas**', description = '''
Cube - **6s^2**
Regular Prism - **2B + Ph** (Where B is the base and P is the perimeter of the base)
Cylinder - **2πr^2 + πr^2h**
''', color = 0x00ff00)
      await ctx.send(embed = embed)

  @commands.command()
  async def poi(self,ctx):
    embed = discord.Embed(title = "Point of Intersection", description = '''
In order to find the point of intersection, you must take the y intercept formula of 2 slopes(y = mx+b form) and then you can either use substituion or elimination to solve for x or y.

Example:
y = x-7
y = 2x-8
These 2 are both equal to y, therefore:
x-7 = 2x-8
**x = 1**
Once you get the answer for one variable, plug it back into one of the first equaitons:

**x = 1**
y = **1** - 7
**y = -6**
Therefore, we can conclude that the Point of Intersection of the lines y = x-7 and y = 2x-8 is (1, -6)''', color = 0x00ff00)
    await ctx.send(embed=embed)

      

def setup(client):
    client.add_cog(Math(client))
    print('---> MATH LOADED')
  