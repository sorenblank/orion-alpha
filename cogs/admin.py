import discord
# from discord import app_commands, Intents, Client, Interaction
from discord.ext import commands
from discord import app_commands
# others
import random
import re
from pymongo import MongoClient


class Admin(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self._last_member = None
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("ADMIN is Loaded ...")
    
    # @commands.command(name = "syn", description="Kicks a user")
    # async def syn(self,ctx):
    #     fnt = await ctx.bot.tree.sync()
    #     await ctx.send(f"Synced {fnt} commands")
    
    @app_commands.command(name = "ping", description="Shows the bot's latency")
    async def ping(self, interaction:discord.Interaction):
        await interaction.response.send_message(f"Pong! {round(self.bot.latency * 1000,2)}ms")



async def setup(bot):
    await bot.add_cog(Admin(bot))