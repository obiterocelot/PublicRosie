#quote_bot runs in parallel to most_basic_bot. Quote_bot is activated daily on the server by Heroku Scheduler which
#essentially acts as a server-specific cron job.

import discord
import os  # allows us to pull the discord token from the environment

from discord.ext import commands, tasks  # bot commands
from dotenv import load_dotenv  # loads environment variables from an .env file which we then pull with os

load_dotenv()   #necessary during local testing etc
TOKEN = os.getenv('DISCORD_TOKEN')  # produces our discord token so its hidden in the visible code

intents = discord.Intents.all()  # to use certain member tools (requires permission if bot on more than 10 servers)
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)  # ! is the standard
                                                         # intents needed for some member related commands/events


@bot.event
async def on_ready():
    """confirmation of bot joining and reminder of cog loaded"""
    print('We have logged in as {0.user}'.format(bot))  # prints below to confirm connection
    for filename in os.listdir('./cogs2'):   #put all cogs for this bot in ./cogs file
        if filename.endswith('.py'):
            bot.load_extension(f'cogs2.{filename[:-3]}')
            print(f'Cog loaded:{filename}')


bot.run(TOKEN)