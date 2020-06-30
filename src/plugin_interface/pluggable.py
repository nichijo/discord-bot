'''
プラグイン使用の共通インターフェース
'''

from abc import (
    ABC,
    abstractmethod
)

class Pluggable(ABC):
    '''
    プラグインが継承すべインターフェース
    '''

    @abstractmethod
    async def on_ready(self, bot):
        pass

    @abstractmethod
    async def on_voice_state_update(self, bot, member, before, after):
        pass