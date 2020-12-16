import discord
import ast

def get_dict():
    """pulls dictionary from text document and turns it into a readable dictionary in programme"""
    with open('warnings.txt', 'r+') as f:
        data = f.read()
        fulldict = ast.literal_eval(data) # pulling the text in the document as a dictionary
        return fulldict

def issue_warning(member):
    """increases the strike number"""
    warnmember = '#'.join((member.name, member.discriminator))
    fulldict = get_dict()
    for entry in fulldict: # searches dictionary for member. If they're there, increases their number.
        if warnmember == entry:
            fulldict[entry] += 1
    if warnmember not in fulldict:
        fulldict[warnmember] = 1 # if not, appends them to dictionary and sets their number as 1
    append_dict(fulldict) # rewrites the dictionary to the file
    return fulldict

def append_dict(fulldict):
    """rewrites the dictionary if there are any changes"""
    with open('warnings.txt', 'r+') as f:
        f.truncate(0)
        f.seek(0)
        f.write(str(fulldict))

def check_timeout(member):
    """returns a boolean value whether they should be timed out"""
    fulldict = get_dict()
    search = '#'.join((member.name, member.discriminator))
    for entry in fulldict:
        if search == entry:
            if fulldict[entry] >= 3: # returns true if their strike counter is over 3
                return True
            else:
                return False

async def strike_reset(ctx, member):
    """resets the strike count and reverts the timeout role"""
    fulldict = get_dict()
    timeoutrole = discord.utils.get(ctx.guild.roles, name="Timeout")  # finds the id for the particular roles
    memberrole = discord.utils.get(ctx.guild.roles, name="Member")
    await member.remove_roles(timeoutrole)
    await member.add_roles(memberrole) # flicks them back to a member role
    search = '#'.join((member.name, member.discriminator))
    del fulldict[search]
    append_dict(fulldict)

async def strike_info(ctx):
    """sets up a Strike Report embedded message. Can be called by a mod command"""
    embedded_var = discord.Embed(title="Strike Report", description="List of all users with a strike", color=0x8b0c3c)
    with open('warnings.txt', 'r') as f:
        content = f.read()
        embedded_var.add_field(name="Users", value=content, inline=False) # turns it into an embedded message
        await ctx.channel.send(embed=embedded_var)