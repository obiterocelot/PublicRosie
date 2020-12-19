import random


def daily_inspiration():
    """sends out an inspirational quote every day"""
    with open('../quote_list.txt', 'r') as reader:
        todays_quote = random.choice(reader.readlines())  # pulls a random line from the .txt doc
        return todays_quote

