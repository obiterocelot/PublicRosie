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


def setup(bot):
    bot.add_cog(Message_Reader(bot))