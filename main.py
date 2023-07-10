import discord
# from discord import app_commands, Intents, Client, Interaction
from discord.ext import commands
from discord import app_commands
import random
import re
from dotenv import load_dotenv
import os
import requests
from pymongo import MongoClient
import asyncio
load_dotenv('.env')

cluster = MongoClient(os.getenv("CLOUD"))
base = cluster["OrionDB"]
ign_cur = base["ign"]

bot = commands.Bot(command_prefix=[".o ", ".O "], 
                   case_insensitive = True, 
                   intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is ready")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(f"Error syncing commands: {e}")

# load cogs
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.{filename[:-3]}")


@bot.tree.command(name= "8ball", description="Ask the magic 8ball a question")
async def _8ball(interaction:discord.Interaction, choice:str):
    responses = [
    "It is certain.", "It is decidedly so.", "Without a doubt.",
    "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
    "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
    "Reply hazy, try again.", "Ask again later.",
    "Better not tell you now.", "Cannot predict now.",
    "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
    "My sources say no.", "Outlook not so good.", "Very doubtful."]
    
    await interaction.response.send_message(random.choice(responses))


async def main():
    async with bot:
        await load_extensions()
        await bot.start(os.getenv("CURRENT_TOKEN"))

#this is a github test
#this is test 2
#this is test 3
asyncio.run(main())