import discord
from discord.ext import commands
import asyncio
from util import ishtar

keys = ["◀️", "▶️"]


class Lore(commands.Cog):
    def __init__(self, client):
        self.client: commands.Bot = client
        self.config = client.config

    @commands.command(aliases=["ishtar"])
    async def lore(self, ctx, *, term):
        # await ctx.send(ishtar.search(term))
        data: dict = ishtar.search(term)

        if data == {}:
            await ctx.send("No results found")
            return

        pages = []

        # e = discord.Embed(title="Ishtar search results")
        for x, y in data.items():
            e = discord.Embed(title=f"Ishtar search result - {x}")
            entry = y[0]
            e.description = entry[0]
            e.url = entry[1]
            pages.append(e)

        page_counter = 0
        message: discord.Message = await ctx.send(embed=pages[page_counter])

        for i in keys:
            await message.add_reaction(i)

        def check(reaction, user):
            return user == ctx.author and (str(reaction.emoji) in keys)

        while True:
            try:
                response_reaction, user = await self.client.wait_for("reaction_add", timeout=10.0, check=check)

            except asyncio.TimeoutError:
                await message.clear_reactions()
                break

            if str(response_reaction) == keys[0]:
                page_counter -= 1
                page_counter = page_counter % len(pages)
                await message.edit(embed=pages[page_counter])
                await message.remove_reaction(response_reaction, user)

            elif str(response_reaction) == keys[1]:
                page_counter += 1
                page_counter = page_counter % len(pages)
                await message.edit(embed=pages[page_counter])
                await message.remove_reaction(response_reaction, user)

            else:
                pass


def setup(client):
    client.add_cog(Lore(client))
