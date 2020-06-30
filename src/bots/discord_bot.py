'''
discordBotの実装

各プラグインを突っ込んで、抽象が持つ同じメソッドをひたすら呼ぶだけ。
やりたい事が増えれば、抽象とここの実装が拡張される想定。
DiscordBotの機能をそこまで把握していないため、とりあえずの実装となる。
'''

import discord
from support.config import logger

class DiscordBot(discord.Client):

    def __init__(self, plugins):
        super().__init__()
        self.plugins = plugins

    async def on_ready(self):
        logger.info('on_ready')
        for p in self.plugins:
            await p.on_ready(self)

    async def on_voice_state_update(self, member, before, after):
        logger.info('on_voice_state_update')
        for p in self.plugins:
            await p.on_voice_state_update(self, member, before, after)
    