'''
VCチャンネルを監視するプラグイン
'''
__all__=['VCWatchPluggin']

from os import environ
from typing import List

from discord.ext import commands
from plugin.extension import DiscordExtension
from plugin.config import cogs

from support.config import logger

logger.info('check vc_watch_plugin runnable')

class VCWatchPluggin(DiscordExtension):
    '''
    vcチャンネルを監視し、必要に応じてチャンネルに発言するプラグイン
    '''
    def __init__(self):
        self.bot = None
        self.send_channel = None

    def initialize(self, bot):
        logger.info('VCWatchPlugin setup run.')
        self.bot = bot
        bot.add_cog(self)

    @commands.Cog.listener()
    async def on_ready(self):
        # 発言するチャンネルを設定するだけ
        self.send_channel = self.bot.get_channel(int(environ.get("DEFAULT_SEND_TEXT_CHANNEL")))

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if self.send_channel is None:
            return  # 発言対象がない場合は静かに終えるのみ……
        # チャンネルに入ったので発言する
        if (before.channel is None and after.channel is not None):
            await self.send_channel.send('📢' + member.display_name + 'が' + after.channel.name + 'に入室しました。')
        # チャンネルから出たので発言する
        if (before.channel is not None and after.channel is None):
            await self.send_channel.send('👋' + member.display_name + 'が' + before.channel.name + 'から退出しました。')
    
    @commands.command()
    async def test(self, ctx):
        await ctx.send('Hello...')

cogs.append(VCWatchPluggin())