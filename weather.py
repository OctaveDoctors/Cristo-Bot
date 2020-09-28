import discord
import io
import aiohttp
import time
from discord.ext import commands

class weather(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    @commands.has_permissions(send_messages=True)
    async def radar(self,ctx,amount=1):
        await ctx.channel.purge(limit=amount)
        time.sleep(0.3)
        async with aiohttp.ClientSession() as session:
            async with session.get("https://radar.weather.gov/lite/N0R/JUA_0.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'JUA_0.png'))

    @commands.command()
    @commands.has_permissions(send_messages=True)
    async def outlook(self,ctx,amount=1):
        await ctx.channel.purge(limit=amount)
        time.sleep(0.3)
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.nhc.noaa.gov/xgtwo/two_atl_5d0.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'two_atl_5d0.png'))


def setup(client):
    client.add_cog(weather(client))
