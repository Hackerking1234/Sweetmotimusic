from pyrogram import Client

from callsmusic.callsmusic import client as veez
from config import BOT_USERNAME
from helpers.filters import command


@Client.on_message(command(["vk", f"vk@{BOT_USERNAME}"]))
async def songs(client, message):
    try:
        if len(message.command) < 2:
            await message.reply_text(
                "❗ **song not found.**\n\n**please give a valid song name.**"
            )
            return
        text = message.text.split(None, 1)[1]
        results = await veez.get_inline_bot_results(1872165533, f"music {text}")
        await veez.send_inline_bot_result(
            message.chat.id, results.query_id, results.results[0].id
        )
    except Exception:
        await message.reply_text("❗ **song not found.**")
