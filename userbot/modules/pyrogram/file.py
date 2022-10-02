# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••
 

import logging
import os
import pathlib
import shutil
import time
import uuid

import img2pdf


from userbot._func.decorators import Nande_cmd as sip-userbot_on_cmd
from userbot._func._helpers import (
    edit_or_reply,
    get_text,
    humanbytes,
    progress,
)

from . import HELP


HELP(
    "file",
)

@ilhammansiz_on_cmd(
    ["chnnlzip", "channelzip"],
    cmd_help={
        "help": "Zips All The Messages/Files/Everything From A Channel/Group",
        "example": "{ch}chnnlzip",
    },
)
async def chnnlzip(client, message):
    pablo = await edit_or_reply(message, "`Fetching All Files From This Channel!`")
    rndm = uuid.uuid4().hex
    un = get_text(message)
    dirz = f"./{rndm}/"
    media_count = 0
    text_count = 0
    os.makedirs(dirz)
    if un:
        chnnl = un
    else:
        chnnl = message.chat.id
    async for msg in client.search_messages(chnnl):
        if msg.sticker:
            rndmname = uuid.uuid4().hex
            if msg.sticker.mime_type == "application/x-tgsticker":
                file_name = os.path.join(dirz + rndmname + ".tgs")
            else:
                file_name = os.path.join(dirz + rndmname + ".wepb")
            try:
                await msg.download(file_name=file_name)
            except Exception as e:
                logging.info(e)
        elif msg.media:
            media_count += 1
            try:
                await msg.download(file_name=dirz)
            except Exception as e:
                logging.info(e)
        elif msg.text:
            text_count += 1
            f = open(os.path.join(dirz + f"{chnnl}.txt"), "a")
            f.write(f"[{msg.date}] - {msg.text} \n\n")
    total = text_count + media_count
    await pablo.edit(
        f"**Total Media :** `{total}` \n**Downloaded Media :** `{media_count}` \n**Total Texts Appended :** `{text_count}` \n**Now Zipping Files.**"
    )
    shutil.make_archive(str(chnnl), "zip", dirz)
    await pablo.edit("`Zipped! Uploading Now!`")
    zip_name = f"{chnnl}.zip"
    await client.send_document(
        message.chat.id,
        zip_name,
        caption=f"**Total :** `{total}` \n**Total Media :** `{media_count}` \n**Total Text :** `{text_count}`",
    )
    os.remove(zip_name)
    shutil.rmtree(dirz)


def file_list(path, lisT):
    pathlib.Path(path)
    for filepath in pathlib.Path(path).glob("**/*"):
        lisT.append(filepath.absolute())
    return lisT


@ilhammansiz_on_cmd(
    ["pdf", "channelpdf"],
    cmd_help={
        "help": "Makes A PDF With All Images In Group/Channel!",
        "example": "{ch}pdf",
    },
)
async def chnnlpdf(client, message):
    pablo = await edit_or_reply(message, "`Fetching All Images From This Channel!`")
    rndm = uuid.uuid4().hex
    un = get_text(message)
    dirz = f"./{rndm}/"
    photo_count = 0
    text_count = 0
    os.makedirs(dirz)
    if un:
        chnnl = un
    else:
        chnnl = message.chat.id
    async for msg in client.search_messages(chnnl, filter="photo"):
        rndmname = uuid.uuid4().hex
        file_name = os.path.join(dirz + rndmname + ".jpg")
        photo_count += 1
        try:
            await msg.download(file_name=file_name)
        except Exception as e:
            logging.info(e)
    text_count + photo_count
    images_path = []
    images_names = os.listdir(dirz)
    for i in images_names:
        path = os.path.join(dirz, i)
        images_path.append(path)
    if not images_path:
        await pablo.edit("`No Images Found!`")
        shutil.rmtree(dirz)
        return
    with open("imagetopdf@ilhammansiz188.pdf", "wb") as f:
        f.write(img2pdf.convert(images_path))
    capt = f"**CONVERTED** \n**Total Images :** `{len(images_path)}` \n**Channel / Group :** `{chnnl}`"
    await client.send_document(message.chat.id, "imagetopdf@ilhammansiz188.pdf", caption=capt)
    os.remove("imagetopdf@ilhammansiz188.pdf")
    shutil.rmtree(dirz)
    await pablo.delete()


@ilhammansiz_on_cmd(
    ["Download"],
    cmd_help={
        "help": "Downloads Replied File To Local Storage!",
        "example": "{ch}download (replying-to-file)",
    },
)
async def Download(client, message):
    pablo = await edit_or_reply(message, "`Processing...`")
    if not message.reply_to_message:
        await pablo.edit("`Reply To A File To Download!`")
        return
    if not message.reply_to_message.media:
        await pablo.edit("`Reply To A File To Download!`")
        return
    c_time = time.time()
    Escobar = await message.reply_to_message.download(
        progress=progress, progress_args=(pablo, c_time, f"`Downloading This File!`")
    )
    await pablo.edit(f"Downloaded to `{Escobar}` Successfully!")


@ilhammansiz_on_cmd(
    ["setthumb"],
    cmd_help={
        "help": "Set Thumbnail For Upload Files!",
        "example": "{ch}setthumb (Replying to thumbnail)",
    },
)
async def st(client, message):
    pablo = await edit_or_reply(message, "`Setting As Thumb!`")
    if not message.reply_to_message:
        await pablo.edit("`Reply To A Image To Set As Thumb For Uploading Files.!`")
        return
    if not message.reply_to_message.photo:
        await pablo.edit("`Reply To A Image To Set As Thumb For Uploading Files.!`")
        return
    await message.reply_to_message.download(file_name="./main_startup/Cache/thumb.jpg")
    await pablo.edit(
        f"`Yay! Custom Thumb Set, All Files Will Be Sent With This Thumb!`"
    )


image_ext = tuple([".jpg", ".png", ".jpeg"])
vid_ext = tuple([".mp4", ".mkv"])
sticker_ext = tuple([".wepb", ".tgs"])
song_ext = tuple([".mp3", ".wav", ".m4a"])


@ilhammansiz_on_cmd(
    ["Upload"],
    cmd_help={
        "help": "Upload Internal File!",
        "example": "{ch}upload (local file path)",
    },
)
async def upload(client, message):
    pablo = await edit_or_reply(message, "`Processing...")
    file = get_text(message)
    c_time = time.time()
    if not file:
        await pablo.edit(
            "`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`"
        )
        return
    if not os.path.exists(file):
        await pablo.edit("`404 : File Not Found.`")
        return
    file_name = os.path.basename(file)
    send_as_thumb = False
    if os.path.exists("./userbot/resources/thumb.jpg"):
        send_as_thumb = True
    size = os.stat(file).st_size
    if file.endswith(image_ext):
        # assume its image file
        capt = f"File Name : `{file_name}` \nFile Size : `{humanbytes(size)}` \nFile Type : `Image (Guessed)`"
        await client.send_photo(
            message.chat.id,
            file,
            caption=capt,
            progress=progress,
            progress_args=(pablo, c_time, f"`Uploading {file_name}!`", file_name),
        )
    elif file.endswith(vid_ext):
        capt = f"File Name : `{file_name}` \nFile Size : `{humanbytes(size)}` \nFile Type : `Video (Guessed)`"
        if send_as_thumb:
            await client.send_video(
                message.chat.id,
                file,
                thumb="./userbot/resources/thumb.jpg",
                caption=capt,
                progress=progress,
                progress_args=(pablo, c_time, f"`Uploading {file_name}!`", file_name),
            )
        else:
            await client.send_video(
                message.chat.id,
                file,
                caption=capt,
                progress=progress,
                progress_args=(pablo, c_time, f"`Uploading {file_name}!`", file_name),
            )
    elif file.endswith(".gif"):
        capt = f"File Name : `{file_name}` \nFile Size : `{humanbytes(size)}` \nFile Type : `Gif (Guessed)`"
        if send_as_thumb:
            await client.send_animation(
                message.chat.id,
                file,
                thumb="./userbot/resources/thumb.jpg",
                caption=capt,
                progress=progress,
                progress_args=(pablo, c_time, f"`Uploading {file_name}!`", file_name),
            )
        else:
            await client.send_animation(
                message.chat.id,
                file,
                caption=capt,
                progress=progress,
                progress_args=(pablo, c_time, f"`Uploading {file_name}!`", file_name),
            )
    elif file.endswith(song_ext):
        capt = f"File Name : `{file_name}` \nFile Size : `{humanbytes(size)}` \nFile Type : `Audio (Guessed)`"
        if send_as_thumb:
            await client.send_audio(
                message.chat.id,
                file,
                thumb="./userbot/resources/thumb.jpg",
                caption=capt,
                progress=progress,
                progress_args=(pablo, c_time, f"`Uploading {file_name}!`", file_name),
            )
        else:
            await client.send_audio(
                message.chat.id,
                file,
                caption=capt,
                progress=progress,
                progress_args=(pablo, c_time, f"`Uploading {file_name}!`", file_name),
            )
    elif file.endswith(sticker_ext):
        await client.send_sticker(
            message.chat.id,
            file,
            progress=progress,
            progress_args=(pablo, c_time, f"`Uploading {file_name}!`", file_name),
        )
    else:
        capt = f"File Name : `{file_name}` \nFile Size : `{humanbytes(size)}` \nFile Type : `Document (Guessed)`"
        if send_as_thumb:
            await client.send_document(
                message.chat.id,
                file,
                thumb="./userbot/resources/thumb.jpg",
                caption=capt,
                progress=progress,
                progress_args=(pablo, c_time, f"`Uploading {file_name}!`", file_name),
            )
        else:
            await client.send_document(
                message.chat.id,
                file,
                caption=capt,
                progress=progress,
                progress_args=(pablo, c_time, f"`Uploading {file_name}!`", file_name),
            )
    await pablo.delete()
