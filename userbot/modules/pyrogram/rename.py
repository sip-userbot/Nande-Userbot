# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


import time

from userbot._func.decorators import Nande_cmd as sip-userbot_on_cmd
from userbot._func._helpers import edit_or_reply, get_text, progress

from . import HELP


HELP(
    "rename",
)

@sip-userbot_on_cmd(
    ["rename", "rupload"],
    cmd_help={
        "help": "Rename File!",
        "example": "{ch}rename (reply to file) (new name)",
    },
)
async def rename(client, message):
    pablo = await edit_or_reply(message, "`Processing..`")
    fname = get_text(message)
    if not fname:
        await pablo.edit("Tolong Beri Nama Baru Untuk File Dengan Ekstensi")
        return
    if not message.reply_to_message:
        await pablo.edit("Silakan Balas Ke File Untuk Mengganti Nama")
        return
    await pablo.edit("⚡️`Ganti nama dan unggah sedang berlangsung, harap tunggu!`⚡️")
    file_name = None
    try:
        file_name = message.reply_to_message.document.file_name
    except:
        pass
    if file_name:
        Kk = fname.split(".")
        try:
            Kk[1]
        except:
            fuck = file_name.rpartition(".")[-1]
            fname = f"{fname}.{fuck}"
    EsCoBaR = await message.reply_to_message.download(fname)
    caption = ""
    if message.reply_to_message.caption:
        caption = message.reply_to_message.caption
    c_time = time.time()
    await client.send_document(
        message.chat.id,
        EsCoBaR,
        caption=caption,
        progress=progress,
        progress_args=(pablo, c_time, f"`Uploading {fname}`", EsCoBaR),
    )
    await pablo.edit(
        "File Diganti Nama dan Diunggah. Oleh Nande - UserBot. Dapatkan Nande -UserBot Anda dari @NandeUserbot"
    )

