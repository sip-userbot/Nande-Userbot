import asyncio
from datetime import datetime

from ... import nandeub
from . import mention
from ..._misc.managers import edit_or_reply

plugin_category = "plugins"


@nandeub.sipuserbot_cmd(
    pattern="ping( -a|$)",
    command=("ping", plugin_category),
    info={
        "header": "check how long it takes to ping your userbot",
        "flags": {"-a": "average ping"},
        "usage": ["{tr}ping", "{tr}ping -a"],
    },
)
async def _(event):
    "To check ping"
    flag = event.pattern_match.group(1)
    start = datetime.now()
    if flag == " -a":
        await edit_or_reply(event, "`!....`")
        await asyncio.sleep(0.3)
        await nandeevent.edit("`πΆ`")
        await asyncio.sleep(0.3)
        await nandeevent.edit("`π`")
        end = datetime.now()
        tms = (end - start).microseconds / 1000
        ms = round((tms - 0.6) / 3, 3)
        await nandeevent.edit(f"π£πΆπ»π΄\n`{ms} ms`")
    else:
        await edit_or_reply(event, "β€")
        await nandeevent.edit("β€β€")
        await nandeevent.edit("β€β€β€")
        await nandeevent.edit("β€β€β€β€")
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await nandeevent.edit(
            f" β€ π½ππππ - πππππππ β€\n"
            f" β€ π£πΆπ»π΄`{ms} ms`\n"
            f" β€ π’ππ»π²πΏπ: {mention} "
        )
