import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

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

@bot.command(name = 'pronouns')
async def setPronouns(ctx, arg):
    await ctx.send("You have been given the role!")
    pass

bot.run(os.getenv("DISCORD_TOKEN"))