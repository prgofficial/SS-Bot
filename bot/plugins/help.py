from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


HELP_TEXT = """
Hi {}. I'm a Screenshot Generator Bot. You can use me for,

    1. Screenshots.
    2. Sample Video.
    3. Trim Video.
 
👺 If bot replies __😟 Sorry! I cannot open the file.__, the file might be --currupted-- or --is malformatted--.

__If issues persists contact @prgofficial.__"""



@ScreenShotBot.on_message(Filters.private & Filters.command("help"))
async def help(c, m):
    
    await m.reply_text(
        text=HELP_TEXT.format(m.from_user.first_name),
        quote=True
    )
