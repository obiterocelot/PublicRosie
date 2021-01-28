from discord.ext import commands

class Heart_Reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def new_react(self, reaction):
        await reaction.message.add_reaction(reaction.emoji)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        potential_emojis = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "🤎", "🤍", "💖", "💗"]
        if reaction.emoji in potential_emojis:
            await reaction.message.add_reaction(reaction.emoji)


def setup(bot):
    bot.add_cog(Heart_Reaction(bot))