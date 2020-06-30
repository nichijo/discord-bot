'''
ロガーの定義とconfigへのロガー提供
'''

import logging
from logging import config as log_conf
import yaml
from support import config as sup_conf

log_conf.dictConfig(yaml.safe_load(open('./logging.yaml').read()))
sup_conf.logger = logging.getLogger('default')
sup_conf.logger.info("logger initialize finished.")