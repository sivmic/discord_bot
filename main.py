import discord
import asyncio
from discord.ext.commands import Bot

bot = Bot(command_prefix="!")


@bot.event
async def on_read():
    print("Client logged in")


@bot.command()
async def hello(*args):
    return await bot.say("Hello, world!")


bot.run("MzA2NDg3MDQ3MjE5MzE0NzAx.C-EeEQ.M7viDKD79MZYVC2MWTnqwMIChdI")
