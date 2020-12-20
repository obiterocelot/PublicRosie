import birthday_list
import daily_inspirations

from discord.ext import commands

class Announcement_Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        """checks from a list whether it's someone's birthday and sends out a message if it is."""
        guild_list = self.bot.guilds    #pulls all guilds that the bot is a part of
        for guild in guild_list:
            birthdays = birthday_list.check_day(guild)
            system_channel = guild.system_channel  # find the system channel
            quote = daily_inspirations.daily_inspiration()
            await system_channel.send("Today's announcements! \n \n Happy birthday to {0}! I hope it's excellent! \n \n "
                                      "Have an excellent day and don't forget: {1}".format(', '.join(birthdays), quote))
        await self.bot.close()  # once completed, close bot down.



def setup(bot):
    bot.add_cog(Announcement_Cog(bot))