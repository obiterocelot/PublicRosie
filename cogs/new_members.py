import random
from discord.ext import commands


class New_Members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """sends a welcome message in the channel when a new member joins"""
        system_channel = member.guild.system_channel
        with open('welcome_message.txt', 'r') as reader:
            welcome_message = random.choice(reader.readlines())
            response = welcome_message.format(member)
        await system_channel.send(response)  # sends a random welcome_greeting to the 'general' channel.

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server.')


def setup(bot):
    bot.add_cog(New_Members(bot))