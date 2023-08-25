# Bot
from pyrogram import Client, filters
from pyrogram.types import Message

# Text extract
from PIL import Image
import pytesseract

# api id, api hash, bot token
import config

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = Client(
    name="bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.TOKEN,
)

@app.on_message(filters.private & filters.command("start"))
async def start(bot:Client, message: Message):
    chat_id = message.chat.id
    name = message.from_user.first_name

    await message.reply_text(
        text=f"**Hello dear [{name}](tg://user?id={chat_id})!**\n\n"
             f"Use /help to get some **information about Bot**\n"
             f"**Only English**\n"
             f"**Note: This robot cannot extract handwriting from images**\n"
             f"**Send your Image** for **Text Extraction** : ")


@app.on_message(filters.private &  filters.photo)
async def photo(client: Client, message: Message):
    msg = await message.reply_text("Please Wait ...")
    image = await client.download_media(message)
    text = pytesseract.image_to_string(Image.open(image), "eng")
    await msg.delete()
    await message.reply_text(f"`{text}`")


@app.on_message(filters.private & filters.command("help"))
async def help(client: Client, message:Message):
    await message.reply_text("Developed by : [01101](https://github.com/Aliireza1101)\n\nRepository link :\n[click here](https://github.com/Aliireza1101/image-to-text)")

if __name__ == "__main__":

    print("BOT IS RUNNING!")
    app.run()
