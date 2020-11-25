import discord
from time import sleep

async def check_for_timeout_role(ctx):
    guild = ctx.guild
    roles = guild.roles
    name_list = []
    for each in roles:
        name_list.append(each.name)
    if "Timeout" in name_list:
        pass
    else:
        await create_timeout_role(guild)

async def create_timeout_role(guild):
    permissions = discord.Permissions(permissions=1049600)
    await guild.create_role(name="Timeout", colour=discord.Colour(0xff0000), permissions=permissions)

async def time_out(member : discord.Member, ctx, *, reason=None):
    timeoutrole = discord.utils.get(ctx.guild.roles, name="Timeout")
    memberrole = discord.utils.get(ctx.guild.roles, name="Member")
    await member.add_roles(timeoutrole)
    await member.remove_roles(memberrole)
    await alert_member(member, reason)
    sleep(30)
    await member.remove_roles(timeoutrole)
    await member.add_roles(memberrole)

async def alert_member(member, reason):
    await member.send(f"You have been timed out for 30 seconds. Reason given: {reason} \n"
                      f"If you have any questions or difficulties, please contact a moderator")
