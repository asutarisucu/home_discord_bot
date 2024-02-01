import discord
import config
def login_event(client,tree):
    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')##コンソールへの出力
        channel_list = list(client.get_all_channels())
        for i in range(len(channel_list)):
            if str(channel_list[i].id) == config.LOG_CHANNEL:
                channel = channel_list[i] 
        await channel.send(embed=config.LOGIN_EMBED)##指定したチャンネルへの出力
        
        await tree.sync()##コマンドの同期