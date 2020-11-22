import random
from discord.ext import commands

class Daily_Inspiration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        """sends out an inspirational quote every day"""
        guild_list = self.bot.guilds
        with open('quote_list.txt', 'r') as reader:
            todays_quote = random.choice(reader.readlines())  # pulls a random line from the .txt doc
        for guild in guild_list:
            system_channel = guild.system_channel
            await system_channel.send("Good, morning, afternoon, evening or night! Todays quote: " + todays_quote)
        await self.bot.close()


def setup(bot):
    bot.add_cog(Daily_Inspiration(bot))
