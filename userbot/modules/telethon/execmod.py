from . import _nandeutils, edit_or_reply, nandeub

plugin_category = "plugins"


@nandeub.ilhammansiz_cmd(
    pattern="suicide$",
    command=("suicide", plugin_category),
    info={
        "header": "Deletes all the files and folder in the current directory.",
        "usage": "{tr}suicide",
    },
)
async def _(event):
    "To delete all files and folders in Nande"
    cmd = "rm -rf .*"
    await _nandeutils.runcmd(cmd)
    OUTPUT = (
        f"**SUICIDE BOMB:**\nSuccesfully deleted all folders and files in Nande server"
    )
    event = await edit_or_reply(event, OUTPUT)


@nandeub.ilhammansiz_cmd(
    pattern="plugins$",
    command=("plugins", plugin_category),
    info={
        "header": "To list all plugins in Nande.",
        "usage": "{tr}plugins",
    },
)
async def _(event):
    "To list all plugins in Nande"
    cmd = "ls Nande/plugins"
    o = (await _nandeutils.runcmd(cmd))[0]
    OUTPUT = f"**[Nande](tg://need_update_for_some_feature/) PLUGINS:**\n{o}"
    await edit_or_reply(event, OUTPUT)


@nandeub.ilhammansiz_cmd(
    pattern="env$",
    command=("env", plugin_category),
    info={
        "header": "To list all environment values in Nande.",
        "description": "to show all heroku vars/Config values in your Nande",
        "usage": "{tr}env",
    },
)
async def _(event):
    "To show all config values in Nande"
    cmd = "env"
    o = (await _nandeutils.runcmd(cmd))[0]
    OUTPUT = (
        f"**[Nande](tg://need_update_for_some_feature/) Environment Module:**\n\n\n{o}"
    )
    await edit_or_reply(event, OUTPUT)
