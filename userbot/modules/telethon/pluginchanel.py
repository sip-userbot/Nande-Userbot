import os
from pathlib import Path

from telethon.tl.types import InputMessagesFilterDocument

from ...Var import Config
from ...helpers.utils import install_pip
from ...resources import load_module
from . import BOTLOG, BOTLOG_CHATID, NandeBot

plugin_category = "modules"

if Config.PLUGIN_CHANNEL:

    async def install():
        documentss = await NandeBot.get_messages(
            Config.PLUGIN_CHANNEL, None, filter=InputMessagesFilterDocument
        )
        total = int(documentss.total)
        for module in range(total):
            plugin_to_install = documentss[module].id
            plugin_name = documentss[module].file.name
            if os.path.exists(f"userbot/modules/pyrogram/{plugin_name}"):
                return
            downloaded_file_name = await NandeBot.download_media(
                await NandeBot.get_messages(Config.PLUGIN_CHANNEL, ids=plugin_to_install),
                "Nande/plugins/",
            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            flag = True
            check = 0
            while flag:
                try:
                    load_module(shortname.replace(".py", ""))
                    break
                except ModuleNotFoundError as e:
                    install_pip(e.name)
                    check += 1
                    if check > 5:
                        break
            if BOTLOG:
                await NandeBot.send_message(
                    BOTLOG_CHATID,
                    f"Installed Plugin `{os.path.basename(downloaded_file_name)}` successfully.",
                )

    NandeBot.loop.create_task(install())
