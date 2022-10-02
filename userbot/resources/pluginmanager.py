import importlib
import sys
from pathlib import Path

from .. import CMD_HELP, LOAD_PLUG
from ..Var import Config
from .._misc import LOADED_CMDS, PLG_INFO
from .._misc.logger import logging
from .._misc.managers import edit_delete, edit_or_reply
from .._misc.session import tgbot, NandeBot
from ..helpers.tools import media_type
from ..helpers.utils import _format, _nandetools, _nandeutils, install_pip, reply_id
from .decorators import admin_cmd, sudo_cmd

LOGS = logging.getLogger("NandeUserbot")


def load_module(shortname, plugin_path=None):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"userbot/modules/{shortname}.py")
        name = "userbot.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Successfully imported " + shortname)
    else:
        if plugin_path is None:
            path = Path(f"userbot/modules/{shortname}.py")
            name = f"userbot.modules.{shortname}"
        else:
            path = Path((f"{plugin_path}/{shortname}.py"))
            name = f"{plugin_path}/{shortname}".replace("/", ".")
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = NandeBot
        mod.vcClient = NandeBot
        mod.LOGS = LOGS
        mod.Config = Config
        mod._format = _format
        mod.tgbot = tgbot
        mod.Stark = tgbot
        mod.asst = tgbot
        mod.sudo_cmd = sudo_cmd
        mod.CMD_HELP = CMD_HELP
        mod.reply_id = reply_id
        mod.admin_cmd = admin_cmd
        mod._nandeutils = _nandeutils
        mod._nandetools = _nandetools
        mod.media_type = media_type
        mod.edit_delete = edit_delete
        mod.install_pip = install_pip
        mod.parse_pre = _format.parse_pre
        mod.edit_or_reply = edit_or_reply
        mod.logger = logging.getLogger(shortname)
        mod.borg = NandeBot
        mod.petercordnande_bot = NandeBot
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["userbot.modules." + shortname] = mod
        LOGS.info("Successfully imported " + shortname)


def remove_plugin(shortname):
    try:
        cmd = []
        if shortname in PLG_INFO:
            cmd += PLG_INFO[shortname]
        else:
            cmd = [shortname]
        for cmdname in cmd:
            if cmdname in LOADED_CMDS:
                for i in LOADED_CMDS[cmdname]:
                    NandeBot.remove_event_handler(i)
                del LOADED_CMDS[cmdname]
        return True
    except Exception as e:
        LOGS.error(e)
    with contextlib.suppress(BaseException):
        for i in LOAD_PLUG[shortname]:
            NandeBot.remove_event_handler(i)
        del LOAD_PLUG[shortname]
    try:
        name = f"userbot.modules.telethon.{shortname}"
        for i in reversed(range(len(NandeBot._event_builders))):
            ev, cb = NandeBot._event_builders[i]
            if cb.__module__ == name:
                del NandeBot._event_builders[i]
    except BaseException as exc:
        raise ValueError from exc


def checkplugins(filename):
    with open(filename, "r") as f:
        filedata = f.read()
    filedata = filedata.replace("sendmessage", "send_message")
    filedata = filedata.replace("sendfile", "send_file")
    filedata = filedata.replace("editmessage", "edit_message")
    with open(filename, "w") as f:
        f.write(filedata)
