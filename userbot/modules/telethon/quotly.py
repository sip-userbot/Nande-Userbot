
# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid


from os import remove
from random import choice

from telethon.tl.functions.users import GetFullUserRequest

from . import edit_delete, edit_or_reply
from ...helpers.utils.misc import create_quotly
plugin_category = "plugins"

from . import nandeub

from .carbon import all_col


@nandeub.sip-userbot_cmd(
    pattern="q(?: |$)(.*)",
    command=("q", plugin_category),
    info={
        "header": "membuat text menjadi tulisan",
        "usage": [
            "{tr}q <text/balas ke pesab>",
            "{tr}q <username> <reply to text>",
            "{tr}q <angka>",
        ],
    },
)
async def quotly(event):
    match = event.pattern_match.group(1).strip()
    if not event.is_reply:
        return await edit_delete(event, "**Mohon Balas ke Pesan**")
    msg = await edit_or_reply(event, "`Processing...`")
    reply = await event.get_reply_message()
    replied_to, reply_ = None, None
    if match:
        spli_ = match.split(maxsplit=1)
        if (spli_[0] in ["r", "reply"]) or (
            spli_[0].isdigit() and int(spli_[0]) in range(1, 21)
        ):
            if spli_[0].isdigit():
                if not event.client._bot:
                    reply_ = await event.client.get_messages(
                        event.chat_id,
                        min_id=event.reply_to_msg_id - 1,
                        reverse=True,
                        limit=int(spli_[0]),
                    )
                else:
                    id_ = reply.id
                    reply_ = []
                    for msg_ in range(id_, id_ + int(spli_[0])):
                        msh = await event.client.get_messages(event.chat_id, ids=msg_)
                        if msh:
                            reply_.append(msh)
            else:
                replied_to = await reply.get_reply_message()
            try:
                match = spli_[1]
            except IndexError:
                match = None
    user = None
    if not reply_:
        reply_ = reply
    if match:
        match = match.split(maxsplit=1)
    if match:
        if match[0].startswith("@") or match[0].isdigit():
            try:
                match_ = await event.client(GetFullUserRequest(match[0]))
                user = await event.client.get_entity(match_)
            except ValueError:
                pass
            match = match[1] if len(match) == 2 else None
        else:
            match = match[0]
    if match == "random":
        match = choice(all_col)
    try:
        file = await create_quotly(reply_, bg=match, reply=replied_to, sender=user)
    except Exception as er:
        return await msg.edit(f"**ERROR:** `{er}`")
    message = await reply.reply("Quotly by Nande-Userbot", file=file)
    remove(file)
    await msg.delete()
    return message
