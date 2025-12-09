import os
import asyncio
from dotenv import load_dotenv
import discord
from discord import app_commands
from game.three_cup_monte import *
from game.rock_paper_scissors.views import rps_views


#look for a file named ".env" in the SAME folder of this python script and loads each key value pair in the script.
load_dotenv()
#this gets the "DISCORD_TOKEN" key from the .env file, TOKEN gets the value
TOKEN = os.getenv("DISCORD_TOKEN")

#Discord bots must declare what kind of events they want to receive. default() gives you a basic, safe set of intents that are enough
#for simple bots that do not need message content or member lists.
# Discord "intents" tell the API what events your bot wants to receive.
# Example of events: message updates, guild joins, member updates, reactions, etc.
# If an intent is disabled here, Discord will NOT send those events to your bot.
# This improves safety and performance.
#
# Some intents are privileged (like members and presence) and must be enabled in the Developer Portal.
#
# intents = the configuration object we pass to the bot when we create it.
intents = discord.Intents.default()

#discord.Client is a class from the library. 'client' is the instance of it.
# discord.Client = the base class for a barebones Discord connection.
# discord.Bot or commands.Bot = built on top of discord.Client, with slash commands, prefix commands, etc.
# You should only create ONE bot object. It represents your connection to Discord.
#
# When we pass intents=intents, we are telling Discord exactly what events this bot wants.
#
# The bot object handles:
#    - connecting to the Discord Gateway
#    - receiving events
#    - sending messages
#    - loading slash commands
#    - dispatching interaction events
#
# Think of this as the "brain" and "connection" of the bot.
client = discord.Client(intents=intents)

#discord.Client is a low level connection. discord.Bot has more functionality. Think of Client as the parent class, Bot as the child class
#  and inherits.
#client = discord.Bot(intents=intents)
#this isn't working btw. But I'll keep this for future references.




#name = the parameter for the slash command '/introduction'
#description = the parameter on what the user sees when it hovers over the command '/introduction'
#ctx = means 'context'. Or more specifically, 'interaction context'. This is provided by the Discord. You don't do this to yourself.
#      it's like saying 'my coroutine accepts a context object' to Discord. And Discord will provide the context object. 
#      The 'context object' provided by Discord contains the following: the user who triggered the command, the guild (server), the channel,
#      the command name, the interaction token, methods to respond
#ctx.respond() = is your bot telling Discord: “I received the slash command, and here is my official response.”
#                This is what satisfies the requirement. Without it, the interaction times out. The requirement = "The bot must acknowledge the interaction within 3 seconds."
#                If the bot didn't respond before this line, then the command fails. It will output 'Interaction failed'.
#                If it dies after ctx.respond(), Discord considers the interaction resolved already.
#@client.slash_command(name="introduction", description="Introduce the Essi Bot")
#async def intro(ctx):
#    essi_bot_introduction()
#    await ctx.respond("Introduction complete")


#Okay since the client.slash_command isn't working (and apparently it's not the python way) I'm going to use this instead.
#But I'll keep it for future reference.

# Slash commands belong to an AppCommand tree.
# In discord.py, this is done through app_commands.CommandTree.
#
# The CommandTree's job:
#    - register your slash commands
#    - sync them to Discord so users can see them
#
# 'tree' is like a container that holds all slash commands for this bot.
# It is similar to how the bot object holds event handlers.
tree = app_commands.CommandTree(client)

# This is a normal Python helper function, not a coroutine.
# Since it does not talk to Discord directly, it does not need 'async' or 'await'.
# Slash command handlers can call normal Python functions like this.
def essi_bot_introduction_console():
    print("Hello, world! This is the Essi bot! I am just a simple bot that can do Three Cup Monte, Tic-Tac-Toe, and Blackjack!")

# name = the name of the slash command. This becomes '/introduction'.
# description = the text users see when they hover over the command in Discord.

# A slash command function receives an 'interaction' parameter.
# 'interaction' is provided by Discord automatically.
# It represents the entire context of the command:
#    - the user who triggered it
#    - the guild (server)
#    - the channel
#    - the command name
#    - the interaction token
#    - response methods you must call

# IMPORTANT:
# Slash commands must respond within 3 seconds.
# This is a Discord rule, not a Python rule.
# If the bot does NOT respond in time:
#    Discord marks the command as 'failed'
#    and shows: "This interaction failed."

# Calling interaction.response.send_message(...) is how the bot
# acknowledges the command. Once this line executes successfully:
#    Discord considers the interaction 'resolved'.
# If the bot crashes AFTER this response, the interaction
# is still considered complete on Discord's side.
@tree.command(name="introduction", description="Introduce the Essi Bot")
#interaction is similar to the 'ctx' above (BUT THEY ARE NOT THE SAME THING, NOT INTERCHANGEABLE, and used in different command systems.). 
# DISCORD PROVIDES THIS. You don't need to create one for you. It contains the following:
#he user who triggered the command, the guild (server), the channel, the command name, the interaction token, methods to respond
async def introduction(interaction: discord.Interaction):
    essi_bot_introduction_console()
    await interaction.response.send_message("Hello, world! This is the Essi bot! I am just a simple bot that can do Three Cup Monte, Tic-Tac-Toe, and Blackjack!")

#Three Cup Monte
@tree.command(name="monte", description="Play Three Cup Monte")
async def monte(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Hello, {interaction.user.display_name}! Welcome to Three Cup Monte!"
    )
    await interaction.followup.send(
        "Would you like instructions or start now?",
        view=MonteMenuView()
    )

#Rock Paper Scissors
async def rps(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Hello, {interaction.user.display_name}! Welcome to Rock, Paper Scissors!",
        view  = rps_views.RpsMainMenuView()
    )

    
#This is a decorator that registers the function under it as an event handler. 
# You are telling the client: “remember this function and call it later when Discord fires the event.”
#This is reserved for Discord events! (because of discord.Client)
#client.event is a method that takes your function (like on_ready) and registers it as an event handler inside the client. 
# It does not return “client.event”. It returns a new function that the client stores internally in its event registry.

#This defines an asynchronous function that is called automatically by discord.py when the bot has successfully connected and is ready. 
# It does not take any parameters for this event.
#the method name MUST match what is indicated in the Discord API. 'on_ready' is one of Discord's methods
#otherwise, DISCORD WILL NOT FIRE IT. A special logic of your own making should be created if you want your own methods
# on_ready() is an event from discord.Client.
# Discord calls this function when the bot has successfully connected
# and is ready to receive events and interactions.
#
# A common job of on_ready() is syncing slash commands:
#    await tree.sync()
#
# Without syncing, new slash commands will NOT show up in Discord.
@client.event
async def on_ready():
    #Inside on_ready, this prints a message to your terminal so you know the bot logged in correctly.
    #  client.user is the bot’s own user object, and the f-string inserts it into the text.
    print(f"Logged in as {client.user}")
    await tree.sync()
    print("Bot is ready!")
#This starts the bot. It opens a connection to Discord using the token, 
# then blocks the script and runs the internal event loop until you stop it with Ctrl+C or an error happens.
#the entry point. Can be interpreted as the 'main' in Java
client.run(TOKEN)




async def load_extensions():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await bot.load_extension(f"commands.{filename[:-3]}")

asyncio.run(load_extensions())
