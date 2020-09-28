import discord
import io
import aiohttp
import random
import time
from discord.ext import commands

class common(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(send_messages=True)
    async def bruh(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)
        time.sleep(0.5)
        await ctx.send('bruh moment')

    @commands.command()
    @commands.has_permissions(send_messages=True)
    async def bitchofeo(self, ctx, amount=1):
        responses = ['se mato por un bloque',
                     'Cabron es Brian el Imposter!1!1!!11!!!!!1!',
                     'me cago en dios',
                     'Despierto, Pensando en Burger King',
                     'papi no me digas eso no seas malo maricon :(',
                     'Luis Daniel 😳',
                     'Mano e que yediel',
                     'قد تحترق في الجحيم',
                     'hakai',
                     'https://www.youtube.com/watch?v=Le8CbESY5aI&ab_channel=RICKYDO%24%24A',
                     'Cancelaron a WAPA',
                     'Queee bochincheee',
                     'mi familia es cabron',
                     'yoxiel x RickyDo$$a - periodico de ayer remix con bambiel',
                     'bruh fart fart bruh fart bruh optimus prime bruh fart',
                     'Voy a cagar a las 4pm',
                     'se me fue el hotspot de open mobile',
                     '(Notices bulge), OwO I see you\'we h-happy too see me... haha. We\'ww say no mowe uwu (dick gurgling sounds)',
                     'Hayden moment',
                     'Te jodistes mano @Drift King',
                     'Fufu es el Espiritu Santo',
                     'llellellellellellellegamos pueblo de puerrrrrtoo rrriicoooooo',
                     'Este cabron vive en Moca',
                     'Time to call in the Big Chungus @Dian Carlos',
                     '😅 🤨 🧐']
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'{random.choice(responses)}')

    @commands.command()
    @commands.has_permissions(send_messages=True)
    async def pedro(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)
        time.sleep(0.3)
        await ctx.send('pedro julio serrano')

    @commands.command()
    @commands.has_permissions(send_messages=True)
    async def pog(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)
        time.sleep(0.3)
        await ctx.send('POG')

    @commands.command()
    @commands.has_permissions(send_messages=True)
    async def bigchungus(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)
        time.sleep(0.3)
        await ctx.send('big chongo')


def setup(client):
    client.add_cog(common(client))