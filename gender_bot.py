import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get


load_dotenv()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents = intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

@bot.event
async def on_member_join(member):
    await member.send("Welcome to TrueColors!")
    role = discord.utils.get(member.guild.roles, name = 'NonMember')
    await member.add_roles(role)

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

@bot.command(name = "react")
async def reactionRole(ctx, arg1):
    message = await ctx.send('React to this message with a thumbs up to recieve the {} role!'.format(arg1))

    thumb_up = '👍'
    thumb_down = '👎'

    await message.add_reaction(thumb_up)
    await message.add_reaction(thumb_down)

    def check(reaction, user):
        return user == ctx.author and str(
            reaction.emoji) in [thumb_up, thumb_down]

    member = ctx.author

    while True:
        try:
            reaction, user = await client.wait_for("on_reaction_add", timeout=10.0, check=check)
            if str(reaction.emoji) == thumb_up:
                await ctx.send('You have been given the member role!')

            if str(reaction.emoji) == thumb_down:
                await ctx.send('The member role has been removed.')
        except:
            return
    pass

@bot.command(name = 'reactionrole')
async def reactionRole(ctx, arg1, arg2):
    # First arg is role name
    # Second arg is a message ID
    message = await ctx.fetch_message(arg2)
    role = discord.utils.get(ctx.guild.roles, name=arg1)
    await message.add_reaction('\N{THUMBS UP SIGN}')
    pass

bot.run(os.getenv("DISCORD_TOKEN"))