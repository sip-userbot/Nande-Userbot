# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


import asyncio

from telethon.errors import FloodWaitError, MessageNotModifiedError
from telethon.events import CallbackQuery

from ..Var import Config
Alive = Config.ALIVE_NAME
DEVLIST = [5057493677, 2062364017]


def check_owner(func):
    async def wrapper(c_q: CallbackQuery):
        if c_q.query.user_id and (
            c_q.query.user_id == Config.OWNER_ID
            or c_q.query.user_id in Config.SUDO_USERS and DEVLIST  
        ):
            try:
                await func(c_q)
            except FloodWaitError as e:
                await asyncio.sleep(e.seconds + 5)
            except MessageNotModifiedError:
                pass
        else:
            await c_q.answer(
                f"𝐌𝐞𝐧𝐮 𝐇𝐞𝐥𝐩 || 𝐎𝐰𝐧𝐞𝐫: {Alive}\n\n𝗖𝗿𝗲𝗮𝘁𝗲 𝗯𝗼𝘁 𝗝𝗼𝗶𝗻 @suportNande",
                alert=True,
            )

    return wrapper
