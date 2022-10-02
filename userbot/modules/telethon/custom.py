from urlextract import URLExtract

from . import nandeub
import logging

from ...Var import Config
from ..._misc.managers import edit_delete, edit_or_reply
from ...sql_helper.globals import addgvar, delgvar, gvarstatus

plugin_category = "plugins"
LOGS = logging.getLogger(__name__)
cmdhd = Config.COMMAND_HAND_LER
extractor = URLExtract()


@nandeub.sipuserbot_cmd(
    pattern="custom (pmpermit|pmblock|pmpic|NAME)$",
    command=("custom", plugin_category),
    info={
        "header": "To customize your Nande-Userbot.",
        "options": {
            "pmpermit": "To customize pmpermit text. ",
            "pmblock": "To customize pmpermit block message.",
            "pmpic": "To customize pmpermit pic. Reply to media url or text containing media.",
        },
        "custom": {
            "{mention}": "mention user",
            "{first}": "first name of user",
            "{last}": "last name of user",
            "{fullname}": "fullname of user",
            "{username}": "username of user",
            "{userid}": "userid of user",
            "{my_first}": "your first name",
            "{my_last}": "your last name ",
            "{my_fullname}": "your fullname",
            "{my_username}": "your username",
            "{my_mention}": "your mention",
            "{totalwarns}": "totalwarns",
            "{warns}": "warns",
            "{remwarns}": "remaining warns",
        },
        "usage": [
            "{tr}custom <option> reply",
        ],
    },
)
async def custom_nandeuserbot(event):
    "To customize your Nande-Userbot."
    reply = await event.get_reply_message()
    text = reply.text
    if not reply:
        return await edit_delete(event, "__Reply to custom text or url__")
    input_str = event.pattern_match.group(1)
    if input_str == "pmpermit":
        addgvar("pmpermit_txt", text)
    if input_str == "ALIVE_NAME":
        addgvar("ALIVE_NAME", text)
    if input_str == "pmblock":
        addgvar("pmblock", text)
    if input_str == "pmpic":
        urls = extractor.find_urls(reply.text)
        if not urls:
            return await edit_delete(event, "`the given link is not supported`", 5)
        addgvar("pmpermit_pic", urls[0])
    await edit_or_reply(event, f"__Your custom {input_str} has been updated__")


@nandeub.sipuserbot_cmd(
    pattern="delcustom (pmpermit|pmblock|pmpic|NAME)$",
    command=("delcustom", plugin_category),
    info={
        "header": "To delete costomization of your Nande-Userbot.",
        "options": {
            "pmpermit": "To delete custom pmpermit text",
            "pmblock": "To delete custom pmpermit block message",
            "pmpic": "To delete custom pmpermit pic.",
        },
        "usage": [
            "{tr}delcustom <option>",
        ],
    },
)
async def custom_nandeuserbot(event):
    "To delete costomization of your Nande-Userbot."
    input_str = event.pattern_match.group(1)
    if input_str == "pmpermit":
        if gvarstatus("pmpermit_txt") is None:
            return await edit_delete(event, "__You haven't customzied your pmpermit.__")
        delgvar("pmpermit_txt")
    if input_str == "pmblock":
        if gvarstatus("pmblock") is None:
            return await edit_delete(event, "__You haven't customzied your pmblock.__")
        delgvar("pmblock")
    if input_str == "NAME":
        if gvarstatus("NAME") is None:
            return await edit_delete(event, "__You haven't customzied your NAME.__")
        delgvar("NAME")
    if input_str == "pmpic":
        if gvarstatus("pmpermit_pic") is None:
            return await edit_delete(event, "__You haven't customzied your pmpic.__")
        delgvar("pmpermit_pic")
    await edit_or_reply(
        event, f"__Succesfully deleted your customization of {input_str}.__"
    )
