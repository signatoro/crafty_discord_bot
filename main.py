
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

discord_api_key = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

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
    #send a message to minecraft server controller
    #get response
    await ctx.send("Not implemented yet")

bot.run(discord_api_key)


    