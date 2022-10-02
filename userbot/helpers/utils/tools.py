import os
from typing import Optional

from moviepy.editor import VideoFileClip
from PIL import Image

import logging
from ..._misc.managers import edit_or_reply
from ..tools import media_type
from .utils import runcmd

LOGS = logging.getLogger(__name__)


async def media_to_pic(event, reply, noedits=False):
    mediatype = media_type(reply)
    if mediatype not in [
        "Photo",
        "Round Video",
        "Gif",
        "Sticker",
        "Video",
        "Voice",
        "Audio",
        "Document",
    ]:
        return event, None
    if not noedits:
        nandeevent = await edit_or_reply(
            event, f"`Transfiguration Time! Converting to ....`"
        )
    else:
        nandeevent = event
    nandemedia = None
    nandefile = os.path.join("./temp/", "meme.png")
    if os.path.exists(nandefile):
        os.remove(nandefile)
    if mediatype == "Photo":
        nandemedia = await reply.download_media(file="./temp")
        im = Image.open(nandemedia)
        im.save(nandefile)
    elif mediatype in ["Audio", "Voice"]:
        await event.client.download_media(reply, nandefile, thumb=-1)
    elif mediatype == "Sticker":
        nandemedia = await reply.download_media(file="./temp")
        if nandemedia.endswith(".tgs"):
            await runcmd(
                f"lottie_convert.py --frame 0 -if lottie -of png '{nandemedia}' '{nandefile}'"
            )
        elif nandemedia.endswith(".webp"):
            im = Image.open(nandemedia)
            im.save(nandefile)
    elif mediatype in ["Round Video", "Video", "Gif"]:
        await event.client.download_media(reply, nandefile, thumb=-1)
        if not os.path.exists(nandefile):
            nandemedia = await reply.download_media(file="./temp")
            clip = VideoFileClip(media)
            try:
                clip = clip.save_frame(nandefile, 0.1)
            except:
                clip = clip.save_frame(nandefile, 0)
    elif mediatype == "Document":
        mimetype = reply.document.mime_type
        mtype = mimetype.split("/")
        if mtype[0].lower() == "image":
            nandemedia = await reply.download_media(file="./temp")
            im = Image.open(nandemedia)
            im.save(nandefile)
    if nandemedia and os.path.exists(nandemedia):
        os.remove(nandemedia)
    if os.path.exists(nandefile):
        return nandeevent, nandefile, mediatype
    return nandeevent, None


async def take_screen_shot(
    video_file: str, duration: int, path: str = ""
) -> Optional[str]:
    thumb_image_path = path or os.path.join(
        "./temp/", f"{os.path.basename(video_file)}.jpg"
    )
    command = f"ffmpeg -ss {duration} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        LOGS.error(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None
