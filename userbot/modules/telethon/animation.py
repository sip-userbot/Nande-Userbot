import asyncio
from collections import deque

from . import edit_or_reply, NandeBot
pandaub = NandeBot

plugin_category = "modules"


@NandeBot.sipuserbot_cmd(
    pattern="think$",
    command=("think", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}think",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "think")
    deq = deque(list("đ¤đ§đ¤đ§đ¤đ§"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@NandeBot.sip-userbot_cmd(
    pattern="lmao$",
    command=("lmao", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}lmao",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "lmao")
    deq = deque(list("đđ¤Ŗđđ¤Ŗđđ¤Ŗ"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@NandeBot.sipuserbot_cmd(
    pattern="nothappy$",
    command=("nothappy", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}nothappy",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "nathappy")
    deq = deque(list("đâšī¸đâšī¸đâšī¸đ"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@NandeBot.sip-userbot_cmd(
    pattern="clock$",
    command=("clock", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}clock",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "clock")
    deq = deque(list("đđđđđđđđđđđ"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@NandeBot.sip-userbot_cmd(
    pattern="muah$",
    command=("muah", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}muah",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "muah")
    deq = deque(list("đđđđđ"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@NandeBot.sipuserbot_cmd(
    pattern="heart$",
    command=("heart", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}heart",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "heart")
    deq = deque(list("â¤ī¸đ§Ąđđđđđ¤"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@NandeBot.sip-userbot_cmd(
    pattern="gym$",
    command=("gym", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}gym",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "gym")
    deq = deque(list("đâđâđ¤¸âđâđâđ¤¸âđâđâđ¤¸â"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@NandeBot.sipuserbot_cmd(
    pattern="earth$",
    command=("earth", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}earth",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "earth")
    deq = deque(list("đđđđđđđđ"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@NandeBot.sip-userbot_cmd(
    pattern="moon$",
    command=("moon", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}moon",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "moon")
    deq = deque(list("đđđđđđđđ"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@NandeBot.sipuserbot_cmd(
    pattern="smoon$",
    command=("smoon", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}smoon",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "smoon")
    animation_interval = 0.2
    animation_ttl = range(101)
    await event.edit("smoon..")
    animation_chars = [
        "đđđđđ\nđđđđđ\nđđđđđ\nđđđđđ\nđđđđđ",
        "đđđđđ\nđđđđđ\nđđđđđ\nđđđđđ\nđđđđđ",
        "đđđđđ\nđđđđđ\nđđđđđ\nđđđđđ\nđđđđđ",
        "đđđđđ\nđđđđđ\nđđđđđ\nđđđđđ\nđđđđđ",
        "đđđđđ\nđđđđđ\nđđđđđ\nđđđđđ\nđđđđđ",
        "đđđđđ\nđđđđđ\nđđđđđ\nđđđđđ\nđđđđđ",
        "đđđđđ\nđđđđđ\nđđđđđ\nđđđđđ\nđđđđđ",
        "đđđđđ\nđđđđđ\nđđđđđ\nđđđđđ\nđđđđđ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@NandeBot.sipuserbot_cmd(
    pattern="tmoon$",
    command=("tmoon", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}tmoon",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "tmoon")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("tmoon..")
    animation_chars = [
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])
