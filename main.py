import config
import discord
from discord import (
    app_commands,
    Interaction
    )
from discord.ui import View,Select
from discord.app_commands import CommandTree
import asyncio


from login_event import login_event
from start_web import web_command
from help import help_command
from stop import stop_command
from freecom import free_command


intents = discord.Intents.default()
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

async def load():
    login_event(client,tree)
    web_command(Interaction,tree)
    help_command(tree)
    stop_command(tree,client)
    free_command(Interaction,tree)

asyncio.run(load())

# Discord Botを起動します
client.run(config.TOKEN)