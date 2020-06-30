'''
VCチャンネルを監視するプラグイン
'''

from os import environ

from plugin_interface.pluggable import Pluggable
from plugin.config import plugins
from support.config import logger

class VCWatchPluggin(Pluggable):
    '''
    vcチャンネルを監視し、必要に応じてチャンネルに発言するプラグイン
    '''

    def __init__(self):
        self.send_channel = None

    async def on_ready(self, bot):
        # 発言するチャンネルを設定するだけ
        self.send_channel = bot.get_channel(int(environ.get("DEFAULT_SEND_TEXT_CHANNEL")))

    async def on_voice_state_update(self, bot, member, before, after):
        if self.send_channel is None:
            return  # 発言対象がない場合は静かに終えるのみ……
        # チャンネルに入ったので発言する
        if (before.channel is None and after.channel is not None):
            await self.send_channel.send('📢' + member.display_name + 'が' + after.channel.name + 'に入室しました。')
        # チャンネルから出たので発言する
        if (before.channel is not None and after.channel is None):
            await self.send_channel.send('👋' + member.display_name + 'が' + before.channel.name + 'から退出しました。')

plugins.append(VCWatchPluggin())
logger.info('VCWatchPlugin_initialized')