
import os 
import discord 
import asyncio
from discord.ext import tasks, commands

token = 'YOUR TOKEN'
 
client = commands.Bot(command_prefix='')

@client.command(name='hello') 
async def _viva(ctx)
    await ctx.send('hello world')

if __name__ == '__main__' :
    client.run(token)
