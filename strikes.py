import discord
import ast
import os

def get_path(member):
    guild = member.guild
    fileDir = os.path.dirname(os.path.abspath(__file__))  # Directory of the Module
    newPath = os.path.join(fileDir, "GuildDirectories", str(guild.id), "strikes.txt")
    return newPath

def get_dict(member):
    """pulls dictionary from text document and turns it into a readable dictionary in programme"""
    newPath = get_path(member)
    with open(newPath, 'r+') as f:
        data = f.read()
        fulldict = ast.literal_eval(data) # pulling the text in the document as a dictionary
        return fulldict

def issue_warning(member):
    """increases the strike number"""
    warnmember = '#'.join((member.name, member.discriminator))
    fulldict = get_dict(member)
    for entry in fulldict: # searches dictionary for member. If they're there, increases their number.
        if warnmember == entry:
            fulldict[entry] += 1
    if warnmember not in fulldict:
        fulldict[warnmember] = 1 # if not, appends them to dictionary and sets their number as 1
    append_dict(fulldict, member) # rewrites the dictionary to the file
    return fulldict

def append_dict(fulldict, member):
    """rewrites the dictionary if there are any changes"""
    newPath = get_path(member)
    with open(newPath, 'r+') as f:
        f.truncate(0)
        f.seek(0)
        f.write(str(fulldict))

def check_timeout(member):
    """returns a boolean value whether they should be timed out"""
    fulldict = get_dict(member)
    search = '#'.join((member.name, member.discriminator))
    for entry in fulldict:
        if search == entry:
            if fulldict[entry] >= 3: # returns true if their strike counter is over 3
                return True
            else:
                return False

async def strike_reset(ctx, member):
    """resets the strike count and reverts the timeout role"""
    fulldict = get_dict(member)
    timeoutrole = discord.utils.get(ctx.guild.roles, name="Timeout")  # finds the id for the particular roles
    memberrole = discord.utils.get(ctx.guild.roles, name="Member")
    await member.remove_roles(timeoutrole)
    await member.add_roles(memberrole) # flicks them back to a member role
    search = '#'.join((member.name, member.discriminator))
    del fulldict[search]
    append_dict(fulldict, member)

async def strike_info(ctx):
    """sets up a Strike Report embedded message. Can be called by a mod command"""
    newPath = get_dict(ctx)
    embedded_var = discord.Embed(title="Strike Report", description="List of all users with a strike", color=0x8b0c3c)
    with open(newPath, 'r') as f:
        content = f.read()
        embedded_var.add_field(name="Users", value=content, inline=False) # turns it into an embedded message
        await ctx.channel.send(embed=embedded_var)