from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from blackjackcode import black_jack

# Loading the token into the program
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Bot set-up below
intents: Intents = Intents.default()
#intents.message_content = True #NOQA
client: Client = Client(intents=intents)

# Reading messages
async def send_message(message: Message, user_message:str) -> None:
    if not user_message:
        print("(Message was empty because intents were not enabled)")
        return
    user_message = user_message.strip().lower()

    if user_message == 'play blackjack':
        try:
            response = black_jack()
            for msg in response:
                await message.channel.send(msg)
        #await message.author.send(response) if user_message[0] == '?' else await message.channel.send(response)
        except Exception as e:
            print(f"Error in blackjack game: {e}")
    else:
        await message.channel.send("Send 'play blackjack' to start the game!")

# Start-up for the Bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# Incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    if user_message.startswith("play blackjack"):
        game_response = black_jack()
        await message.channel.send("\n".join(game_response))
    elif user_message.startswith("1") or user_message.startswith("11"):
        game_response = black_jack(player_choice=user_message)
        await message.channel.send("\n".join(game_response))
    elif user_message in ["hit","stay"]:
        game_response = black_jack(player_choice=user_message)
        await message.channel.send("\n".join(game_response))
    else:
        await message.channel.send("Send 'play blackjack' to start the game!")

client.run(TOKEN)

