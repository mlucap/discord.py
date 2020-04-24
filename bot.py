import discord
from discord.ext import commands, tasks
from discord.utils import get
import youtube_dl
import os
import time
from itertools import cycle


client = commands.Bot(command_prefix='.')
status = cycle(['Created by Coffii', '.help'])


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('.help'))
    change_status.start()
    print('Logged in.')


@client.command()
async def ping(ctx):
    await ctx.send(f"Latency is `{round(client.latency * 1000)}ms`")


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    """Clears messages. Default Value is 5. Requires permission manage_messages"""
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Cleared {amount} messages')
    time.sleep(5)
    await ctx.channel.purge(limit=1)


@clear.error
async def no_perms(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('`You are missing permissions to run this command. Please see .help clear`')


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


client.run('MzU2MTA5NTAwNDEyODU0Mjc1.XqMong.-J6RqE9hwJ1T6FNdKOCSUVOQM3k')