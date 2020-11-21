import discord
import datetime
from discord.ext import commands, tasks

class Daily_Inspiration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.first_loop.start() #initialises the very first_loop on loading

    def daily_quote(self):
        """sends out an inspirational quote every day"""
        with open('quote_list.txt', 'r') as reader:
            todays_quote = random.choice(reader.readlines())    #pulls a random line from the .txt doc
            print("Good morning, afternoon, evening and night! Today's inspiration: " + todays_quote)

    @tasks.loop(minutes=60)
    async def first_loop(self):
        """provides a med timer to a hard-coded release hour"""
        time = datetime.datetime.now()  #on the first run, checks the time every 1h
        release_hour = 7
        hour = time.strftime("%H")
        if int(hour) == release_hour:   #if the hour is 7am
            self.timer.start()  #start the rapid checking timer
            self.first_loop.stop()  #stop this one

    @tasks.loop(seconds=30)
    async def timer(self):
        """provides a short timer to a hard-coded release hour"""
        time = datetime.datetime.now() #checks the time every 30 seconds
        release_time = 8.0
        target = time.strftime("%H.%M")
        if float(target) > release_time:    #whoops, somehow you missed it
            self.daily_quote()  #post it anyway
            self.first_loop.start() #reset the timer with the first_loop
            self.timer.stop()
        if float(target) == release_time: #if the target time is reached
            self.daily_quote()  #send out the quote
            self.sleeper.start()    #move to the sleeper timer
            self.timer.stop()   #stop this timer

    @tasks.loop(hours=23, minutes=55)
    async def sleeper(self):
        """provides an almost day long sleeper timer to a hard-coded release time"""
        time = datetime.datetime.now() #wake up ad check the time after 23h, 55min
        release_time = 8.0
        target = time.strftime("%H.%M")
        if float(target) > release_time:    #if the target is more than the release time.
            self.daily_quote()  #whoops, missed it. Post the quote anyway.
            self.first_loop.start() #reset the timer with the first_loop
            self.sleeper.stop()
        elif float(target) <= release_time: #if it is getting close to the time
            self.timer.start() #start the shorter timer
            self.sleeper.stop() #stop this one

def setup(bot):
    bot.add_cog(Daily_Inspiration(bot))