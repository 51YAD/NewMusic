from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in @SportsFederation group's voice call.

aDd Me To Your Group And Play Music ,Enjoy My musics and Sports Talks!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Sports  Federation 🛠", url="https://t.me/SportsFederation")
                  ],[
                    InlineKeyboardButton(
                        "🏏 Cricket", url="https://t.me/IPLFansKerala"
                    ),
                    InlineKeyboardButton(
                        "⚽️ Football", url="https://t.me/Football_Lokam"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Football Status ➕", url="https://t.me/FootballStatus
                        "
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏏 Cricket", url="https://t.me/IPLFansKerala")
                ]
            ]
        )
   )


