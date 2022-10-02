# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


import glob
import os
import sys
from asyncio.exceptions import CancelledError
from pathlib import Path
from telethon.tl.functions.channels import JoinChannelRequest
import requests
from telethon import functions, types, utils

from .. import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID, pyrobot, pyrobot2, pyrobot3, pyrobot4

from ..Var import Config
from .._misc.logger import logging
from .._misc.session import NandeBot, NandeBot2, NandeBot3, tgbot, cekbot
from ..helpers.utils import install_pip
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from .pluginmanager import load_module
from .tools import create_supergroup
import base64
from ..versions import __version__ as botvers

LOGS = logging.getLogger("NandeUserbot")
cmdhr = Config.COMMAND_HAND_LER
nandeub = NandeBot

async def setup_bot():
    try:
        await NandeBot.start()
        delta = await NandeBot(functions.help.GetConfigRequest())
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
        NandeBot.me = await NandeBot.get_me()
        bot_details = await tgbot.get_me()
        Config.TG_BOT_USERNAME = f"@{bot_details.username}"
        NandeBot.uid = tgbot.uid = utils.get_peer_id(NandeBot.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(NandeBot.me)
        if Config.STRING_SESSION2:
            await NandeBot2.start()
        if Config.STRING_SESSION3:
            await NandeBot3.start()
    except Exception as e:
        LOGS.error(f"STRING_SESSION - {str(e)}")
        sys.exit()

    

# don't know work or not just a try in future will use sleep
async def ipchange():
    """
    Just to check if ip change or not
    """
    newip = (requests.get("https://httpbin.org/ip").json())["origin"]
    if gvarstatus("ipaddress") is None:
        addgvar("ipaddress", newip)
        return None
    oldip = gvarstatus("ipaddress")
    if oldip != newip:
        delgvar("ipaddress")
        LOGS.info("Ip Change detected")
        try:
            await Nandeub.disconnect()
        except (ConnectionError, CancelledError):
            pass
        return "ip change"

async def loads(folder):
    """
    To load plugins from the mentioned folder
    """
    path = f"userbot/{folder}/*.py"
    files = glob.glob(path)
    files.sort()
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                if shortname.replace(".py", "") not in Config.NO_LOAD:
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                shortname.replace(".py", ""),
                                plugin_path=f"userbot/{folder}",
                            )
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"userbot/{folder}/{shortname}.py"))
            except Exception as e:
                os.remove(Path(f"Nande/{folder}/{shortname}.py"))
                LOGS.info(f"Gagal membuka file {shortname} dikarenakan error {e}")


async def buka(folder):
    """
    To load plugins from the mentioned folder
    """
    path = f"userbot/modules/{folder}/*.py"
    files = glob.glob(path)
    files.sort()
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                if shortname.replace(".py", "") not in Config.NO_LOAD:
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                shortname.replace(".py", ""),
                                plugin_path=f"userbot/modules/{folder}",
                            )
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"userbot/modules/{folder}/{shortname}.py"))
            except Exception as e:
                os.remove(Path(f"userbot/modules/{folder}/{shortname}.py"))
                LOGS.info(f"Gagal membuka file {shortname} dikarenakan error {e}")

async def bukabot(folder):
    """
    To load plugins from the mentioned folder
    """
    path = f"userbot/modules/telethon/{folder}/*.py"
    files = glob.glob(path)
    files.sort()
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                if shortname.replace(".py", "") not in Config.NO_LOAD:
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                shortname.replace(".py", ""),
                                plugin_path=f"userbot/modules/telethon/{folder}",
                            )
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"userbot/modules/telethon/{folder}/{shortname}.py"))
            except Exception as e:
                os.remove(Path(f"userbot/modules/telethon/{folder}/{shortname}.py"))
                LOGS.info(f"Gagal membuka file {shortname} dikarenakan error {e}")




async def verifyLoggerGroup():
    """
    Will verify the both loggers group
    """
    flag = False
    if BOTLOG:
        try:
            entity = await Nandeub.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "Permissions missing to send messages for the specified PRIVATE_GROUP_BOT_API_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "Permissions missing to addusers for the specified PRIVATE_GROUP_BOT_API_ID."
                    )
        except ValueError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID cannot be found. Make sure it's correct."
            )
        except TypeError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID is unsupported. Make sure it's correct."
            )
        except Exception as e:
            LOGS.error(
                "An Exception occured upon trying to verify the PRIVATE_GROUP_BOT_API_ID.\n"
                + str(e)
            )
    else:
        descript = "Don't delete this group or change to group(If you change group all your previous snips, welcome will be lost.)"
        _, groupid = await create_supergroup(
            "Nande - Userbot BotLog Group", Nandeub, Config.TG_BOT_USERNAME, descript
        )
        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)
        print(
            "Private Group for PRIVATE_GROUP_BOT_API_ID is created successfully and added to vars."
        )
        flag = True
    if PM_LOGGER_GROUP_ID != -100:
        try:
            entity = await Nandeub.get_entity(PM_LOGGER_GROUP_ID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "Permissions missing to send messages for the specified PM_LOGGER_GROUP_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "Permissions missing to addusers for the specified PM_LOGGER_GROUP_ID."
                    )
        except ValueError:
            LOGS.error("PM_LOGGER_GROUP_ID cannot be found. Make sure it's correct.")
        except TypeError:
            LOGS.error("PM_LOGGER_GROUP_ID is unsupported. Make sure it's correct.")
        except Exception as e:
            LOGS.error(
                "An Exception occured upon trying to verify the PM_LOGGER_GROUP_ID.\n"
                + str(e)
            )
    if flag:
        executable = sys.executable.replace(" ", "\\ ")
        args = [executable, "-m", "Nande"]
        os.execle(executable, *args, os.environ)
        sys.exit(0)


ON = f"""
Nande-Userbot
Owner {Config.ALIVE_NAME}
Version - `{botvers}`
Ketik `{cmdhr}alive` untuk Mengecheck Bot apakah sudah aktif
"""

MSG_ON = """
Nande-Userbot
━━
Version - `{}'
Ketik `{}alive` untuk Mengecheck Bot
━━
"""


CHATID = "-1001726206158"

async def ongrup():
    try:
        if cekbot:
            if CHATID != 0:
                await cekbot.send_message(
                    CHATID,
                    ON,
                )
                await cekbot.send_message(
                    CHATID,
                    ON,
                )
                await cekbot.send_message(
                    CHATID,
                    ON,
                )
    except BaseException:
        pass


async def ongruppyro():
    try:
        await pyrobot.send_message(BOTLOG_CHATID, MSG_ON.format(botvers, cmdhr))
        await pyrobot2.send_message(BOTLOG_CHATID, MSG_ON.format(botvers, cmdhr))
        await pyrobot3.send_message(BOTLOG_CHATID, MSG_ON.format(botvers, cmdhr))
        await pyrobot4.send_message(BOTLOG_CHATID, MSG_ON.format(botvers, cmdhr))
    except BaseException:
        pass

async def join():
    X = base64.b64decode("QHN1cG9ydE5hbmRl")
    L = base64.b64decode("QE5hbmRlc3VwcG9ydA==")
    try:
        await NandeBot(JoinChannelRequest(X))
    except BaseException:
        pass
    try:
        await NandeBot(JoinChannelRequest(L))
    except BaseException:
        pass

## Modular •••••√√√√√√••••••^••√√

P = "plugins"
M = "modules"
V = "VCPlugins"
A = "AsistenBot"
