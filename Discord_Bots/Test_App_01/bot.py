# bot.py
import os

import discord

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

#TOKEN = os.environ['DISCORD_TOKEN']
#GUILD = os.environ['DISCORD_GUILD']

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
    if message.author == client.user: #preventing infinite feedback loop.
        return

    ## Below are some variables used within this method. 
    brooklyn_99_quotes = [ #list of brooklyn 99 quotes
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),

        'I am bisexual',
        'This is a random chatbot, but I made it, so ya know, its cool'
    ]
    
    guild = discord.utils.get(client.guilds, name=GUILD) # same code as seen in line 22.
    
    members = '\n -'.join([member.name for member in guild.members]) # same code as seen in line 29.

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    elif 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')
            
    elif (message.content == 'members!'):
        await message.channel.send(
            f'Server Members: \n -{members}'
            )
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

client.run(TOKEN)
