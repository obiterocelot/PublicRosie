import discord
from time import sleep

def check_for_timeout_role(ctx):
    guild = ctx.guild
    roles = guild.roles
    name_list = []
    for each in roles:
        name_list.append(each.name)
        print(name_list)
    if "timeout" in name_list:
        print("There is already a role called Timeout")
    else:
        await create_timeout_role(guild)

def create_timeout_role(guild)
    permissions = discord.Permissions(permissions=1049600)
    await guild.create_role(name="timeout", colour=discord.Colour(0xffffff), permissions=permissions)

def time_out(ctx, member : discord.Member, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name="timeout")
    await member.add_roles(role)
    await alert_member(member, reason)
    sleep(30)
    await member.remove_roles(role)

def alert_member(member, reason)
    await member.send(f"You have been timed out for 30 seconds. Reason given: {reason}/n "
                      f"If you have any questions or difficulties, please contact a moderator")
