import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get

load_dotenv()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

@bot.command(name = 'hello')
async def hello(ctx):
    await ctx.send("What's up??")
    pass

@bot.command(name = 'whatdo')
async def help(ctx):
    await ctx.send("Here's the list of commands!")
    pass

@bot.command(name = 'setpronouns')
async def setPronouns(ctx, arg1):
    guild = ctx.guild
    user = ctx.message.author
    if get(ctx.guild.roles, name=arg1):
        role = discord.utils.get(ctx.guild.roles, name=arg1)
    else:
        await ctx.guild.create_role(name=arg1, colour=discord.Colour(0x0062ff))
        role = discord.utils.get(ctx.guild.roles, name=arg1)
    await user.add_roles(role)
    await ctx.send("You have been given the role {}!".format(arg1))
    pass

@bot.command(name = 'removepronouns')
async def removePronouns(ctx, arg1):
    guild = ctx.guild
    user = ctx.message.author
    if get(ctx.guild.roles, name=arg1):
        role = discord.utils.get(ctx.guild.roles, name=arg1)
        await user.remove_roles(role)
        await ctx.send("The {} role has been removed!".format(arg1))
    else:
        await ctx.send("You do not have the {} role!".format(arg1))
    pass

bot.run(os.getenv("DISCORD_TOKEN"))