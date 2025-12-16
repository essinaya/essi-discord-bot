import discord
from discord import app_commands
from discord.ext import commands

from game.rock_paper_scissors.views.rps_views import (
    RpsMainMenuView,
    RpsButton,
    RpsMovesView
)


#Define command logic. Write the command under a Cog
class RPSCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="rps", description="Play Rock Paper Scissors with Essi Bot")
    async def rps(self, interaction: discord.Interaction):
        view = RpsMainMenuView()  # INSTANTIATE THE VIEW.
        #Discord UI elements (Views, Buttons, Select menus) must be instances, not classes.
        
        await interaction.response.send_message(
            content = "Ready to Play Rock Paper Scissors?",
            view= view, #must receive an object instance, not the class. Previous code was RpsMainMenuView
            #view= RpsMainMenuView(), #this works as well. Either of the two works.
            ephemeral=True
        )

    
    
#Add the setup function for bot loading so that Essi bot can register the command properly
async def setup(bot: commands.Bot):
    await bot.add_cog(RPSCommand(bot))




