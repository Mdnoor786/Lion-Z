#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    """𝙿𝙻𝙴𝙰𝚂𝙴 𝙶𝙾 𝚃𝙾 my.telegram.org
𝙻𝙾𝙶𝙸𝙽 𝚄𝚂𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙰𝙲𝙲𝙾𝚄𝙽𝚃
𝙲𝙻𝙸𝙲𝙺 𝙾𝙽 𝙰𝙿𝙸 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙼𝙴𝙽𝚃 𝚃𝙾𝙾𝙻𝚂
𝙲𝚁𝙴𝙰𝚃𝙴 𝙰 𝙽𝙴𝚆 𝙰𝙿𝙿𝙻𝙸𝙲𝙰𝚃𝙸𝙾𝙽, 𝙱𝚈 𝙴𝙽𝚃𝙴𝚁𝙸𝙽𝙶 𝚁𝙴𝚀𝚄𝙸𝚁𝙴𝙳 𝙳𝙴𝚃𝙰𝙸𝙻𝚂
𝚃𝙴𝙰𝙼𝙻𝙸𝙾𝙽-Z
 _       _____   ____   _   _ _
| |     |_   _| / __ \\ | \\ | |
| |       | |  | |  | | |  \\| |
| |       | |  | |  | | | . \. |
| |____  _| |_ | |__| | | |\\  |
|______||_____| \\____/ |_| \\_|


Running Lion Fire Z 🔥🔥🔥🔥...."""
)
APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
    client.send_message("me", client.session.save())
