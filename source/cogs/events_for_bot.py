import discord
from discord.ext import commands
from io import StringIO
from sys import path
path.insert(1, "../")
from modules.embed import embedGenerator
from config import Config
from modules.logs import log

class BOT_EVENTS(commands.Cog):
	def __init__(self, client):
		self.client:discord.Client = client # sets the client variable so we can use it in cogs
	
	@commands.Cog.listener()
	async def on_ready(self):
		print(f"Bot ready on {self.client.user.name} ({self.client.user.id})")
		await self.client.change_presence(activity=Config.status)
	
	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
			if isinstance(error, commands.CommandNotFound):
				pass
			else:
				try:await ctx.send(str(error))
				except:log(f'[red]ERROR[/red] [blue]Can not send message about error![/blue]')
				log(f'[red bold]DISCORD WARNING[/][red] {error}')

def setup(client):
	client.add_cog(BOT_EVENTS(client))