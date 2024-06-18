
import os

import discord
import requests
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

    for guild in bot.guilds:
        print(guild)

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

@bot.command()
async def say(ctx, *, message):
    """Repeats the message provided by the user."""
    await ctx.send(message)

@bot.command()
async def servers(ctx):
    response = requests.get(f'http://{server_ip}:{server_port}/mc/server')
    print(response.json())

    await ctx.send(F'RESPONSE: {response.json()}')


@bot.command()
async def whitelist(ctx, server_id: str, user_name: str):
    """Adds two numbers provided by the user."""
    print(user_name)

    response = requests.post(f"http://{server_ip}:{server_port}/mc/server/{server_id}", params={"username": f"{user_name}", 'token': f'{os.getenv("SERVER_TOKEN")}'})
    print(response.json())
    #send a message to minecraft server controller
    #get response
    await ctx.send(f"RESPONSE: {response.json()}")

@bot.command()
async def online(ctx, server_id: str | None):
    print("HERE 1")

    response = requests.get(f"http://{server_ip}:{server_port}/mc/server/{server_id}", params={'token': f'{os.getenv("SERVER_TOKEN")}'})
    print(response.json())

    await ctx.send(f"RESPONSE: {response.json()}")

    await ctx.send(f"server id: {server_id}")

@bot.command()
async def set_default(ctx, servername: str | None):
    await ctx.send(f'servername: {servername}')


bot.run(discord_api_key)


    