import ast
from discord.ext import commands

class Announcement_Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        """checks from a list whether it's someone's birthday and sends out a message if it is."""
        guild_list = self.bot.guilds    #pulls all guilds that the bot is a part of
        with open('birthday_list.txt', 'r') as reader:
            for guild in guild_list:    #for every guild that is in the list
                system_channel = guild.system_channel   #find the system channel
                await system_channel.send("Good, morning, afternoon, evening or night! And remember: " + todays_quote)
        await self.bot.close() #once completed, close bot down.


def setup(bot):
    bot.add_cog(Daily_Inspiration(bot))