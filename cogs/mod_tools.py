import discord
from discord.ext import commands, tasks

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=2):
        """bulk clear command"""
        await ctx.channel.purge(limit=amount) #amount default 2 includes the !clear command and the message above it

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):  # asterix=all parameters after member and reason will just be added to reason
        """quick kick command with reasons"""
        await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):  # asterix=otherwise all spaces would be additional parameters
        """quick ban command with reasons"""
        await member.ban(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):  # don't convert to discord.Member as it isn't a server member, just a string
        """quick unban command with reasons"""
        banned_users = await ctx.guild.bans() #pulls ban list
        member_name, member_discriminator = member.split('#') #split the member name from the numerical discriminator
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                return

def setup(bot):
    bot.add_cog(Moderation(bot))