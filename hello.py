import os
import random
import re

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())

isai = re.compile(r'\bia\b', re.IGNORECASE)
isnotpro = re.compile(r'\bmauvais|\bpas\b|\bhais\b|\bdeteste\b|\barrete\b', re.IGNORECASE)


async def changegrudges(culprit, message):
    #is going to have issues when used more than for demonstrations, it's just a proof of concept
    await grudges_book.edit(content=f'{grudges_book.content}\n{culprit} said "{message}"')
    

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for c in client.get_all_channels():
        if c.name == "book-of-grudges":
            global grudges_book
            grudges_book = None
            print("book channel found")
            async for m in c.history(limit=1, oldest_first=True):
                
                if (m.author.name == "Watchsquirrel"):
                    grudges_book = m
                    print("book found")
                    break
            if grudges_book == None:
                grudges_book = await c.send(content="list of grudges:")
            break
    

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
        await changegrudges(culprit=message.author, message=message.content)

@client.event
async def on_message_delete(message):

    if isai.search(message.content) and not isnotpro.search(message.content):
        await message.channel.send(message.author.mention + '[.](https://klipy.com/gifs/nodding-yes-6)', delete_after=5)

client.run(TOKEN)