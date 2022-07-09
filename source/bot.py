import os
import discord
from discord.ext import commands
from config import Config

client = commands.Bot(
    command_prefix=Config.prefix,
    help_command=None,
    description=Config.description,
    intents=discord.Intents.all(),
    owner_id=763432000463306773
)

for f in os.listdir("./cogs"):
	if f.endswith(".py"):
		client.load_extension("cogs." + f[:-3])

client.run(Config.token)
