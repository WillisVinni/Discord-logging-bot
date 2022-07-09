import discord
from discord.ext import commands
from io import StringIO
from sys import path
path.insert(1, "../")
from modules.embed import embedGenerator
from config import Config
from modules.logs import log


class GUILD_EVENTS(commands.Cog):
    def __init__(self, client):
        self.client:discord.Client = client # sets the client variable so we can use it in cogs

    def get_log_channel(self,id_):
        
        return Config.log_channels
    
    @commands.Cog.listener()
    async def on_guild_channel_create(self,chnl: discord.TextChannel):
        typee = 'текстовый' if str(chnl.type)=='text' else 'голосовой' if str(chnl.type)=='voice' else chnl.type
        for ch in self.get_log_channel(chnl.guild.id):ch = await self.client.fetch_channel(ch);await ch.send(embed=embedGenerator(
            f'Создан {typee} канал',
            f"Создан {typee} канал в категории {chnl.category.name}",
            time=chnl.created_at,
            fields=[
                {
                    'name':'Информация',
                    'value':f'Канал: {chnl.mention} ({chnl.id})\n\
Категория: {chnl.category.mention} ({chnl.category.id})\n\
Создан: {chnl.created_at.strftime("%d.%m.%Y %H:%M:%S")}'
                }
            ]
        ))
        
    @commands.Cog.listener()
    async def on_guild_channel_delete(self,chnl: discord.TextChannel):
        typee = 'текстовый' if str(chnl.type)=='text' else 'голосовой' if str(chnl.type)=='voice' else chnl.type
        ifs = chnl.last_message!=None if str(chnl.type)!='voice' else False
        contentm = chnl.last_message.content if ifs else 'Сообщения отсутствуют'
        for ch in self.get_log_channel(chnl.guild.id):ch = await self.client.fetch_channel(ch);await ch.send(embed=embedGenerator(
            f"Удален {typee} канал",
            f"Удален {typee} канал из категории {chnl.category.name}",
            fields = [
                {
                    'name':'Информация',
                    'value':f'Имя: {chnl.name}\nID: {chnl.id}\nСоздан в: {chnl.created_at.strftime("%d.%m.%Y %H:%M:%S")}\nПоследнее сообщение: ```\n{contentm}```\nID Категории: {chnl.category_id}'
                }
            ]

        ))
    # @commands.Cog.listener()
    # async def on_webhooks_update(chnl: discord.TextChannel):
    #     pass
    
        
    @commands.Cog.listener()
    async def on_guild_role_create(self,role: discord.Role):
        for ch in self.get_log_channel(role.guild.id):ch = await self.client.fetch_channel(ch);await ch.send(embed=embedGenerator(
            "Роль создана",
            f"Роль {role.mention} была создана",
            time=role.created_at,
            fields=[
                {
                    "name":"Информация",
                    "value":f"Имя роли: {role.name}\nID роли: {role.id}\nСоздана в: {role.created_at.strftime('%d.%m.%Y %H:%M:%S')}"
                }
            ]
        ))
        
    @commands.Cog.listener()
    async def on_guild_role_delete(self,role: discord.Role):
        for ch in self.get_log_channel(role.guild.id):ch = await self.client.fetch_channel(ch);await ch.send(embed=embedGenerator(
            "Удалена роль",
            f"Была удалена роль {role.name} ({role.id})"
        ))
        
    
        
    @commands.Cog.listener()
    async def on_invite_create(self,invite: discord.Invite):
        for ch in self.get_log_channel(invite.guild.id):ch = await self.client.fetch_channel(ch);await ch.send(embed=embedGenerator(
            "Был создан инвайт",
            f"Был создан инвайт {invite.url}",
            invite.inviter,
            time=invite.created_at,
            fields=[
                {
                    "name":"Информация",
                    "value":f"Инвайт: {invite.url}\nСоздатель: {invite.inviter.mention} ({invite.inviter.id})\n\
ID: {invite.id}\nВ канал: {invite.channel.mention} ({invite.channel.id})\nСоздан в: {invite.created_at.strftime('%d.%m.%Y %H:%M:%S')}"
                }
            ]
        ))
    @commands.Cog.listener()
    async def on_invite_delete(self,invite: discord.Invite):
        for ch in self.get_log_channel(invite.guild.id):ch = await self.client.fetch_channel(ch);await ch.send(embed=embedGenerator(
            "Инвайт удалён",
            f"Инвайт от {invite.inviter.mention} ({invite.inviter.id}) удалён. Он ссылался в канал: {invite.channel.mention} ({invite.channel.id})"
        ))
        

def setup(client):
	client.add_cog(GUILD_EVENTS(client))