


@bot.event
async def called_once_a_day():
    message = channel_default.send("Hey")
    schedule.every().day.at("14:16").do(message)