# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


from pyrogram import filters
from userbot.modules.pyrogram.database.gbandb import gban_info, gban_list, gban_user, ungban_user
from userbot.modules.pyrogram.database.gmutedb import gmute, is_gmuted, ungmute
from userbot.Var import Config
from userbot._func.decorators import Nande_cmd as sip-userbot_on_cmd, listen
from userbot._func._helpers import (
    edit_or_reply,
    edit_or_send_as_file,
    get_text,
    get_user,
    iter_chats,
)
from userbot._func.logger_s import LogIt
from . import devs_id
from . import HELP


HELP(
    "gban",
)

@sip-userbot_on_cmd(
    ["gmute"],
    cmd_help={
        "help": "Nonaktifkan Pengguna Secara Global!",
        "example": "{ch}gmute (membalas pesan pengguna ATAU memberikan ID-nya)",
    },
)
async def gmute_him(client, message):
    g = await edit_or_reply(message, "`Processing..`")
    text_ = get_text(message)
    user, reason = get_user(message, text_)
    if not user:
        await g.edit("`Balas Ke Pengguna Atau Sebut Untuk Gmute Dia`")
        return
    try:
        userz = await client.get_users(user)
    except:
        await g.edit(f"`404 : Pengguna Tidak Ada Dalam Obrolan Ini !`")
        return
    if not reason:
        reason = "Just_Gmutted!"
    if userz.id == (client.me).id:
        await g.edit("`Oh, Ini Sangat Lucu Btw :/`")
        return
    if userz.id in devs_id:
        await g.edit("`Sayangnya, Saya Tidak Bisa Melakukannya!`")
        return
    if userz.id in Config.AFS:
        await g.edit("`Pengguna Sudo Tidak Dapat Dipotong! Hapus Dia Dan Coba Lagi!`")
        return
    if is_gmuted(userz.id):
        await g.edit("`Gmute ulang?serius? :/`")
        return
    gmute(userz.id, reason)
    gmu = f"**#Gmutted** \n**User :** `{userz.id}` \n**Reason :** `{reason}`"
    await g.edit(gmu)
    log = LogIt(message)
    await log.log_msg(client, gmu)


@sip-userbot_on_cmd(
    ["ungmute"],
    cmd_help={
        "help": "Suarakan Pengguna Secara Global!",
        "example": "{ch}ungmute (balas pesan pengguna ATAU berikan ID-nya)",
    },
)
async def gmute_him(client, message):
    ug = await edit_or_reply(message, "`Processing..`")
    text_ = get_text(message)
    user_ = get_user(message, text_)[0]
    if not user_:
        await ug.edit("`Reply To User Or Mention To Un-Gmute Him`")
        return
    try:
        userz = await client.get_users(user_)
    except:
        await ug.edit(f"`404 : Pengguna Tidak Ada Dalam Obrolan Ini !`")
        return
    if userz.id == (client.me).id:
        await ug.edit("`Oh, Ini Sangat Lucu Btw :/`")
        return
    if userz.id in Config.AFS:
        await ug.edit("`Pengguna Sudo Tidak Dapat Dibatalkan! Hapus Dia Dan Coba Lagi!`")
        return
    if not is_gmuted(userz.id):
        await ug.edit("`Un-Gmute Pengguna yang Tidak Di-Gmut? Dengan serius? :/`")
        return
    ungmute(userz.id)
    ugmu = f"**#Un-Gmutted** \n**User :** `{userz.id}`"
    await ug.edit(ugmu)
    log = LogIt(message)
    await log.log_msg(client, ugmu)


@sip-userbot_on_cmd(
    ["gban"],
    cmd_help={
        "help": "Larang Pengguna Secara Global!",
        "example": "{ch}gban (balas pesan pengguna ATAU berikan ID-nya)",
    },
)
async def gbun_him(client, message):
    gbun = await edit_or_reply(message, "`Processing..`")
    text_ = get_text(message)
    user, reason = get_user(message, text_)
    failed = 0
    if not user:
        await gbun.edit("`Balas Ke Pengguna Atau Sebutkan Ke GBan Dia`")
        return
    try:
        userz = await client.get_users(user)
    except:
        await gbun.edit(f"`404 : Pengguna Tidak Ada Dalam Obrolan Ini !`")
        return
    if not reason:
        reason = "Private Reason!"
    if userz.id == (client.me).id:
        await gbun.edit("`Oh, Ini Sangat Lucu Btw :/`")
        return
    if userz.id in devs_id:
        await g.edit("`Sayangnya, Saya Tidak Bisa Melakukannya!`")
        return
    if userz.id in Config.AFS:
        await gbun.edit("`Pengguna Sudo Tidak Dapat Diblokir! Hapus Dia Dan Coba Lagi!`")
        return
    if gban_info(userz.id):
        await gbun.edit("`Re-Gban? Serius? :/`")
        return
    await gbun.edit("`Tolong, Tunggu Mengambil Obrolan Anda!`")
    chat_dict = await iter_chats(client)
    chat_len = len(chat_dict)
    if not chat_dict:
        gbun.edit("`Anda Tidak Memiliki Obrolan! Sangat sedih`")
        return
    await gbun.edit("`Mulai GBan Sekarang!`")
    for ujwal in chat_dict:
        try:
            await client.kick_chat_member(ujwal, int(userz.id))
        except:
            failed += 1
    gban_user(userz.id, reason)
    gbanned = f"**#GBanned** \n**User :** [{userz.first_name}](tg://user?id={userz.id}) \n**Reason :** `{reason}` \n**Affected Chats :** `{chat_len-failed}`"
    await gbun.edit(gbanned)
    log = LogIt(message)
    await log.log_msg(client, gbanned)


@sip-userbot_on_cmd(
    ["ungban"],
    cmd_help={
        "help": "Unban Pengguna Secara Global!",
        "example": "{ch}ungban (membalas pesan pengguna ATAU memberikan ID-nya)",
    },
)
async def ungbun_him(client, message):
    ungbun = await edit_or_reply(message, "`Processing..`")
    text_ = get_text(message)
    user = get_user(message, text_)[0]
    failed = 0
    if not user:
        await ungbun.edit("`Balas Ke Pengguna Atau Sebut Untuk Un-GBan Dia`")
        return
    try:
        userz = await client.get_users(user)
    except:
        await ungbun.edit(f"`404 : Pengguna Tidak Ada!`")
        return
    if userz.id == (client.me).id:
        await ungbun.edit("`Oh, Ini Sangat Lucu Btw :/`")
        return
    if not gban_info(userz.id):
        await ungbun.edit("`Batalkan Gban Pengguna yang Tidak Dicekal?serius? :/`")
        return
    await ungbun.edit("`Tolong, Tunggu Mengambil Obrolan Anda!`")
    chat_dict = await iter_chats(client)
    chat_len = len(chat_dict)
    if not chat_dict:
        ungbun.edit("`Anda Tidak Memiliki Obrolan! Sangat sedih`")
        return
    await ungbun.edit("`Mulai Un-GBans Sekarang!`")
    for ujwal in chat_dict:
        try:
            await client.unban_chat_member(ujwal, int(userz.id))
        except:
            failed += 1
    ungban_user(userz.id)
    ungbanned = f"**#Un_GBanned** \n**User :** [{userz.first_name}](tg://user?id={userz.id}) \n**Affected Chats :** `{chat_len-failed}`"
    await ungbun.edit(ungbanned)
    log = LogIt(message)
    await log.log_msg(client, ungbanned)


@listen(filters.incoming & ~filters.me & ~filters.user(Config.AFS))
async def watch(client, message):
    if not message:
        return
    if not message.from_user:
        return
    user = message.from_user.id
    if is_gmuted(user):
        try:
            await message.delete()
        except:
            return
    if gban_info(user):
        if message.chat.type != "supergroup":
            return
        try:
            me_ = await message.chat.get_member(int(client.me.id))
        except:
            return
        if not me_.can_restrict_members:
            return
        try:
            await client.kick_chat_member(message.chat.id, int(user))
        except:
            return
        await client.send_message(
            message.chat.id,
            f"**#GbanWatch** \n**Chat ID :** `{message.chat.id}` \n**User :** `{user}` \n**Reason :** `{await gban_info(user)}`",
        )
    


@sip-userbot_on_cmd(
    ["gbanlist"],
    cmd_help={
        "help": "Dapatkan Daftar Pengguna yang Dilarang Secara Global!",
        "example": "{ch}gbanlist (membalas pesan pengguna ATAU memberikan ID-nya)",
    },
)
async def give_glist(client, message):
    oof = "**#GBanList** \n\n"
    glist = await edit_or_reply(message, "`Processing..`")
    list_ = gban_list()
    if len(list_) == 0:
        await glist.edit("`Tidak Ada Pengguna yang Diblokir Hingga Sekarang!`")
        return
    for lit in list_:
        oof += f"**User :** `{lit['user']}` \n**Reason :** `{lit['reason']}` \n\n"
    await edit_or_send_as_file(oof, glist, client, "GbanList", "Gban-List")


@sip-userbot_on_cmd(
    ["gbroadcast"],
    cmd_help={
        "help": "Kirim Pesan Ke Semua Obrolan, Anda Masuki!",
        "example": "{ch}gbroadcast (replay Pesan)",
    },
)
async def gbroadcast(client, message):
    msg_ = await edit_or_reply(message, "`Mengambil Daftar Obrolan Anda!`")
    failed = 0
    if not message.reply_to_message:
        await msg_.edit("`Balas Pesan Bos!`")
        return
    chat_dict = await iter_chats(client)
    chat_len = len(chat_dict)
    await msg_.edit("`Sekarang Mengirim Ke Semua Obrolan Mungkin!`")
    if not chat_dict:
        msg_.edit("`Anda Tidak Memiliki Obrolan! Sangat sedih`")
        return
    for c in chat_dict:
        try:
            await message.reply_to_message.copy(c)
        except:
            failed += 1
    await msg_.edit(
        f"`Message Sucessfully Send To {chat_len-failed} Chats! Failed In {failed} Chats.`"
    )
