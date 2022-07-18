import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord')
    guild = discord.utils.get(bot.guilds, name=GUILD)
    members = '\n -'.join([member.name for member in guild.members])
    print(f'Guild Members: \n -{members}')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
            f'Hi {member.name}, welcome to my Discord server!'
        )

@bot.command(name='99', help='Gives a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),

        'I am bisexual',
        'This is a random chatbot, but I made it, so ya know, its cool',
        'You can hate people and still think they\'re hot'
    ]
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='members' , help='Gives a list of members in guild')
async def members(ctx):
    guild = discord.utils.get(bot.guilds, name=GUILD)
    members = '\n -'.join([member.name for member in guild.members])
    await ctx.send(f'Guild Members:\n -{members}')


bot.run(TOKEN)