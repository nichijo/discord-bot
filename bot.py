# 
# VCに入ったら発言するボットくん
#


import discord
import os
import logging
from os.path import join, dirname
from dotenv import load_dotenv

# logging initialize
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# .env initialize
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# discord initialize
client = discord.Client()
send_channel = None

@client.event
async def on_ready():
    # 発言するチャンネルを設定するだけ
    global send_channel
    send_channel = client.get_channel(int(os.environ.get("DEFAULT_SEND_TEXT_CHANNEL")))

@client.event
async def on_voice_state_update(member, before, after):
    # チャンネルに入ったので発言する
    if (before.channel is None and after.channel is not None):
        await send_channel.send('📢' + member.display_name + 'が' + after.channel.name + 'に入室しました。')
    # チャンネルから出たので発言する
    if (before.channel is not None and after.channel is None):
        await send_channel.send('👋' + member.display_name + 'が' + before.channel.name + 'から退出しました。')

client.run(os.environ.get("TOKEN"))

