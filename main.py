# -*- coding: utf-8 -*-
# !/usr/bin/python3

import discord
import router

from config import BOT_ID

client = discord.Client()


@client.event
async def on_read():
    print("Client logged in")


@client.event
async def on_message(message):
    rtr = router.Router()
    await rtr.route_request(message, client)


client.run(BOT_ID)
