from dis import disco
import os
import asyncio
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from game.three_cup_monte import (MonteMenuView)

# Load .env
load_dotenv()
# TOKEN: str = os.getenv("DISCORD_TOKEN")
TOKEN = os.getenv("DISCORD_TOKEN")
TOKEN_PATH = TOKEN if TOKEN is not None else "C:"

if TOKEN is None:
    raise RuntimeError("DISCORD_TOKEN is missing. Check your .env file.")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN missing")

TOKEN = str(TOKEN)

#Get w.o.e (my personal discord) from .env
WOE_DISCORD_ID = os.getenv("WOE_DISCORD_ID")
WOE_DISCORD_ID = int(WOE_DISCORD_ID) if WOE_DISCORD_ID is not None else 0
WOE_DISCORD_ID_TOKEN = discord.Object(id=WOE_DISCORD_ID)

# Intents
intents = discord.Intents.default()
intents.guilds = True

# Bot
bot = commands.Bot(command_prefix="!", intents=intents)

# ---------- SLASH COMMANDS ----------

@bot.tree.command(name="introduction", description="Introduce the Essi Bot")
async def introduction(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Hello! I'm Essi Bot. I can play Three Cup Monte and Rock Paper Scissors."
    )

@bot.tree.command(name="monte", description="Play Three Cup Monte")
async def monte(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Welcome {interaction.user.display_name}!",
        view=MonteMenuView()
    )

# ---------- SETUP HOOK (CRITICAL) ----------

@bot.event
async def setup_hook():
    # Load RPS cogs
    commands_dir = "game/rock_paper_scissors/commands"
    for file in os.listdir(commands_dir):
        if file.endswith(".py"):
            await bot.load_extension(
                f"game.rock_paper_scissors.commands.{file[:-3]}"
            )

    # Sync ALL slash commands
    await bot.tree.sync()
    print("[SYNC] Slash commands synced")

# ---------- READY ----------

@bot.event
async def on_ready():
    print(f"[READY] Logged in as {bot.user}")

# ---------- START ----------

async def main():
    await bot.start(TOKEN_PATH)

if __name__ == "__main__":
    asyncio.run(main())