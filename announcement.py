import random
from discord.ext import commands

class Birthday_Checker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        """sends out an inspirational quote every day"""
        guild_list = self.bot.guilds    #pulls all guilds that the bot is a part of
        with open('quote_list.txt', 'r') as reader:
            todays_quote = random.choice(reader.readlines())  # pulls a random line from the .txt doc
        for guild in guild_list:    #for every guild that is in the list
            system_channel = guild.system_channel   #find the system channel
            await system_channel.send("Good, morning, afternoon, evening or night! And remember: " + todays_quote)
        await self.bot.close() #once completed, close bot down.


def setup(bot):
    bot.add_cog(Daily_Inspiration(bot))