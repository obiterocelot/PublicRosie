import discord
import datetime
from discord.ext import commands, tasks

class Daily_Inspiration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.first_loop.start()

    def daily_quote(self):
        with open('quote_list.txt', 'r') as reader:
            todays_quote = random.choice(reader.readlines())
            print("Today's inspiration: " + todays_quote)

    @tasks.loop(minutes=60)
    async def first_loop(self):
        time = datetime.datetime.now()
        release_hour = 7
        hour = time.strftime("%H")
        if int(hour) == release_hour:
            self.timer.start()
            self.first_loop.stop()

    @tasks.loop(seconds=10)
    async def timer(self):
        time = datetime.datetime.now()
        release_time = 0
        minute = time.strftime("%M")
        if int(minute) == release_time:
            self.daily_quote()
            self.sleeper.start()
            self.timer.stop()

    @tasks.loop(hours=23, minutes=55)
    async def sleeper(self):
        time = datetime.datetime.now()
        release_time = 8.0
        target = time.strftime("%H.%M")
        if float(target) > release_time:
            self.daily_quote()
        elif float(target) <= release_time:
            self.timer.start()
            self.sleeper.stop()

def setup(bot):
    bot.add_cog(Daily_Inspiration(bot))