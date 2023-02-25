#sahibim #HuseynH

#əməyə xatir kanala qoşulun @Botlarm
import os
import requests
import aiohttp
import yt_dlp
import wget
from config import Config
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
from yt_dlp import YoutubeDL
from pyrogram import Client, filters
import yt_dlp
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)


#config#

bot = Client(
    'RahidMusic',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)

#start mesajı

## Əmrlər --------------------------------
@bot.on_message(filters.command(['start']))
def start(client, message):
    MusicAzBot = f'[👋](https://te.legra.ph/file/01f12da067a1340352710.jpg) Salam @{message.from_user.username}\n\nℹ️ Bu bot ilə istədiyiniz musiqi və video yükləyə bilərsiniz\n\nYükləmək üçün:\n1) /song (musiqi adı)\n2) /video (video adı)'
    message.reply_text(
        text=MusicAzBot, 
        quote=False,
         reply_markup=InlineKeyboardMarkup(
            [
                [
                  InlineKeyboardButton(
                        "➕ ❰ Qrupa Əlavə Et ❱ ➕", url=f"https://t.me/{Config.BOT_USERNAME}?startgroup=true"
                    )
                ],
                [ 
                  InlineKeyboardButton(
                        "🎧 Playlist", url=f"https://t.me/{Config.PLAYLIST_NAME}"
                    ),
                ],
                [                     
                  InlineKeyboardButton(
                        "✅ Kanal", url=f"https://t.me/{Config.CHANNEL}"
                    )                    
                ]
                
           ]
        ),
    )
  
  
#alive mesaji
@bot.on_message(filters.command("alive") & filters.user(Config.BOT_OWNER))
async def live(client: Client, message: Message):
    livemsg = await message.reply_text('Mən Əla İşləyirəm ✅')
    
#musiqi əmri#

@bot.on_message(filters.command("song") & ~filters.edited)
def song(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("<b>Musiqi Axtarıram... 🔍</b>")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("İstədiyiniz musiqi tapılmadı 😕")
        print(str(e))
        return
    m.edit("`✅ Musiqini tapdım və göndərirəm...`")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🎧 **Başlıq**: [{title[:35]}]({link})\n⌛ **Müddət**: `{duration}`\n'f"🤖 **Bot**: [Music Bot](https://t.me/{Config.BOT_USERNAME})"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("✅ Göndərirəm...")
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer=f"{Config.PLAYLIST_NAME}")
        m.delete()
        bot.send_audio(chat_id=Config.PLAYLIST_ID, audio=audio_file, caption=rep, performer=f"{Config.BOT_USERNAME}", parse_mode='md', title=title, duration=dur, thumb=thumb_name)
    except Exception as e:
        m.edit('**⚠️ Gözlənilməyən xəta yarandı**\n**Xahiş edirəm xətanı @Rahid_7 sahibimə xəbərdar et!**')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


@bot.on_message(filters.command("video") & ~filters.edited)
async def vsong(client, message):
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("🔍 **Video Axtarıram...**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"🚫 **Xəta:** {e}")
    preview = wget.download(thumbnail)
    await msg.edit("✅ **Videonu tapdım və göndərirəm...**")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=ytdl_data["title"],
    )
    try:
        os.remove(file_name)
        await msg.delete()
    except Exception as e:
        print(e)



bot.run()
