import os

api_id = None
api_hash = None


# If not saved or if the user wants to change them
if not api_id or not api_hash or input("Do you want to change API ID and API Hash? (y/n): ").strip().lower() == "y":
    api_id = input("Please enter your API ID: ").strip()
    api_hash = input("Please enter your API Hash: ").strip()

    # Save the credentials
    with open("api_credentials.txt", "w") as file:
        file.write(api_id + "\n")
        file.write(api_hash + "\n")

# Check if API ID and API Hash are already saved
if os.path.exists("api_credentials.txt"):
    with open("api_credentials.txt", "r") as file:
        saved_credentials = file.read().splitlines()
        if len(saved_credentials) == 2:
            api_id, api_hash = saved_credentials


from telethon import TelegramClient, sync, events
from time import sleep
from pyrogram import Client, filters
from pyrogram.errors.exceptions.flood_420 import FloodWait
import asyncio

app = Client("hexa", api_id, api_hash)

fitem = input("Enter what you want to find : \n")

async def main():
    async with app:
        while True:
            await app.send_message("hexamonbot", "/hunt")
            print("Sending Message ...", end="")
            await asyncio.sleep(20)

@app.on_message(filters.incoming & filters.chat("hexamonbot"))
async def echo(client, message):
    print("... Receiving Message")
    if not message.text:
        message.text = message.caption
    print(message.text)
    if fitem in message.text:
        print("Found Shiny/TM")
        quit()

app.run(main())
