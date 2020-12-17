import os
import shutil

from discord.ext import commands

class New_Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        fileDir = os.path.dirname(os.path.abspath(__file__))  # Directory of the Module
        parentDir = os.path.dirname(fileDir)  # Directory of the Module directory
        newPath = os.path.join(parentDir, "GuildDirectories/", str(guild.id))  # Get the directory for StringFunctions

        os.mkdir(newPath)

        with open(os.path.join(newPath, 'birthday_list.txt'), 'w') as file:
            file.write('{}')

        with open(os.path.join(newPath, 'strikes.txt'), 'w') as file:
            file.write('{}')

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        fileDir = os.path.dirname(os.path.abspath(__file__))  # Directory of the Module
        parentDir = os.path.dirname(fileDir)  # Directory of the Module directory
        newPath = os.path.join(parentDir, "GuildDirectories/", str(guild.id))

        try:
            shutil.rmtree(newPath)
        except OSError as e:
            print("Error: %s : %s" % (dir_path, e.strerror))


def setup(bot):
    bot.add_cog(New_Server(bot))