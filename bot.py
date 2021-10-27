'''MIT License

Copyright (c) 2021 vasu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

import requests
from telethon import *
from telethon import TelegramClient
from telethon import events
import os
import logging
import asyncio
from asyncio import sleep
import functools
from telethon.tl import types
from telethon.tl import functions



logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

# Basics
APP_ID = os.environ.get("APP_ID", default=None)
API_HASH = os.environ.get("API_HASH", default=None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", default=None)
EVENT_LOGS = os.environ.get("EVENT_LOGS", default=None)
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", default="VasuXD")
OWNER = os.environ.get("OWNER", default="VasuXD")


bot = TelegramClient("SpamingBot", APP_ID, API_HASH)
run = bot.start(bot_token=BOT_TOKEN) 


async def is_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (
                await bot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerUser):
        return True

vasu = "this bot is made by vasu"


@bot.on(events.NewMessage(pattern="^/cspam (.+)"))
async def tmeme(e):
    if not "vasu" in vasu:
     await e.reply("bhosdike motherchod randi ki olaad he tu saale hizde, developer ko credit dene me teri maa chud jati he kya randwe jo tune code se name htaya benchod. abhi uske github pr jaa or follow kr gandu. made by vasu")

          
    else: 
         cspam = str(e.pattern_match.group(1))
         message = cspam.replace(" ", "")
         await e.delete()
         for letter in message:
             await e.respond(letter)



@bot.on(events.NewMessage(pattern="^/wspam (.+)"))
async def t_meme(e):

    if not "vasu" in vasu:
      await e.reply("bhosdike motherchod randi ki olaad he tu saale hizde, developer ko credit dene me teri maa chud jati he kya randwe jo tune code se name htaya benchod. abhi uske github pr jaa or follow kr gandu. made by vasu")
    
    else:
        wspam = str(e.pattern_match.group(1))
        message = wspam.split()
        await e.delete()
        for word in message:
            await e.respond(word)
 


@bot.on(events.NewMessage(pattern="^/spam (\d+) (.+)"))
async def spammer(e):

    if not "vasu" in vasu:
      await e.reply("bhosdike motherchod randi ki olaad he tu saale hizde, developer ko credit dene me teri maa chud jati he kya randwe jo tune code se name htaya benchod. abhi uske github pr jaa or follow kr gandu. made by vasu")
    
    if not e.sender_id == 1926090919:
        await e.reply("Fucking mf, you're not my owner.")
    
    else:
        counter = int(e.pattern_match.group(1))
        spam_message = str(e.pattern_match.group(2))
        await e.delete()
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])



@bot.on(events.NewMessage(pattern="^/picspam (\d+) (.+)"))
async def tiny_pic_spam(e):

    if not "vasu" in vasu:
      await e.reply("bhosdike motherchod randi ki olaad he tu saale hizde, developer ko credit dene me teri maa chud jati he kya randwe jo tune code se name htaya benchod. abhi uske github pr jaa or follow kr gandu. made by vasu")

    
    else:
        counter = int(e.pattern_match.group(1))
        link = str(e.pattern_match.group(2))
        await e.delete()
        for _ in range(1, counter):
            await e.client.send_file(e.chat_id, link)



@bot.on(events.NewMessage(pattern="/delayspam (.*)"))
async def spammer(e):

    if not "vasu" in vasu:
      await e.reply("bhosdike motherchod randi ki olaad he tu saale hizde, developer ko credit dene me teri maa chud jati he kya randwe jo tune code se name htaya benchod. abhi uske github pr jaa or follow kr gandu. made by vasu")

    
    else:
        spamDelay = float(e.pattern_match.group(1).split(" ", 2)[0])
        counter = int(e.pattern_match.group(1).split(" ", 2)[1])
        spam_message = str(e.pattern_match.group(1).split(" ", 2)[2])
        await e.delete()
        for _ in range(1, counter):
            await e.respond(spam_message)
            await sleep(spamDelay)





print ("Successfully Started")
run.run_until_disconnected()
