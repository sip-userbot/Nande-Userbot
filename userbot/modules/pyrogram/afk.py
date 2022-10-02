from datetime import datetime

from pyrogram import filters

from userbot.modules.pyrogram.database.afk import check_afk, go_afk, no_afk
from ..._func.decorators import ilhammansiz_on_cmd, listen
from ..._func._helpers import edit_or_reply, get_text
from ..._func.logger_s import LogIt

afk_sanity_check: dict = {}


async def is_afk_(f, client, message):
    af_k_c = check_afk()
    if af_k_c:
        return bool(True)
    else:
        return bool(False)


is_afk = filters.create(func=is_afk_, name="is_afk_")


@ilhammansiz_on_cmd(
    ["afk"],
    propagate_to_next_handler=False,
    cmd_help={
        "help": "Set AFK!",
        "example": "{ch}afk",
    },
)
async def set_afk(client, message):
    pablo = await edit_or_reply(message, "`Processing..`")
    msge = None
    msge = get_text(message)
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    log = LogIt(message)
    if msge:
        msg = (
                f"┌ 🐍 AFK\n"
                f"│┌ Saya Sedang AFK\n"
                f"└└ Alasan: ```{msge}```"
            )
        await log.log_msg(
            client,
            f"#Afk Afk Is Active And Reason is {msge}",
        )
        go_afk(afk_start, msge)
    else:
        msg = (
                f"┌ 🐍 AFK\n"
                f"│┌ Saya Sedang AFK\n"
                f"└└ Alasan: ```{msge}```"
            )
        await log.log_msg(
            client,
            f"#Afk Afk Is Active",
        )
        go_afk(afk_start)
    await pablo.edit(msg)


@listen(
    is_afk
    & (filters.mentioned | filters.private)
    & ~filters.me
    & ~filters.bot
    & ~filters.edited
    & filters.incoming
)
async def afk_er(client, message):
    if not message:
        return
    if not message.from_user:
        return
    use_r = int(message.from_user.id)
    if use_r not in afk_sanity_check.keys():
        afk_sanity_check[use_r] = 1
    else:
        afk_sanity_check[use_r] += 1
    if afk_sanity_check[use_r] == 5:
        await message.reply_text(
            "`I Told You 5 Times That My Master Isn't Available, Now I Will Not Reply To You. ;(`"
        )
        afk_sanity_check[use_r] += 1
        return
    if afk_sanity_check[use_r] > 5:
        return
    lol = check_afk()
    reason = lol["reason"]
    if reason == "":
        reason = None
    back_alivee = datetime.now()
    afk_start = lol["time"]
    afk_end = back_alivee.replace(microsecond=0)
    total_afk_time = str((afk_end - afk_start))
    message_to_reply = (
        f"I Am **[AFK]** Right Now. \n**Last Seen :** `{total_afk_time}`\n**Reason** : `{reason}`"
        if reason
        else f"I Am **[AFK]** Right Now. \n**Last Seen :** `{total_afk_time}`"
    )
    await message.reply(message_to_reply)


@listen(filters.outgoing & filters.me & is_afk)
async def no_afke(client, message):
    lol = check_afk()
    back_alivee = datetime.now()
    afk_start = lol["time"]
    afk_end = back_alivee.replace(microsecond=0)
    total_afk_time = str((afk_end - afk_start))
    kk = await message.reply(
        f"""__Pro is Back Alive__\n**No Longer afk.**\n `I Was afk for:``{total_afk_time}`""",
    )
    await kk.delete()
    no_afk()
    log = LogIt(message)
    await log.log_msg(
        client,
        f"#AfkLogger User is Back Alive ! No Longer Afk\n AFK for : {total_afk_time} ",
    )
