import birthday_list

from discord.ext import commands

class Birthday_Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        """checks from a list whether it's someone's birthday and sends out a message if it is."""
        guild_list = self.bot.guilds    #pulls all guilds that the bot is a part of
        for guild in guild_list:
            birthdays = birthday_list.check_day(guild)
            system_channel = guild.system_channel  # find the system channel
            await system_channel.send("Happy birthday to {0}! I hope it's excellent!".format(birthdays))



def setup(bot):
    bot.add_cog(Birthday_Cog(bot))