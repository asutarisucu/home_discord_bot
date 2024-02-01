import config
import discord
from discord import (
    app_commands,
    Interaction
    )
from discord.ui import View,Select
from discord.app_commands import CommandTree
from home_math import Math

intents = discord.Intents.default()
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
  print(f'Logged in as {client.user}')
  await tree.sync()

@tree.command(name='math',description='簡単な計算をします')
async def start(interaction: Interaction,num1:int,text:str,num2:int):
    ans:int=Math(interaction,num1,text,num2)
    if ans=="null":
        await interaction.response.send_message("無効な演算子です")
    else:
        await interaction.response.send_message(f"{num1}{text}{num2}={ans:int}")

# Discord Botを起動します
client.run(config.TOKEN)