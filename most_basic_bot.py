## a lot of help from https://www.youtube.com/channel/UCR-zOCvDCayyYy1flR5qaAg

import discord
import os  # allows us to pull the discord token from the environment

from discord.ext import commands, tasks  # bot commands
from dotenv import load_dotenv  # loads environment variables from an .env file which we then pull with os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  # produces our discord token so its hidden in the visible code

intents = discord.Intents.all()  # to use certain member tools (requires permission if bot on more than 10 servers)
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)  # ! is the standard


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))  # prints below to confirm connection
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Cog loaded:{filename}')


bot.run(TOKEN)
