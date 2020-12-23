import ast
import os
from datetime import date
import discord

def get_path(guild):
    fileDir = os.path.dirname(os.path.abspath(__file__))  # Directory of the Module
    newPath = os.path.join(fileDir, "GuildDirectories", str(guild.id), "birthday_list.txt")
    return newPath

def get_dict(guild):
    """pulls dictionary from text document and turns it into a readable dictionary in programme"""
    newPath = get_path(guild)
    with open(newPath, 'r+') as f:
        data = f.read()
        fulldict = ast.literal_eval(data) # pulling the text in the document as a dictionary
        return fulldict

def append_dict(guild, fulldict):
    """rewrites the dictionary if there are any changes"""
    newPath = get_path(guild)
    with open(newPath, 'r+') as f:
        f.truncate(0)
        f.seek(0)
        f.write(str(fulldict))

def add_birthday(guild, member):
    """adds the birthday to the dictionary with today's date"""
    bdaymember = member
    fulldict = get_dict(guild)
    today = date.today()
    if bdaymember not in fulldict:
        fulldict[bdaymember] = today.strftime("%d/%m/%y") # if not, appends them to dictionary and sets their number as 1
    append_dict(guild, fulldict) # rewrites the dictionary to the file

def check_birthday(guild, member):
    fulldict = get_dict(guild)
    if member in fulldict:
        return True
    else:
        return False

def check_day(guild):
    fulldict = get_dict(guild)
    today = date.today()
    todaysdate = today.strftime("%d/%m/%y")
    birthdays = []
    for name, bday in fulldict.items():
        if bday == todaysdate:
            birthdays.append(name)
    return birthdays

async def birthday_info(ctx):
    """sets up a Birthday List embedded message. Can be called by a mod command"""
    guild = ctx.guild
    newPath = get_path(guild)
    embedded_var = discord.Embed(title="Birthday List", description="List of User's Birthdays", color=0x8b0c3c)
    with open(newPath, 'r') as f:
        content = f.read()
        embedded_var.add_field(name="Users", value=content, inline=False) # turns it into an embedded message
        await ctx.channel.send(embed=embedded_var)

async def birthday_del(ctx, member):
    """resets the strike count and reverts the timeout role"""
    guild = ctx.guild
    fulldict = get_dict(guild)
    search = '#'.join((member.name, member.discriminator))
    del fulldict[search]
    append_dict(guild, fulldict)