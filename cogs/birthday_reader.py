import cleanup
import asyncio
import birthday_list
from discord.ext import commands


class Birthday(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.members = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        """Responds if the bot hears about someone's birthday"""
        channel = message.channel
        cleanmessage = cleanup.easyreader(message)
        new_message = " ".join(cleanmessage) # clean message so it could be searched with capitals etc
        ids = self.bot.user.id
        if "happy birthday" in new_message:
            user = message.mentions[0] # pulls the first user mention. Will break if there is more than one
            member = '#'.join((user.name, user.discriminator))
            if birthday_list.check_birthday(message.guild, member) == True:
                pass
            else:
                if message.mentions == []:
                    pass
                else:
                    await channel.send("Wait, is it {0}'s birthday?!".format(user.mention))

                def check(message):
                    cleanmessage = cleanup.easyreader(message)
                    return message.channel == channel and str(ids) in cleanmessage and "yes" in cleanmessage
                    # The about number is pulled as the bot's client id. Should work across all servers.

                try:
                    await self.bot.wait_for('message', timeout=60.0, check=check) # waits for response for 1 min
                except asyncio.TimeoutError:
                    await channel.send("Oh, I guess not.") # if it doesn't get the right response in time
                else:
                    await channel.send("Why didn't anyone tell me?! HAVE THE BEST OF BIRTHDAYS {0}!!".format(user.mention))
                    birthday_list.add_birthday(message.guild, member)


def setup(bot):
    bot.add_cog(Birthday(bot))