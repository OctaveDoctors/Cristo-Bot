import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')
statuses = cycle(['Escuchando Emmanuel el album por Aries', 'Meando', "Cagando","Haciendome una paja","Big Chungus","Luis Daniel,"
                  "Cabron", "Kenny es pato"])

@client.command()
@commands.has_permissions(administrator=True)
async def bitcho_load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.has_permissions(administrator=True)
async def bitcho_unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
@commands.has_permissions(administrator=True)
async def bitcho_reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')

@tasks.loop(minutes=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(statuses)))

@client.command()
async def bitcho_ping(ctx, amount=1):
    await ctx.send(f'Toma cabron, {round(client.latency * 1000)}ms')
    await ctx.channel.purge(limit=amount)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')




client.run('NzU3MDI0Njg5OTkzNDE2NzA1.X2aYLg.I9pSkbk8V54TW1XdBs0Yd82Re2c')
