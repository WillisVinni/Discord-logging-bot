import discord
from discord.ext import commands
from io import StringIO
from sys import path
path.insert(1, "../")
from modules.embed import embedGenerator
from config import Config
from modules.logs import log


class MBR_EVENTS(commands.Cog):
    def __init__(self, client):
        self.client:discord.Client = client # sets the client variable so we can use it in cogs

    def get_log_channel(self,id_):
        return Config.log_channels
    
    @commands.Cog.listener()
    async def on_member_join(self,mbr: discord.Member):
        if not mbr.guild.id in Config.guilds:return
        
        for ch in self.get_log_channel(mbr.guild.id):ch = await self.client.fetch_channel(ch);await ch.send(embed=embedGenerator(
            "Новый участник",
            f"На сервер зашёл новый {mbr.mention}",
            mbr,
            fields=[
                {
                    'name':'Информация',
                    'value':f'ID: {mbr.id}\nЗашёл в: {mbr.joined_at.strftime("%d.%m.%Y %H:%M:%S")}\nАккаунт создан: {mbr.created_at.strftime("%d.%m.%Y %H:%M:%S")}'
                }
            ],
            time=mbr.joined_at
        ))
        
    @commands.Cog.listener()
    async def on_member_remove(self,mbr: discord.User):
        try:
            if not mbr.guild.id in Config.guilds:return
        except:pass

        for ch in self.get_log_channel(mbr.guild.id):ch = await self.client.fetch_channel(ch);await ch.send(embed=embedGenerator(
            "Участник вышел",
            f"Участник {mbr.name} ({mbr.id}) вышел из сервера."
        ))
    
    @commands.Cog.listener()
    async def on_member_ban(self,guild: discord.Guild, user: discord.User):
        if not guild.id in Config.guilds:return
        for ch in self.get_log_channel(guild.id):ch = await self.client.fetch_channel(ch);await ch.send(embed=embedGenerator(
            "Произошёл бан пользователя",
            f"Пользователя {user.name} ({user.id}) забанили"
        ))
    
    @commands.Cog.listener()
    async def on_member_unban(self,guild: discord.Guild, user: discord.User):
        if not guild.id in Config.guilds:return
        
        for ch in self.get_log_channel(guild.id):ch = await self.client.fetch_channel(ch);await ch.send(embed=embedGenerator(
            "Пользователя разбанили",
            f"Пользователя {user.name} ({user.id}) разбанили"
        ))
    

    

def setup(client):
	client.add_cog(MBR_EVENTS(client))