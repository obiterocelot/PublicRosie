import discord
import random
from discord.ext import commands


intents = discord.Intents.default()  # to use certain member tools (requires permission if bot on more than 10 servers)
intents.members = True


class New_Members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print("hi")
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """sends a welcome message in the channel when a new member joins"""
        channel_default = member.guild.system_channel
        print(channel_default)
        welcome_greeting = ["Hey there {0.mention}. Fancy seeing you here.".format(member),
                            "Welcome to the Chaos {0.mention}! Have a biscuit.".format(member),
                            "{0.mention} is in the building! Who let you in?".format(member),
                            "Ph'nglui mglw'nafh {0.mention} Chaos".format(member),
                            "Well, we've gone and done it now. {0.mention}'s awake.".format(member),
                            "WOO! {0.mention}! WOO!".format(member)
                            ]  # to add to
        response = random.choice(welcome_greeting)
        if channel_default is not None:
            await channel_default.send(response)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server.')


def setup(bot):
    bot.add_cog(New_Members(bot))