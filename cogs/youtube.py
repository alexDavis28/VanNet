import discord
from discord.ext import commands


class Youtube(commands.Cog):
    def __init__(self, client):
        self.client: commands.Bot = client
        self.config = client.config

    @commands.command()
    async def datto(self, ctx, *, search):
        search = "".join(["%20" if i==" " else i for i in search])
        await ctx.send(f"https://www.youtube.com/user/DattoDoesDestiny/search?query={search}")


def setup(client):
    client.add_cog(Youtube(client))
