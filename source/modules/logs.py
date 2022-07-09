import discord
from rich.console import Console
from datetime import datetime
import logging
import discord

logger = Console()

time = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
loggerds = logging.getLogger(f'discord')
loggerds.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=f'logs/discord{time}.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
loggerds.addHandler(handler)

def log(*txt, sep=' '):
    logger.print(datetime.now().strftime('%d.%m.%Y %H:%M:%S'), '> ', sep.join(map(str, txt)))
