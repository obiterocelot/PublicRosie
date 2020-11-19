import discord
from discord.ext import commands

channel_default = discord.utils.get(member.text_channels, name='general')

intents = discord.Intents.default()
intents.members = True

class Members():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joined(self, member : discord.Member):
        """sends a welcome message in the channel when a new member joins"""
        welcome_greeting = ["Hey there {0.mention}. Fancy seeing you here.".format(member),
                            "Welcome to the Chaos {0.mention}! Have a biscuit.".format(member),
                            "{0.mention} is in the building! Who let you in?".format(member),
                            "Ph'nglui mglw'nafh {0.mention} Chaos".format(member),
                            "Well, we've gone and done it now. {0.mention}'s awake.".format(member),
                            "WOO! {0.mention}! WOO!".format(member)
                            ]  # to add to
        response = random.choice(welcome_greeting)
        await self.bot.say(response)


def setup(bot):
    bot.add_cog(Members(bot))