# bot.py
import os

import discord
from dotenv import load_dotenv

import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild: \n'
        f'{guild.name}(id:{guild.id})'
    )
#Line 29 creates members. It is printed to console. I want this to be triggered by message in discord. 
    members = '\n -'.join([member.name for member in guild.members])
    print(f'Guild Members:\n -{members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
            f'Hi {member.name}, welcome to my Discord server!'
        )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),

        'I am bisexual',
        'This is a random chatbot, but I made it, so ya know, its cool'
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')

    ## Comment the below two lines and uncommen t line 66 to recreate my errors.
    members = ["This is placehoder text. I want it to eventually show",
    " the same `members` that is referenced on line 29"]

    # members = '\n -'.join([member.name for member in client.guilds.members])
    
    if message.content == 'members!':
        await message.channel.send(
            f'Server Members: n\ -{members}'
            )

print(TOKEN)
#client.run(TOKEN)
