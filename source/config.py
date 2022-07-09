import discord
from dataclasses import dataclass

@dataclass
class NConf:
    prefix: str
    token: str
    description: str
    log_channels: list[int]
    status:discord.Activity
    guilds: list[int]

Config = NConf(
    prefix="ПРЕФИКС",
    token="ТОКЕН",
    description="ОПИСАНИЕ",
    log_channels=[АЙДИ],
    status=discord.Streaming(name='Twitch', url='https://www.twitch.tv/404/'),
    guilds=[АЙДИ]
)
