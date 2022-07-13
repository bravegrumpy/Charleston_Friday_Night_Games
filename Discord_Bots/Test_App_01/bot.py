#TOKEN = 'OTk1ODc4MDQ2NjUxMzgzODg4.G-S78h.hvxtqCMrzWONnnI6pAhdcOrvl1gLP5b5mLjIvc'
#GUILD = 'Brave Grumpy Server'

# bot.py
import os
from pathlib import Path

import discord
import dotenv

from dotenv import load_dotenv


import random


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')
    guild = discord.utils.get(client.guilds, name=GUILD)

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
    # members = ["This is placehoder text. I want it to eventually show",
    # " the same `members` that is referenced on line 29"]

    # members = '\n -'.join([member.name for member in client.guilds.members])

    guild = discord.utils.get(client.guilds, name=GUILD)
    
    members = '\n -'.join([member.name for member in guild.members])
            
    if message.content == 'members!':
        await message.channel.send(
            f'Server Members: \n -{members}'
            )

client.run(TOKEN)
