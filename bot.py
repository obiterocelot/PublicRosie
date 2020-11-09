import discord
import os  # allows us to pull the discord token from the environment
import random

from discord.ext import commands  # bot commands
from dotenv import load_dotenv  # loads environment variables from an .env file which we then pull with os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  # produces our discord token so its hidden in the visible code

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents = intents)  # ! is the standard


@bot.event
async def on_member_join(member):
    print('new member detected')
    channel = discord.utils.get(member.guild.text_channels, name='general')
    welcome_greeting = ["Hey there {0.mention}. Fancy seeing you here.".format(member),
                        "Welcome to the Chaos {0.mention}! Have a biscuit.".format(member),
                        "{0.mention} is in the building! Who let you in here?".format(member),
                        "Ph'nglui mglw'nafh {0.mention} Chaos".format(member),
                        "Well, we've gone and done it now. {0.mention}'s awake.".format(member),
                        "WOO! {0.mention}! WOO!".format(member)
                        ]
    response = random.choice(welcome_greeting)
    await channel.send(response)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))  # prints below to confirm connection

##TO TEST!! Welcome Message##
bot.run(TOKEN)
