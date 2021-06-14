import discord
import os
from discord import activity
from discord import embeds
from discord.ext import commands, tasks
from itertools import cycle 
from discord import FFmpegPCMAudio, PCMVolumeTransformer
import random
import aiohttp
from dotenv import load_dotenv
from googleapiclient.discovery import build
client = commands.Bot(command_prefix = '>')




status = cycle(['>help','>happy','>server'])
extension = ['youtube','text','cogs','image']
players = { }
@client.event
async def on_ready():
    change_status.start()
    print('bot is ready.')

@tasks.loop(seconds=2)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)



@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Numbers of message need to delete')
@client.command()
async def knd(ctx):
    await ctx.send('First of all, Doãn Hải. Second of all, manipulative. Third of all, uncultured dad. Fourth of all, just wait one more year as you said. And most importantly, REMEMBER that faking post, REMEMBER THIS: :poop:') 
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

# @client.command()
# async def join(ctx):
#     channel = ctx.author.voice.channel
#     await channel.connect()
# @client.command(pass_context=True)
# async def leave(ctx):
#     await ctx.voice_client.disconnect()
# @client.command(pass_context=True)
# async def play(ctx, url):
#     server = ctx.message.server
#     voice_client = client.voice_client_in(server)
#     player = await voice_client.create_ytdl_player(url)
#     players[server.id] = player
#     player.start()

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# @client.command()
# async def ping(ctx):
#     await ctx.send(f'Pong! {round(client.latency * 1000)}ms')




client.run('ODUzMjk0MTY2MTA0NjA0NzMy.YMTSHg.wX29xwbdQG5MVmyI8NdWjwneoI8')
