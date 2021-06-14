import discord
from discord.ext import commands

class Emoji(commands.Cog):

    def __init__(self, client):
        self.cllient = client
    @commands.command()
    async def ping_ping_ping(self, ctx):
        await ctx.send('pong pong pong')

def setup(client):
    client.add_cog(Emoji(client))
