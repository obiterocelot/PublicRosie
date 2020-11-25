import string
import timeout
from discord.ext import commands

class Auto_mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        message_content = str(message.content)
        message_lower = message_content.lower()
        cleanup = message_lower.translate(str.maketrans('', '', string.punctuation))
        list_message = cleanup.split()
        with open('bad_words.txt', 'r') as reader:
            bad_words = reader.read()
            banned_as_list = bad_words.split()
        for words in list_message:
            if words in banned_as_list:
                await message.delete()
                await timeout.time_out(member, ctx, reason="For using a banned word.")


def setup(bot):
    bot.add_cog(Auto_mod(bot))