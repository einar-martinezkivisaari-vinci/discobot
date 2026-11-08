import os
import random
import re

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())

isai = re.compile(r'\bia\b|\bai\b', re.IGNORECASE)
isnotpro = re.compile(r'\bmauvais|\bpas\b|\bhais\b|\bdeteste\b', re.IGNORECASE)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if isai.search(message.content):
        if isnotpro.search(message.content):
            #https://www.unicode.org/emoji/charts/full-emoji-list.html
            await message.add_reaction('\U0001faf6')
            return
        await message.reply('https://tenor.com/view/bunny-rabbit-angry-pistol-pistol-gun-gif-17001523090508176980', delete_after=5)
        await message.add_reaction('\U0001F52B')

@client.event
async def on_message_delete(message):

    if isai.search(message.content) and not isnotpro.search(message.content):
        await message.channel.send(message.author.mention + '[.](https://klipy.com/gifs/nodding-yes-6)', delete_after=5)

client.run(TOKEN)