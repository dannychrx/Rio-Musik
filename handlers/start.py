from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>🔹 **ʜᴀʟᴏ {message.from_user.mention()} ꜱᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ!** \n
💭 **ɴᴀᴍᴀ ꜱᴀʏᴀ {BOT_NAME}, ꜱᴀʏᴀ ᴀᴅᴀʟᴀʜ ᴘᴇɴɢᴀᴍᴇɴ ʏᴀɴɢ ʙᴀɪᴋ , ᴀɴᴅᴀ ʙɪꜱᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ꜱᴀʏᴀ ᴜɴᴛᴜᴋ ᴍᴇᴍᴜᴛᴀʀ ʟᴀɢᴜ ᴅɪ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ (VCG). ɪɴꜰᴏ ʟᴇʙɪʜ ʟᴀɴᴊᴜᴛ ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ꜱᴀʏᴀ ʙɪꜱᴀ ᴛᴇᴋᴀɴ /help . Special Thanks To {OWNER_NAME}**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ ᴛᴀᴍʙᴀʜᴋᴀɴ ꜱᴀʏᴀ ᴋᴇ ɢʀᴜᴘ ᴍᴜ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                         "🐥 Group", url="https://t.me/{GROUP_SUPPORT}")
                    ),
                    InlineKeyboardButton(
                        "🐥 ᴘᴇᴍɪʟɪᴋ ʙᴏᴛ", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "👥 ᴏꜰꜰɪᴄɪᴀʟ ɢʀᴏᴜᴘ", url=f"https://t.me/siiniaja"
                    ),
                    InlineKeyboardButton(
                        "📣 ᴏꜰꜰɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/riobotsupport")
                ],[
                    InlineKeyboardButton(
                        "🤴 ᴘᴇɴᴇᴍᴜ ʙᴏᴛ", url="https://t.me/riio00"
                ],[
                    InlineKeyboardButton(
                        "🛠 Repo", url="http://github.com/RioProjectX/Rio-Music")
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✅ **Bot is running Successful**\n\n<b>🎈 **Bot uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url=f"https://t.me/siiniaja"
                    ),
                    InlineKeyboardButton(
                        "Channel", url=f"https://t.me/riobotsupport"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hello {message.from_user.mention()}, please tap the button below to see the help message you can read for using this bot</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="❔ Cara Menggunakan ❔", url="https://t.me/siiniaja"
                    )
                ]
            ]
        )
    )

@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Halo Welcome to help menu ✨
\n📌ʙᴀɢᴀɪᴍᴀɴᴀ ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ꜱᴀʏᴀ?
\n1. pertama tambahkan saya ke grup mu.
2. promote me as admin and give all permission.
3. kemudian, tambahkan @{ASSISTANT_NAME} ke grupmu atau bisa ketik /userbotjoin.
3. nyalakan dulu VCG sebelum memutar musik.
\n📌**perintan untuk semua anggota grup:**
\n/play (judul lagu) - memutar musik melalui youtube
/stream (balas ke audio) - memutar musik melalui balas audio
/playlist - kenunjukan daftar putar
/current - menunjukan yang sedang diputar saat ini
/song (judul lagu) - mengunduh musik melalui youtube
/search (nama video) - mencari video dari youtube secara rinci
/vsong (nama video) - mengunduh video dari youtube secara rinci
/vk (judul lagu) - unduh melalui mode inline
\n📌 **perintah untuk admin:**
\n/player - membuka panel oengaturan musik
/pause - jeda pemutaran musik
/resume - melanjutkan pemutaran musik
/skip - melompati lagu yang sedang diputar
/end - menghentikan musik
/userbotjoin - mengundang assisten ke grup anda
/reload - untuk memperbarui daftar admin
/cache - untuk membersihkan cache admin
/musicplayer (on / off) - mematikan/menghidupkan pemutar musik di grupmu
\n🎧 channel streaming commands:
\n/cplay - mendengarkan musik lewat channel
/cplayer - melihat daftar putar
/cpause - jeda pemutar musik
/cresume - melajutkan musik yang di jeda
/cskip - melompati lagu yang sedang diputar
/cend - menghentikan lagu
/admincache - memperbarui cache admin
\n🧙‍♂️ command for sudo users:
\n/userbotleaveall - mengeluarkan asisten dari semua grup
/gcast - mengirim pesan siaran
\n📌 **commands for fun:**
\n/lyric - (judul lagu) melihat lirik
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "GROUP", url=f"https://t.me/siiniaja"
                    ),
                    InlineKeyboardButton(
                        "CHANNEL", url=f"https://t.me/riobotsupport"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/riio00"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("Sedang Mengecek Ping...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "**Ping Pong!!**\n"
        f"🔹 `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@authorized_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🔮Status Bot:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
