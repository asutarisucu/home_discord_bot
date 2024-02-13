import discord
import os
def web_command(Interaction,tree):
    @tree.command(name='start',description='webサーバーを起動します')
    async def start(interaction: Interaction,text:str):
        commands = {
        'start':"sudo systemctl start apache2"
        }
        if text in commands:
            os.system(commands[text])
        else:
            interaction.response.send_message('無効な引数です')