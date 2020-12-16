import cleanup
import asyncio
from discord.ext import commands


class Message_Reader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.members = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        member = message.author
        search = '#'.join((member.name, member.discriminator))
        channel = message.channel
        if search not in self.members:
            self.members[search] = 0
        else:
            pass

        if self.members[search] == 0:
            cleanmessage = cleanup.easyreader(message)
            if "lana" in cleanmessage:
                self.members[search] = 1

        def check(message):
            cleanmessage = cleanup.easyreader(message)
            return "lana" in cleanmessage and message.channel == channel

        try:
            await self.bot.wait_for('message', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            self.members[search] = 0
        else:

            if self.members[search] == 1:
                cleanmessage = cleanup.easyreader(message)
                if "lana" in cleanmessage:
                    self.members[search] = 2
                    await channel.send("...")

            elif self.members[search] == 2:
                cleanmessage = cleanup.easyreader(message)
                if "lana" in cleanmessage:
                    self.members[search] = 0
                    await channel.send("WHAT!?")

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        cleanmessage = cleanup.easyreader(message)
        new_message = " ".join(cleanmessage)
        bot = self.bot
        if "happy birthday" in new_message:
            user = message.mentions[0]
            await channel.send("Wait, is it {0}'s birthday?!".format(user.mention))

            def check(message):
                cleanmessage = cleanup.easyreader(message)
                return message.channel == channel and "775418160290856972" in cleanmessage and "yes" in cleanmessage

            try:
                await bot.wait_for('message', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await channel.send("Oh, I guess not.")
            else:
                await channel.send("Why didn't anyone tell me?! HAVE THE BEST OF BIRTHDAYS {0}!!".format(user.mention))


def setup(bot):
    bot.add_cog(Message_Reader(bot))