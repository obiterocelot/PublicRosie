import discord
import random
from discord.ext import commands


class New_Members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """sends a welcome message in the channel when a new member joins"""
        system_channel = member.guild.system_channel
        welcome_greeting = ["Hey there {0.mention}. Fancy seeing you here.".format(member),
                            "Welcome to the Chaos {0.mention}! Have a biscuit.".format(member),
                            "{0.mention} is in the building! Who let you in?".format(member),
                            "Ph'nglui mglw'nafh {0.mention} Chaos".format(member),
                            "Well, we've gone and done it now. {0.mention}'s awake.".format(member),
                            "WOO! {0.mention}! WOO!".format(member)
                            ]  # to add to
        response = random.choice(welcome_greeting)
        await system_channel.send(response)  # sends a random welcome_greeting to the 'general' channel.

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server.')


def setup(bot):
    bot.add_cog(New_Members(bot))