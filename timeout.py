import discord
import strikes
from asyncio import sleep


async def check_for_timeout_role(ctx):
    """checks for existence of timeout role and makes one if it isn't there"""
    guild = ctx.guild
    roles = guild.roles
    name_list = []
    for each in roles:
        name_list.append(each.name) #creates a list of role names in the guild
    if "Timeout" in name_list:
        pass    #if there is one called Timeout, never mind
    else:
        await create_timeout_role(guild) #if there isn't, create the role


async def create_timeout_role(guild):
    """creation of the timeout role"""
    permissions = discord.Permissions(permissions=1049600) #there is a discord calculator to get this number
                                                           #https://discordapi.com/permissions.html#0
    await guild.create_role(name="Timeout", colour=discord.Colour(0xff0000), permissions=permissions)


async def time_out(member : discord.Member, ctx, reason):
    """timeout for 30 secs"""
    timeoutrole = discord.utils.get(ctx.guild.roles, name="Timeout") #finds the id for the particular roles
    memberrole = discord.utils.get(ctx.guild.roles, name="Member")
    await member.add_roles(timeoutrole) #switch the Member role for the Timeout role
    await member.remove_roles(memberrole)
    await alert_member(member, reason) #sends a DM to the member you timedout
    await sleep(30) #asyncio.sleep
    await member.remove_roles(timeoutrole) #switches back after 30 sec
    await member.add_roles(memberrole)


async def alert_member(member, reason):
    """DMs member to alert them to their timeout"""
    await member.send(f"You have been timed out for 30 seconds. Reason given: {reason} \n"
                      f"If you have any questions or difficulties, please contact a moderator")

async def perma_timeout(member : discord.Member, ctx):
    """longterm timeout if strikes are above 3. Can be removed and reset by a mod"""
    timeoutrole = discord.utils.get(ctx.guild.roles, name="Timeout")  # finds the id for the particular roles
    memberrole = discord.utils.get(ctx.guild.roles, name="Member")
    await member.add_roles(timeoutrole)  # switch the Member role for the Timeout role
    await member.remove_roles(memberrole)
    await member.send(f"Due to continuous misbehaviour, you are under suspension until a moderator reviews your case. If you have any questions, please contact a moderator.")

async def timeoutprocess(ctx, member, reason):
    """calls the entire timeout process in order. Elements can also be called seperately"""
    await check_for_timeout_role(ctx)
    strikes.issue_warning(member)
    timeout_type = strikes.check_timeout(member)
    if timeout_type == True:
        await perma_timeout(member, ctx)
    if timeout_type == False:
        await time_out(member, ctx, reason)