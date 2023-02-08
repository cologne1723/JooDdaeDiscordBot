import discord, asyncio, http.client, json, requests
from bs4 import BeautifulSoup

import members
import discord_token

token = discord_token.discord_token
headers = {"User-Agent":"JooDdae Bot"}
MAX_TIMEOUT = 30


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
  commands = message.content.split(" ")
  
  if commands[0] == "!막고라":
    import makgora
    await makgora.start_makgora(commands, message, client)
    return


client.run(token)