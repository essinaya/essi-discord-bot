import os
from dotenv import load_dotenv
import discord

#look for a file named ".env" in the SAME folder of this python script and loads each key value pair in the script.
load_dotenv()
#this gets the "DISCORD_TOKEN" key from the .env file, TOKEN gets the value
TOKEN = os.getenv("DISCORD_TOKEN")

#Discord bots must declare what kind of events they want to receive. default() gives you a basic, safe set of intents that are enough
#for simple bots that do not need message content or member lists.
intents = discord.Intents.default()

#This creates the actual bot client object. Think of "client" as your connection to Discord; 
# it handles the WebSocket, events, and sending messages. Passing intents=intents tells Discord what kind of events you want.
#discord.Client is a class from the library. 'client' is the instance of it.
client = discord.Client(intents=intents)

#This is a decorator that registers the function under it as an event handler. 
# You are telling the client: “remember this function and call it later when Discord fires the event.”
#This is reserved for Discord events! (because of discord.Client)
#client.event is a method that takes your function (like on_ready) and registers it as an event handler inside the client. 
# It does not return “client.event”. It returns a new function that the client stores internally in its event registry.
@client.event
#This defines an asynchronous function that is called automatically by discord.py when the bot has successfully connected and is ready. 
# It does not take any parameters for this event.
#the method name MUST match what is indicated in the Discord API. 'on_ready' is one of Discord's methods
#otherwise, DISCORD WILL NOT FIRE IT. A special logic of your own making should be created if you want your own methods
async def on_ready():
    #Inside on_ready, this prints a message to your terminal so you know the bot logged in correctly.
    #  client.user is the bot’s own user object, and the f-string inserts it into the text.
    print(f"Logged in as {client.user}")
#This starts the bot. It opens a connection to Discord using the token, 
# then blocks the script and runs the internal event loop until you stop it with Ctrl+C or an error happens.
#the entry point. Can be interpreted as the 'main' in Java
client.run(TOKEN)



def essi_bot_introduction():
    print("Hello, world! This is the Essi bot! I am just a simple bot that can do Three Cup Monte, Tic-Tac-Toe, and Blackjack!")

