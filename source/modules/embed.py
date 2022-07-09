from datetime import datetime
import discord

def embedGenerator(
    title:str,
    description:str='',
    member:discord.Member=None,
    color=0x2ecc71,
    thumbnail=None,
    time=datetime.now(),
    fields:list = []
):
    embed=discord.Embed(title=title, description=description, color=color)
    if member:embed.set_author(name=member.name, icon_url=member.avatar_url)
    
    for field in fields:
        if 'inline' in list(field.keys()):inline=field['inline']
        else:inline = True
        embed.add_field(name=field['name'], value=field['value'], inline=inline)
    embed.set_footer(text=time.strftime('%d.%m.%Y %H:%M:%S'))
    if thumbnail:embed.set_thumbnail(url=thumbnail)

    return embed
