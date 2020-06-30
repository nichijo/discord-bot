'''
.env読み取り処理
'''

from os.path import join, dirname
from dotenv import load_dotenv

# .env initialize
load_dotenv(verbose=True)
load_dotenv(join(dirname(__file__), '.env'))