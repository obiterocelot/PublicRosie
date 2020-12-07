import cleanup
import timeout
from discord.ext import commands


class Auto_mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        """checks messages for banned_words. If word is found, issues a timeout."""
        list_message = cleanup.easyreader(message)
        with open('bad_words.txt', 'r') as reader:
            bad_words = reader.read()
            banned_as_list = bad_words.split()  #Second module checking for banned words. To look at regular expressions
        for words in list_message:
            if words in banned_as_list:
                await timeout.timeoutprocess(ctx, message.author, reason=None)
                #issues time out - cannot interact with discord except to read/hear for 30sec. DM sent to inform.


def setup(bot):
    bot.add_cog(Auto_mod(bot))