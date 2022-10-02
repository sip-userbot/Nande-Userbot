import os

import requests

from userbot._func.decorators import Panda_cmd as sip-userbot_on_cmd
from userbot._func._helpers import edit_or_reply, get_text
from . import HELP


HELP(
    "paste",
)

@sip-userbot_on_cmd(
    ["paste"],
    cmd_help={
        "help": "Pastes The File Text In Nekobin!",
        "example": "{ch}paste (reply to file)",
    },
)
async def paste(client, message):
    pablo = await edit_or_reply(message, "`Please Wait.....`")
    tex_t = get_text(message)
    message_s = tex_t
    if not tex_t:
        if not message.reply_to_message:
            await pablo.edit("`Reply To File / Give Me Text To Paste!`")
            return
        if not message.reply_to_message.text:
            file = await message.reply_to_message.download()
            m_list = open(file, "r").read()
            message_s = m_list
            os.remove(file)
        elif message.reply_to_message.text:
            message_s = message.reply_to_message.text
    key = (
        requests.post("https://nekobin.com/api/documents", json={"content": message_s})
        .json()
        .get("result")
        .get("key")
    )
    url = f"https://nekobin.com/{key}"
    raw = f"https://nekobin.com/raw/{key}"
    reply_text = f"Pasted Text To [NekoBin]({url}) And For Raw [Click Here]({raw})"
    await pablo.edit(reply_text)
