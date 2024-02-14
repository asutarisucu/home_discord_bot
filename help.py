import discord
def help_command(Interaction,tree):
    @tree.command(name='help',description='コマンドヘルプを表示します')
    async def start(interaction: Interaction):
        await interaction.response.defer()
        embed=discord.Embed(
            color=0x7cfc00,
            title="command list"
        )
        embed.add_field(inline=False,name="web",value="start\nstop\nrestart\nupdate")
        await interaction.followup.send(embed=embed)
        