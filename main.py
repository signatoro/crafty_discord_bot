
import os
# import requests

import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

discord_api_key = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
server_ip = os.getenv("IP_ADDRESS")
server_port = os.getenv("SERVER_PORT")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')


@bot.command()
async def say(ctx, *, message):
    """Repeats the message provided by the user."""
    await ctx.send(message)

@bot.command()
async def whitelist(ctx, user_name: str):
    """Adds two numbers provided by the user."""
    print(user_name)

    # response = requests.post(f"http://{server_ip}:{server_port}/whitelist", data=user_name)
    # print(response)
    #send a message to minecraft server controller
    #get response
    await ctx.send("Not implemented yet")

bot.run(discord_api_key)


    