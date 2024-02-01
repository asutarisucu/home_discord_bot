import config
import discord
from discord import (
    app_commands,
    Interaction
    )
from discord.ui import View,Select
from discord.app_commands import CommandTree
from login_event import login_event

intents = discord.Intents.default()
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

login_event(client,tree)

# Discord Botを起動します
client.run(config.TOKEN)