# -*- coding: utf-8 -*-
# !/usr/bin/python3

import discord
import asyncio
from discord.ext.commands import Bot

client = discord.Client()
bot = Bot(command_prefix="!")


@client.event
async def on_read():
    print("Client logged in")


@client.event
async def on_message(message):
    if message.content.startswith("Hello, Handles."):
        await client.send_message(message.channel, "Hi, I'm Handles.")


@bot.command()
async def echo(*, message: str):
    await bot.say(message)


@bot.command()
async def hans():
    await bot.say("Get zu flammenwerfer!")


@bot.command()
async def lunch():
    await bot.say("Ask your Gideon, you bastard!")


@bot.command()
async def supl():
    await bot.say("Ask your Gideon, you bastard!")


bot.run("MzA2NDg3MDQ3MjE5MzE0NzAx.C-EeEQ.M7viDKD79MZYVC2MWTnqwMIChdI")
