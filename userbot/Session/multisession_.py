from telethon import version

from .pyroclient import pyrotgbot, pyrobot
from telethon import functions, utils

import logging
from .._database._var import Var
from logging import getLogger
import pyrogram as Nandepyro
from .client import *
from .._func.startup import load_modulesPyro, plugin_collecter
from .pyroclient import *
import sys
LOGS = getLogger(__name__)
import os
from pyrogram import __version__ as pyrover

PRIVATE = int(os.environ.get("PRIVATE") or "-1001826967333")

cmdhr = os.environ.get("COMMAND_HAND_LER") or "."

MSG_ON = """
♤ 𝙽𝚊𝚗𝚍𝚎 - 𝚄𝚜𝚎𝚛𝚋𝚘𝚝 ♤
✨ Pengguna - @{}
♻️ Pyrogram Version - `{}'
`[Telah DiAktifkan]`
°Ketik `{}alive` untuk Mengecheck Bot
"""


THON_ON = """
♤ 𝙽𝚊𝚗𝚍𝚎 - 𝚄𝚜𝚎𝚛𝚋𝚘𝚝 ♤
✨ Pengguna - @{}
♻️ Telethon Version - `{}'
`[Telah Diaktifkan]`
°Ketik `{}alive` untuk Mengecheck Bot
"""


def Telethon():
    if Var.STRING_SESSION:
        try:
            NandeBot.start()
            cekbot.start(bot_token=CEKBOT)
            delta = NandeBot(functions.help.GetConfigRequest())
            for option in delta.dc_options:
                if option.ip_address == NandeBot.session.server_address:
                    if NandeBot.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {NandeBot.session.dc_id}"
                            f" to {option.id}"
                        )
                    NandeBot.session.set_dc(option.id, option.ip_address, option.port)
                    NandeBot.session.save()
                    break
            NandeBot.me = NandeBot.get_me()
            tgbot.get_me()
            NandeBot.uid = tgbot.uid = utils.get_peer_id(NandeBot.me)
            if Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(NandeBot.me)
            if NandeBot:
                cekbot.send_message(PRIVATE, THON_ON.format(NandeBot.me.username, version.__version__, cmdhr))
        except Exception as e:
            LOGS.error(f"STRING_SESSION - {str(e)}")
            sys.exit()


    if Var.STRING_SESSION2:
        try:
            NandeBot2.start()
            delta = NandeBot2(functions.help.GetConfigRequest())
            for option in delta.dc_options:
                if option.ip_address == NandeBot2.session.server_address:
                    if NandeBot2.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {NandeBot2.session.dc_id}"
                            f" to {option.id}"
                        )
                    NandeBot2.session.set_dc(option.id, option.ip_address, option.port)
                    NandeBot2.session.save()
                    break
            NandeBot2.me = NandeBot2.get_me()
            tgbot.get_me()
            NandeBot2.uid = tgbot.uid = utils.get_peer_id(NandeBot2.me)
            if Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(NandeBot2.me)
            if NandeBot:
                cekbot.send_message(PRIVATE, THON_ON.format(NandeBot.me.username, version.__version__, cmdhr))
        except Exception as e:
            LOGS.error(f"STRING_SESSION - {str(e)}")
            sys.exit()
     
    if Var.STRING_SESSION3:
        try:
            NandeBot3.start()
            delta = NandeBot3(functions.help.GetConfigRequest())
            for option in delta.dc_options:
                if option.ip_address == NandeBot3.session.server_address:
                    if NandeBot3.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {NandeBot3.session.dc_id}"
                            f" to {option.id}"
                        )
                    NandeBot3.session.set_dc(option.id, option.ip_address, option.port)
                    NandeBot3.session.save()
                    break
            NandeBot3.me = NandeBot3.get_me()
            tgbot.get_me()
            NandeBot3.uid = tgbot.uid = utils.get_peer_id(NandeBot.me)
            if Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(NandeBot3.me)
            if NandeBot:
                cekbot.send_message(PRIVATE, THON_ON.format(NandeBot.me.username, version.__version__, cmdhr))
        except Exception as e:
            LOGS.error(f"STRING_SESSION - {str(e)}")
            sys.exit()


def Pyrogram():
    if pyrotgbot:
        pyrotgbot.start()
        pyrotgbot.me = pyrotgbot.get_me()
        assistant_mods = plugin_collecter("./userbot/modules/pyrogram/assistant/")
        for mods in assistant_mods:
            try:
                load_modulesPyro(mods, assistant=True)
            except Exception as e:
                logging.error("[ASSISTANT] - Failed To Load : " + f"{mods} - {str(e)}")
    if pyrobot:
        pyrobot.start()
        pyrobot.me = pyrobot.get_me()
        pyrobot.has_a_bot = True if pyrotgbot else False
    if pyrobot2:
        pyrobot2.start()
        pyrobot2.me = pyrobot2.get_me()
        pyrobot2.has_a_bot = True if pyrotgbot else False
    if pyrobot3:
        pyrobot3.start()
        pyrobot3.me = pyrobot3.get_me()
        pyrobot3.has_a_bot = True if pyrotgbot else False
    if pyrobot4:
        pyrobot4.start()
        pyrobot.me = pyrobot4.get_me()
        pyrobot4.has_a_bot = True if pyrotgbot else False
    needed_mods = plugin_collecter("./userbot/modules/pyrogram/")
    for nm in needed_mods:
        try:
            load_modulesPyro(nm)
        except Exception as e:
            logging.error("[USER] - Failed To Load : " + f"{nm} - {str(e)}")
    if pyrobot:
        pyrobot.join_chat("suportNande")
        pyrobot.join_chat("Nandesupport")
        pyrobot.send_message(PRIVATE, MSG_ON.format(pyrobot.me.username, pyrover, cmdhr))
    if pyrobot2:
        pyrobot2.join_chat("suportNande")
        pyrobot2.join_chat("Nandesupport")
        pyrobot2.send_message(PRIVATE, MSG_ON.format(pyrobot2.me.username, pyrover, cmdhr))
    if pyrobot3:
        pyrobot3.join_chat("suportNande")
        pyrobot3.join_chat("Nandesupport")
        pyrobot3.send_message(PRIVATE, MSG_ON.format(pyrobot3.me.username, pyrover, cmdhr))
    if pyrobot4:
        pyrobot4.join_chat("suportNande")
        pyrobot4.join_chat("Nandesupport")
        pyrobot4.send_message(PRIVATE, MSG_ON.format(pyrobot4.me.username, pyrover, cmdhr))
    LOGS.info(f"♤ 𝙽𝚊𝚗𝚍𝚎 - 𝚄𝚜𝚎𝚛𝚋𝚘𝚝 ♤\n✨ PyroVersion:{pyrover} [Telah Diaktifkan]")
    Nandepyro.idle()
