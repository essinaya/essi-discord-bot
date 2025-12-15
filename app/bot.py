import os
import asyncio
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

# Load .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    raise RuntimeError("DISCORD_TOKEN is missing. Check your .env file.")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN missing")

TOKEN = str(TOKEN)

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

# Bot with no prefix (slash commands only)
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

# When bot is ready
@bot.event
async def on_ready():
    print(f"[READY] Logged in as {bot.user}")
    await tree.sync()
    print("[SYNC] Slash commands synced.")

# Load cogs/extensions
COMMANDS_DIR = "game/rock_paper_scissors/commands"

async def load_extensions():
    print(f"[EXT] Looking in: {COMMANDS_DIR}")
    for filename in os.listdir(COMMANDS_DIR):
        if filename.endswith(".py"):
            module = filename[:-3]
            module_path = f"game.rock_paper_scissors.commands.{module}"
            try:
                await bot.load_extension(module_path)
                print(f"[EXT] Loaded: {module_path}")
            except Exception as e:
                print(f"[EXT] Failed to load {module_path}: {e}")

# Main 
async def main():
    await load_extensions()
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
