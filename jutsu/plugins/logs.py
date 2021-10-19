from pyrogram import filters
from .updater import HEROKU_APP


@Client.on_message(
    filters.command(["logs"], prefixes=";")
    & filters.user([1013414037]),
    group=3
)
async def logging_(bot, message):
    await bot.send_message(message.chat.id, "`Checking logs...`")
    try:
        limit = (message.text).split()[1]
    except:
        limit = 100
    if not limit.isdigit():
        limit = 100
    if HEROKU_APP:
        logs = (HEROKU_APP.get_log)(lines=limit)
        await bot.send_as_file(
            chat_id=message.chat.id,
            text=logs,
            filename="sedex-heroku.log",
            caption=f"sedex-heroku.log [ {limit} lines ]",
        )