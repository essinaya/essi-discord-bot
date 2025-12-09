import discord
from discord import app_commands
from discord.ext import commands

import views.rps_views
from views.rps_views import RpsMainMenuView, RpsButton, RpsMovesView


#Define command logic. Write the command under a Cog
class RPSCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="rps", description="Play Rock Paper Scissors with Essi Bot")
    async def rps(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            content = "Ready to Play Rock Paper Scissors?",
            view= RpsMainMenuView,
            ephemeral=True
        )

    
    
#Add the setup function for bot loading so that Essi bot can register the command properly
async def setup(bot: commands.Bot):
    await bot.add_cog(RPSCommand(bot))




