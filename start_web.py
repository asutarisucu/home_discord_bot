import os
def web_command(Interaction,tree):
    @tree.command(name='web',description='webサーバーに関するコマンドです')
    async def start(interaction: Interaction,text:str):
        await interaction.response.defer()
        commands = {
        'start':"sudo systemctl start apache2",
        'stop':"sudo systemctl stop apache2",
        'restart':"sudo systemctl restart apache2",
        'update':"sudo bash /home/asuta/scripts/update_web.sh"
        }
        if text in commands:
            os.system(commands[text])
            await interaction.followup.send('コマンドが実行されました')
        else:
            await interaction.followup.send('無効な引数です')