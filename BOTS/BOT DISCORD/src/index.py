import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description="This is a helper bot")

# COMANDOS
@bot.command()
async def ping(ctx):
    """..."""

    await ctx.send("pong")

@bot.command()
async def suma(ctx, num1: int, num2: int):
    """..."""
    
    await ctx.send(num1 + num2)


@bot.command()
async def info(ctx):
    """..."""

    embed = discord.Embed(title=f"{ctx.guild.name}", description="BLABLABLA", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}") # NO FUNCIONAAAA

    await ctx.send(embed=embed)


@bot.command()
async def youtube(ctx, search):
    """..."""

    query_string = parse.urlencode({"search_query": search})
    html_content = request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall('watch\?v=(.{11})', html_content.read().decode('utf-8'))

    await ctx.send("https://www.youtube.com/watch?v=" + search_results[0])


# EVENTOS
@bot.event
async def on_ready():
    """..."""
    
    # await bot.change_presence(activity=discord.Streaming(name="Tutorials", url="https://www.twitch.tv/accountname"))
    print("My bot is ready")

bot.run('ODgyMjQyMDkyMDI0MzQwNTAx.YS4h-g.BDeP0aYu4kL1fubftT8KbCW6RtU')

# client = discord.Client()

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#     # if message.author == client.user:
#     #     return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

# client.run('ODgyMjQyMDkyMDI0MzQwNTAx.YS4h-g.BDeP0aYu4kL1fubftT8KbCW6RtU')