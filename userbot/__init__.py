# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


from telethon.sync import TelegramClient, custom, events
from .sql_helper.globals import addgvar, delgvar, gvarstatus
import heroku3
from redis import StrictRedis

import sys
import os
from .Var import *
from ._database import DatabaseCute
DB = DatabaseCute()
SqL = DB
import time
from .Session import *
from .versions import __version__
import logging
from .versions import __version__, __license__, __author__, __copyright__
from ._misc.client import dual_duall


DEVLIST = [5057493677, 2062364017]
DEVS = DEVLIST
LOGS = logging.getLogger("NandeUserbot")
loop = None

__version__ = __version__
__license__ = __license__ 
__author__ = __author__
__copyright__ = __copyright__

LOGS.info(f"Memeriksa {DB.name}...")
LOGS.info(f"Terkoneksi {DB.name} Successfully!")

nandeversion = __version__
StartTime = time.time()
BOT_MODE = SqL.getdb("MODE_DUAL")
DUAL_MODE = SqL.getdb("DUAL_MODE")
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
TG_BOT_USERNAME = os.environ.get("TG_BOT_USERNAME", None)
LOG_CHANNEL = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID") or 0)


"""
if not BOT_TOKEN:
    from .helpers.functions.auto import autobot

    if NandeBot:
        NandeBot.loop.run_until_complete(autobot())
else:
    BOT_TOKEN = None
    if not SqL.getdb("BOT_TOKEN") and BOT_TOKEN:
        SqL.setdb("BOT_TOKEN", BOT_TOKEN)
    if not SqL.getdb("BOT_TOKEN"):
        LOGS.info('"BOT_TOKEN" not Found! Please add it, in order to use "MODE BoT"')
        import sys

        sys_exit()
"""

if BOT_MODE:
    tgbot = tgbot
    NandeBot = tgbot
 

bot = NandeBot
nandeub = NandeBot
botvc = NandeBot
Stark = NandeBot
petercordnande_bot = nandeub

def dual_mode():
    try:
        if SqL.getdb("DUAL_MODE") is not None:
            mode = SqL.setdb("DUAL_MODE", "DUAL") or "DUAL"
            return mode
        else:
            mode = SqL.setdb("DUAL_MODE", "False")
            return mode
    except Exception as e:
        print(f"{str(e)}")
        sys.exit()



from .Var import Config


if Config.UPSTREAM_REPO == "NANDE_USERBOT":
    UPSTREAM_REPO_URL = "https://github.com/sip-userbot/Nande-Userbot"
else:
    UPSTREAM_REPO_URL = Config.UPSTREAM_REPO


if Config.PRIVATE_GROUP_BOT_API_ID == 0:
    if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is None:
        Config.BOTLOG = False
        Config.BOTLOG_CHATID = "me"
    else:
        Config.BOTLOG_CHATID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))
        Config.PRIVATE_GROUP_BOT_API_ID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))
        Config.BOTLOG = True
else:
    if str(Config.PRIVATE_GROUP_BOT_API_ID)[0] != "-":
        Config.BOTLOG_CHATID = int("-" + str(Config.PRIVATE_GROUP_BOT_API_ID))
    else:
        Config.BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID
    Config.BOTLOG = True

if Config.PM_LOGGER_GROUP_ID == 0:
    if gvarstatus("PM_LOGGER_GROUP_ID") is None:
        Config.PM_LOGGER_GROUP_ID = -100
    else:
        Config.PM_LOGGER_GROUP_ID = int(gvarstatus("PM_LOGGER_GROUP_ID"))
elif str(Config.PM_LOGGER_GROUP_ID)[0] != "-":
    Config.PM_LOGGER_GROUP_ID = int("-" + str(Config.PM_LOGGER_GROUP_ID))

try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except Exception:
    HEROKU_APP = None

LOGSPAMMER = os.environ.get("LOGSPAMMER", "False")


class Auto(object):
    LOGGER = True

    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    
Gblacklist = [-1001159103924, -1001718757023]

# Global Configiables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
XTRA_CMD_LIST = {}
ISAFK = False
AFKREASON = None
CMD_LIST = {}
SUDO_LIST = {}
AFF_LIST = {}
# for later purposes
INT_PLUG = ""
LOAD_PLUG = {}


# Variables
BOTLOG = Config.BOTLOG
BOTLOG_CHATID = Config.BOTLOG_CHATID
PM_LOGGER_GROUP_ID = Config.PM_LOGGER_GROUP_ID

def where_hosted():
    if os.getenv("DYNO"):
        return "heroku"
