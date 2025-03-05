

from config import LOG, LOG_GROUP_ID
import psutil
import time
from ArchMusic import app
from ArchMusic.utils.database import is_on_off
from ArchMusic.utils.database.memorydatabase import (
    get_active_chats, get_active_video_chats)
from ArchMusic.utils.database import (get_global_tops,
                                       get_particulars, get_queries,
                                       get_served_chats,
                                       get_served_users, get_sudoers,
                                       get_top_chats, get_topp_users)



async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ"

        logger_text = f"""
**{app.mention} 𝘼𝙆𝙄𝙎 𝘽𝘼𝙎𝙇𝘼𝘿𝙄**

**𝙜𝙧𝙪𝙥 𝙞𝙙 :** `{message.chat.id}`
**𝙜𝙧𝙪𝙥 𝙖𝙙𝙞 :** {message.chat.title}
**𝙜𝙧𝙪𝙥 𝙠𝙪𝙡𝙡𝙖𝙣𝙞𝙘𝙞 𝙖𝙙𝙞 :** {chatusername}

**𝙠𝙪𝙡𝙡𝙖𝙣𝙞𝙘𝙞 𝙞𝙙 :** `{message.from_user.id}`
**𝙠𝙪𝙡𝙡𝙖𝙣𝙞𝙘𝙞 𝙞𝙨𝙢𝙞 :** {message.from_user.mention}
**𝙠𝙪𝙡𝙡𝙖𝙣𝙞𝙘𝙞 𝙖𝙙𝙞 :** @{message.from_user.username}

**𝙠𝙪𝙮𝙧𝙪𝙠 :** {message.text.split(None, 1)[1]}
**𝙨𝙖𝙧𝙠𝙞 𝙖𝙙𝙞 :** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except Exception as e:
                print(e)
        return