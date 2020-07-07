''' 
VCに入ったら発言するボットくん
'''
import os
from discord.ext.commands import Bot
from support.config import logger
from plugin import *

try:
    # discord initialize
    token = os.environ.get("TOKEN")
    if token is None:
        logger.info(token + "is not defined.")
        raise Exception("トークンが未設定だよ")

    baseBot = Bot(command_prefix = '$',description=None)

    logger.info("cog size :" + str(len(config.cogs)))

    for cog in config.cogs:
        logger.info(cog)
        cog.initialize(baseBot)

    logger.info("initialize setup.")
    baseBot.run(token)

except() as ex:
    logger.exception(ex)
