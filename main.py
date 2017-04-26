# -*- coding: utf-8 -*-
# !/usr/bin/python3

import discord
import asyncio
import router

client = discord.Client()

@client.event
async def on_read():
    print("Client logged in")


@client.event
async def on_message(message):
    rtr = router.Router()
    await rtr.route_request(message, client)


client.run("MzA2NDg3MDQ3MjE5MzE0NzAx.C-EeEQ.M7viDKD79MZYVC2MWTnqwMIChdI")
