TOKEN = 'OTk1ODc4MDQ2NjUxMzgzODg4.GqUDLK.gtid7DnsH5Qqt3_w6lN_3eKdfhfPijnyrMeNPc'
GUILD = 'Robin Personal Server'

import os
import discord


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild: \n'
        f'{guild.name}(id: {guild.id})'
        )


client.run(TOKEN)
