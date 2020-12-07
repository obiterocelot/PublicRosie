import discord
import ast

def get_dict():
    with open('warnings.txt', 'r+') as f:
        data = f.read()
        fulldict = ast.literal_eval(data)
        return fulldict

def issue_warning(member):
    warnmember = '#'.join((member.name, member.discriminator))
    fulldict = get_dict()
    for entry in fulldict:
        if warnmember == entry:
            fulldict[entry] += 1
    if warnmember not in fulldict:
        fulldict[warnmember] = 1
    append_dict(fulldict)
    return fulldict

def append_dict(fulldict):
    with open('warnings.txt', 'r+') as f:
        f.truncate(0)
        f.seek(0)
        f.write(str(fulldict))

def check_timeout(member):
    fulldict = get_dict()
    search = '#'.join((member.name, member.discriminator))
    for entry in fulldict:
        if search == entry:
            if fulldict[entry] >= 3:
                return True
            else:
                return False

async def strike_reset(ctx, member):
    fulldict = get_dict()
    timeoutrole = discord.utils.get(ctx.guild.roles, name="Timeout")  # finds the id for the particular roles
    memberrole = discord.utils.get(ctx.guild.roles, name="Member")
    await member.remove_roles(timeoutrole)
    await member.add_roles(memberrole)
    search = '#'.join((member.name, member.discriminator))
    del fulldict[search]
    append_dict(fulldict)

async def strike_info(ctx):
    embedded_var = discord.Embed(title="Strike Report", description="List of all users with a strike", color=0x8b0c3c)
    with open('warnings.txt', 'r') as f:
        content = f.read()
        embedded_var.add_field(name="Users", value=content, inline=False)
        await ctx.channel.send(embed=embedded_var)
