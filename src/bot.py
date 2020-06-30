''' 
VCに入ったら発言するボットくん
'''
import os
from bots import discord_bot
from plugin.config import plugins
from support.config import logger

try:
    # discord initialize
    token = os.environ.get("TOKEN")
    if token is None:
        logger.info(token + "is not defined.")
        raise Exception("トークンが未設定だよ")

    bot = discord_bot.DiscordBot(plugins)
    bot.run(token)
except() as ex:
    logger.exception(ex)