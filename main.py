import discord
import asyncio
from discord.ext.commands import Bot

bot = Bot(command_prefix="!")


@bot.event
async def on_read():
    print("Client logged in")


@bot.command()
async def hello():
    return await bot.say("Hello, world! ")


@bot.command()
async def echo(*, message: str):
    await bot.say(message)


bot.run("MzA2NDg3MDQ3MjE5MzE0NzAx.C-EeEQ.M7viDKD79MZYVC2MWTnqwMIChdI")