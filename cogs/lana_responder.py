import cleanup
import asyncio
from discord.ext import commands


class Lana_Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.members = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        """respond if you're getting pinged with Lana messages"""
        member = message.author
        search = '#'.join((member.name, member.discriminator)) # searches the member name
        channel = message.channel
        if search not in self.members:
            self.members[search] = 0    # creates a little dictionary to act as a counter
        else:
            pass

        if self.members[search] == 0:   # if the counter is at the start
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

            if self.members[search] == 1: # after the first message
                cleanmessage = cleanup.easyreader(message)
                if "lana" in cleanmessage:
                    self.members[search] = 2
                    await channel.send("...")

            elif self.members[search] == 2: # after the second message
                cleanmessage = cleanup.easyreader(message)
                if "lana" in cleanmessage:
                    self.members[search] = 0
                    await channel.send("WHAT!?")

def setup(bot):
    bot.add_cog(Lana_Bot(bot))