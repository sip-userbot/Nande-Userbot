
from . import nandeub

from . import edit_or_reply

plugin_category = "plugins"

# ===========================================================================================
S = (
    "..... (¯`v´¯)♥️\n"
    ".......•.¸.•´\n"
    "....¸.•´  🅷🅸\n"
    "... (   BABYy\n"
    "☻/ \n"
    "/▌✿🌷✿\n"
    "/ \     \|/\n"
)



D = (
    "░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄\n"
    "░███████████████████████ \n"
    "░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤ \n"
    "░▀░▐▓▓▓▓▓▓▌▀█░░░█▀░\n"
    "░░░▓▓▓▓▓▓█▄▄▄▄▄█▀░░\n"
    "░░█▓▓▓▓▓▌░░░░░░░░░░\n"
    "░▐█▓▓▓▓▓░░░░░░░░░░░\n"
    "░▐██████▌░░░░░░░░░░\n"
)


U = (
    "🌙.     *       ☄️      \n"
    "🌟   .  *       .         \n"
    "                       *   .      🛰     .        ✨      *\n"
    "  .     *   SLEEP WELL        🚀     \n"
    "      .              . . SWEET DREAMS 🌙\n"
    ". *       🌏 GOOD NIGHT         *\n"
    "                     🌙.     *       ☄️      \n"
    "🌟   .  *       .         \n"
    "                       *   .      🛰     .        ✨      *\n"
)

W = (
    "G🌷o🍃o🌷D\n"
    "M🍃o🌷r🍃N🌷i🍃N🌷g\n"
    "            \n"
    "No matter how good or \n"
    "bad your life is,\n"
    "wake up each morning\n"
    "and be thankful.\n"
    "You still have a new day.\n"
    "        \n"
    "🌞   \n"
    "         \n"
    "╱◥████◣\n"
    "│田│▓ ∩ │◥███◣\n"
    "╱◥◣ ◥████◣田∩田│\n"
    "│╱◥█◣║∩∩∩ 田∩田│\n"
    "║◥███◣∩田∩ 田∩田│\n"
    "│∩│ ▓ ║∩田│║▓田▓\n"
    "🌹🌷🌹🌷🌹🍃🌷🌹🌷🌹\n"
)

X = (
    ".......🦋🦋........🦋🦋\n"
    "...🦋.........🦋🦋.......🦋\n"
    "...🦋............💙..........🦋\n"
    ".....🦋🅣🅗🅐🅝🅚🅢 🦋\n"
    "....... 🦋.................🦋\n"
    "..............🦋......🦋\n"
    "...................💙\n"
)
# =========================================================================================


@nandeub.sipuserbot_cmd(
    pattern="baby$",
    command=("baby", plugin_category),
    info={
        "header": "Hi Baby art",
        "usage": "{tr}baby",
    },
)
async def baby(event):
    "Hi Baby art."
    await edit_or_reply(event, S)

@nandeub.sipuserbot_cmd(
    pattern="pistol$",
    command=("pistol", plugin_category),
    info={
        "header": "Pistol art",
        "usage": "{tr}pistol",
    },
)
async def baby(event):
    "pistol art."
    await edit_or_reply(event, D)

@nandeub.sipuserbot_cmd(
    pattern="hbd(?: |$)(.*)",
    command=("hbd", plugin_category),
    info={
        "header": "Happy birthday art.",
        "usage": "{tr}hbd <text>",
    },
)
async def hbd(event):
    inpt = event.pattern_match.group(1)
    text = f"**♥️{inpt}♥️**"
    if not inpt:
        text = ""
    "Happy birthday art."
    await edit_or_reply(
        event,
        f"▃▃▃▃▃▃▃▃▃▃▃\n┊ ┊ ┊ ┊ ┊ ┊\n┊ ┊ ┊ ┊ ˚✩ ⋆｡˚ ✩\n┊ ┊ ┊ ✫\n┊ ┊ ✧🎂🍰🍫🍭\n┊ ┊ ✯\n┊ . ˚ ˚✩\n........♥️♥️..........♥️♥️\n.....♥️........♥️..♥️........♥️\n...♥️.............♥️............♥️\n......♥️.....Happy.......♥️__\n...........♥️..............♥️__\n................♥️.....♥️__\n......................♥️__\n...............♥️......♥️__\n..........♥️...............♥️__\n.......♥️..Birthday....♥️\n.....♥️..........♥️..........♥️__\n.....♥️.......♥️_♥️.......♥️__\n.........♥️♥️........♥️♥️.....\n.............................................\n..... (¯`v´¯)♥️\n.......•.¸.•´STAY BLESSED\n....¸.•´      LOVE&FUN\n... (   YOU DESERVE\n☻/ THEM A LOT\n/▌✿🌷✿\n/ \     \|/\n▃▃▃▃▃▃▃▃▃▃▃\n\n{text}",
    )


@nandeub.sipuserbot_cmd(
    pattern="thanks$",
    command=("thanks", plugin_category),
    info={
        "header": "Thanks art.",
        "usage": "{tr}thanks",
    },
)
async def gn(event):
    "Thanks art."
    await edit_or_reply(event, X)



@nandeub.sipuserbot_cmd(
    pattern="gmg$",
    command=("gmg", plugin_category),
    info={
        "header": "Good morning art.",
        "usage": "{tr}gmg",
    },
)
async def gm(event):
    "Good morning art."
    await edit_or_reply(
        event,
        "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･\n╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮\n╭━┳━┳━┳╯┃╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n┣╮┣━┻━┻━╯╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･",
    )


@nandeub.sipuserbot_cmd(
    pattern="gmg2$",
    command=("gmg2", plugin_category),
    info={
        "header": "Good morning art.",
        "usage": "{tr}gmg2",
    },
)
async def gm(event):
    "Good morning art."
    await edit_or_reply(
        event,
        "♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n╔══╗────╔╗──────────╔╗\n║╔═╬═╦═╦╝║╔══╦═╦╦╦═╦╬╬═╦╦═╗\n║╚╗║╬║╬║╬║║║║║╬║╔╣║║║║║║║╬║\n╚══╩═╩═╩═╝╚╩╩╩═╩╝╚╩═╩╩╩═╬╗║\n────────────────────────╚═╝\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･",
    )


@nandeub.sipuserbot_cmd(
    pattern="gmg3$",
    command=("gmg3", plugin_category),
    info={
        "header": "Good morning art.",
        "usage": "{tr}gmg3",
    },
)
async def gm(event):
    "Good morning art."
    await edit_or_reply(event, W)


@nandeub.sipuserbot_cmd(
    pattern="gnt$",
    command=("gnt", plugin_category),
    info={
        "header": "Good night art.",
        "usage": "{tr}gnt",
    },
)
async def gn(event):
    "Good night art."
    await edit_or_reply(
        event,
        "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･\n╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮\n╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫\n┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯\n╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥° ♥｡･ﾟ♡ﾟ･",
    )


@nandeub.sipuserbot_cmd(
    pattern="gnt2$",
    command=("gnt2", plugin_category),
    info={
        "header": "Good night art.",
        "usage": "{tr}gnt2",
    },
)
async def gn(event):
    "Good night art."
    await edit_or_reply(
        event,
        "♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n╔══╗────╔╗╔═╦╦╗─╔╗╔╗\n║╔═╬═╦═╦╝║║║║╠╬═╣╚╣╚╗\n║╚╗║╬║╬║╬║║║║║║╬║║║╔╣\n╚══╩═╩═╩═╝╚╩═╩╬╗╠╩╩═╝\n──────────────╚═╝\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･",
    )


@nandeub.sipuserbot_cmd(
    pattern="gnt3$",
    command=("gnt3", plugin_category),
    info={
        "header": "Good morning art.",
        "usage": "{tr}gnt3",
    },
)
async def gn(event):
    "Good night art."
    await edit_or_reply(event, U)


# @PhycoNinja13b 's Part begin from here


@nandeub.sipuserbot_cmd(
    pattern="hi(?: |$)(.*)",
    command=("hi", plugin_category),
    info={
        "header": "Hi text art.",
        "usage": [
            "{tr}hi <emoji>",
            "{tr}hi",
        ],
    },
)
async def hi(event):
    "Hi text art."
    giveVar = event.text
    nande = giveVar[4:5]
    if not nande:
        nande = "🌺"
    await edit_or_reply(
        event,
        f"{nande}✨✨{nande}✨{nande}{nande}{nande}\n{nande}✨✨{nande}✨✨{nande}✨\n{nande}{nande}{nande}{nande}✨✨{nande}✨\n{nande}✨✨{nande}✨✨{nande}✨\n{nande}✨✨{nande}✨{nande}{nande}{nande}\n☁☁☁☁☁☁☁☁",
    )


@nandeub.sipuserbot_cmd(
    pattern="cheer$",
    command=("cheer", plugin_category),
    info={
        "header": "Cheer text art.",
        "usage": "{tr}cheer",
    },
)
async def cheer(event):
    "cheer text art."
    await edit_or_reply(
        event,
        "💐💐😉😊💐💐\n☕ Cheer Up  🍵\n🍂 ✨ )) ✨  🍂\n🍂┃ (( * ┣┓ 🍂\n🍂┃*💗 ┣┛ 🍂 \n🍂┗━━┛  🍂🎂 For YOU  🍰\n💐💐😌😚💐💐",
    )


@nandeub.sipuserbot_cmd(
    pattern="getwell$",
    command=("getwell", plugin_category),
    info={
        "header": "Get Well art.",
        "usage": "{tr}getwell",
    },
)
async def getwell(event):
    "Get Well art."
    await edit_or_reply(
        event, "🌹🌹🌹🌹🌹🌹🌹🌹 \n🌹😷😢😓😷😢💨🌹\n🌹💝💉🍵💊💐💝🌹\n🌹 GetBetter Soon! 🌹\n🌹🌹🌹🌹🌹🌹🌹🌹"
    )


@nandeub.sipuserbot_cmd(
    pattern="luck$",
    command=("luck", plugin_category),
    info={
        "header": "luck art.",
        "usage": "{tr}luck",
    },
)
async def luck(event):
    "Luck art."
    await edit_or_reply(
        event, "💚~🍀🍀🍀🍀🍀\n🍀╔╗╔╗╔╗╦╗✨🍀\n🍀║╦║║║║║║👍🍀\n🍀╚╝╚╝╚╝╩╝。 🍀\n🍀・・ⓁⓊⒸⓀ🍀\n🍀🍀🍀 to you💚"
    )


@nandeub.sipuserbot_cmd(
    pattern="sprinkle$",
    command=("sprinkle", plugin_category),
    info={
        "header": "sprinkle art.",
        "usage": "{tr}sprinkle",
    },
)
async def sprinkle(event):
    "Sprinkle text art."
    await edit_or_reply(
        event,
        "✨.•*¨*.¸.•*¨*.¸¸.•*¨*• ƸӜƷ\n🌸🌺🌸🌺🌸🌺🌸🌺\n Sprinkled with love❤\n🌷🌻🌷🌻🌷🌻🌷🌻\n ¨*.¸.•*¨*. ¸.•*¨*.¸¸.•*¨`*•.✨\n🌹🍀🌹🍀🌹🍀🌹🍀",
    )
