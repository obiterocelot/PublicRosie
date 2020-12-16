import discord
import random
from discord.ext import commands


class New_Members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def check_for_role(self, member):
        """double check to see if a member role has already been created"""
        guild = member.guild
        roles = guild.roles
        name_list = []
        for each in roles:
            name_list.append(each.name) # pull all roles into a name list for searching.
        if "Member" in name_list:
            pass    # ignore if the name is already in the list.
        else:
            await self.create_member_role(guild)    # else, create it.

    async def create_member_role(self, guild):
        """specific permissions for member role"""
        permissions = discord.Permissions(permissions=104287808)    # permissions number taken from an online calculator.
        await guild.create_role(name="Member", colour=discord.Colour(0x318ad1), permissions=permissions)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """assigns new member their role and sends a welcome message in the channel when a new member joins"""
        await self.check_for_role(member)
        guild = member.guild
        memberrole = discord.utils.get(guild.roles, name="Member")
        await member.add_roles(memberrole)

        system_channel = member.guild.system_channel
        with open('welcome_message.txt', 'r') as reader:
            welcome_message = random.choice(reader.readlines())
            response = welcome_message.format(member)
        await system_channel.send(response)  # sends a random welcome_greeting to the 'general' channel.

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        """advises in the server that someone has left."""
        print(f'{member} has left a server.')


def setup(bot):
    bot.add_cog(New_Members(bot))