import discord
from discord.ext import commands

class Emoji(commands.Cog):

    def __init__(self, client):
        self.cllient = client

    @commands.command()
    async def happy(self, ctx):
        await ctx.send('<:dango_thanks:841394207217811456>')
    @commands.command()
    async def server(self, ctx):
        await ctx.send('<:dango_sever:848567102997528636>')
    @commands.command()
    async def bonk(self, ctx):
        await ctx.send('<:dango_cry:848567383152263219>')
    
def setup(client):
    client.add_cog(Emoji(client))