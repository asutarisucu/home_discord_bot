import discord
import config
import shutil
def login_event(client,tree):
    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')##コンソールへの出力
        channel_list = list(client.get_all_channels())
        for i in range(len(channel_list)):
            if str(channel_list[i].id) == config.LOG_CHANNEL:
                channel = channel_list[i] 
        embed=create_embed()
        await channel.send(embed=config.LOGIN_EMBED)##指定したチャンネルへの出力
        
        await tree.sync()##コマンドの同期

def create_embed():
    embed=config.LOGIN_EMBED
    disksize=get_disk_size()
    embed.add_field(name="ディスク使用量",value=disksize)
    
def get_disk_size():
    total, used, free = shutil.disk_usage('/')
    try:
        used=float(used)
        kb=used/1024
    except:
        return"予期せぬエラーが発生しました"
    if kb>=1024:
        mb=kb/1024
        if mb>=1024:
            gb=mb/1024
            return "%.2fGB" %gb
        else:
            return "%.2fMB" %mb
    else:
        return "%.2fKB" %kb
    