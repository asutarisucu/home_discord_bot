import discord
import os
def web_command(Interaction,tree):
    @tree.command(name='web',description='webサーバーに関するコマンドです')
    async def start(interaction: Interaction,text:str):
        commands = {
        'start':"sudo systemctl start apache2"
        }
        if text in commands:
            os.system(commands[text])
            await interaction.response.send_message('コマンドが実行されました')
        else:
            await interaction.response.send_message('無効な引数です')