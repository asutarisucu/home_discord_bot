import discord
import config

class Button(discord.ui.View):
    def __init__(self,client, timeout=None):
        super().__init__(timeout=timeout)
        self.client=client

    @discord.ui.button(label="OK", style=discord.ButtonStyle.success)
    async def ok(self, button: discord.ui.Button, interaction: discord.Interaction):
        await button.response.send_message("botを停止します")
        await self.client.close()

    @discord.ui.button(label="NO", style=discord.ButtonStyle.gray)
    async def no(self, button: discord.ui.Button, interaction: discord.Interaction):
        await button.response.send_message("コマンドを中断します")

def stop_command(tree,client):
    @tree.command(name='stop', description='botを停止します')
    async def stop(interaction: discord.Interaction):
        view = Button(client,timeout=None)
        embed=discord.Embed(
            color=0xff0000
        )
        embed.add_field(name="警告",value="本当に停止してもいいですか？\n起動するにはもう一度コンソールから起動する必要があります")
        await interaction.response.send_message(embed=embed,view=view)