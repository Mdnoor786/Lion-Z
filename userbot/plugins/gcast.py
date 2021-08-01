
import os

from telethon import events
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights

from . import *

plugin_category = "admin"

@lionub.lion_cmd(
  pattern="gcast ?(.*)",
  command=("gcast", plugin_category),
    info={
        "header": "global groups cast.",
        "description": "Use this command to global broadcast a message in all groups.",
        "usage": "{tr}gcast",
    },
)
async def gcast(event):
    if not event.out and not is_fullsudo(event.sender_id):
        return await edit_or_reply(event, "`This Command Is Sudo Restricted.`")
    xx = event.pattern_match.group(1)
    if not xx:
        return edit_or_reply(event, "`Give some text to Globally Broadcast`")
    tt = event.text
    msg = tt[6:]
    event = await edit_or_reply(event, "`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"Done in {done} chats, error in {er} chat(s)")


@lionub.lion_cmd(
  pattern="gucast ?(.*)",
  command=("gucast", plugin_category),
    info={
        "header": "global users cast.",
        "description": "Use this command to broadcast global message to all users only.",
        "usage": "{tr}gucast",
    },
)
async def gucast(event):
    if not event.out and not is_fullsudo(event.sender_id):
        return await edit_or_reply(event, "`This Command Is Sudo Restricted.`")
    xx = event.pattern_match.group(1)
    if not xx:
        return edit_or_reply(event, "`Give some text to Globally Broadcast`")
    tt = event.text
    msg = tt[7:]
    kk = await edit_or_reply(event, "`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"Done in {done} chats, error in {er} chat(s)")
