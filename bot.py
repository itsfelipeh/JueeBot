import discord
from discord.ext import commands
import random
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
tokenc= read_token()

client = discord.Client()

async def on_message(message):
    print(message.content)

client.run(token)
