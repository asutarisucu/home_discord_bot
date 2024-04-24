import os
import config
import discord


def free_command(Interaction,tree):
    @tree.command(name='freecom',description='自由にコマンドを実行できます')
    async def freecom(interaction: Interaction,text:str):
        await interaction.response.defer()
        try:
            embed=config.TRUE_EMBED
            cmd=os.popen(text).read().rstrip('\n')
            embed.add_field(name=text+"が実行されました",value=cmd)
            await interaction.followup.send(embed=config.TRUE_EMBED)
            embed.remove_field(0)
            
        except Exception as e:
            embed=config.ERROR_EMBED
            embed.add_field(name="エラーが発生しました",value=e)
            await interaction.followup.send(embed)