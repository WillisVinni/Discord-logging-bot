import discord
from discord.ext import commands
from io import StringIO
from sys import path
path.insert(1, "../")
from modules.embed import embedGenerator
from config import Config
from modules.logs import log


class MSG_EVENTS(commands.Cog):
    def __init__(self, client):
        self.client:discord.Client = client # sets the client variable so we can use it in cogs

    def get_log_channel(self,id_):
        return Config.log_channels
    
    # Удалено одно сообщение
    @commands.Cog.listener()
    async def on_message_delete(self,msg: discord.Message):
        if msg.author.bot:return
        if not msg.guild.id in Config.guilds:return
        
        for ch in self.get_log_channel(msg.guild.id):
            ch = await self.client.fetch_channel(ch);await ch.send(embed=embedGenerator(
                'Сообщение удалено',
                f'Сообщение:```\n{msg.content}```',
                msg.author,
                fields=[
                    {
                        "name":"Информация",
                        "value":f"Канал: {msg.channel.mention}\nУчастник: {msg.author.mention}" #\n<:partner:985459448384458772> Ссылка: {msg.jump_url}
                    }
                ]
            ), files=msg.attachments)
    
    # Массовое удаление сообщений
    @commands.Cog.listener()
    async def on_bulk_message_delete(self,msgs: list[discord.Message]):
        if not msgs[0].guild.id in Config.guilds:return
        text = ''
        msgt = msgs[0]
        
        for msg in msgs:
            text += f'{msg.created_at}: {msg.author.name} ({msg.author.id}) - \n{msg.content}\n\n{"-"*20}\n\n'
        
        with StringIO(text) as f:
            for ch in self.get_log_channel(msgt.guild.id):
                ch = await self.client.fetch_channel(ch);await ch.send(embed=embedGenerator(
                    'Массовое удаление сообщений',
                    f'Было произдведено массовое удаление сообщений из канала {msgt.channel.mention}. В файле (ANSII) все удалённые сообщения.'
                ), file=discord.File(f, 'msgs.txt'))

    # Сообщение изменено
    @commands.Cog.listener()
    async def on_message_edit(self,before, after: discord.Message):
        if not after.guild.id in Config.guilds:return
        if after.author.bot:return
        await self.client.process_commands(after)
        urls = ' , '.join(map(str, [i.url for i in after.attachments]))
        for ch in self.get_log_channel(after.guild.id):
            ch = await self.client.fetch_channel(ch)
            await ch.send(embed=embedGenerator(
                'Сообщение изменено',
                f'Сообщение от {after.author.mention} было изменено',
                after.author,
                time=after.edited_at,
                fields=[
                    {
                        'name':'До',
                        'value':f'```\n{before.content}```'
                    },
                    {
                        'name':'После',
                        'value':f'```\n{after.content}```'
                    },
                    {
                        'name':'Информация',
                        'value':f"Канал: {after.channel.mention}\nУчастник: {after.author.mention}\nСсылка: [\[ПЕРЕЙТИ]]({after.jump_url})",'inline':False
                    }
                ]
            ))

    # Очистка реакций
    @commands.Cog.listener()
    async def on_reaction_clear(self,msg: discord.Message, reacts: list[discord.Reaction]):
        if not msg.guild.id in Config.guilds:return
        r = ', '.join(map(str, [i.emoji for i in reacts]))
        for ch in self.get_log_channel(msg.guild.id):
            ch = await self.client.fetch_channel(ch)
            await ch.send(embed=embedGenerator(
                'Очистка реакций',
                'Была произведена очистка реакций',
                fields=[
                    {
                        'name':'Инфомрация',
                        'value':f'Автор сообщения: {msg.author.mention} ({msg.author.id})\n\
Канал с сообщением: {msg.channel.mention} ({msg.channel.id})\n\
Сообщение: [КЛИК]({msg.jump_url})\n\
Эмодзи: {r}'
                    }
                ]
            ))

    

def setup(client):
	client.add_cog(MSG_EVENTS(client))