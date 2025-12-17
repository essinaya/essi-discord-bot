import discord

from game.rock_paper_scissors.views.rps_navigate import (
        RpsNavigate
    )

rps_nav_obj = RpsNavigate()

class HowToPlayView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180):
        super().__init__(timeout=timeout)
        
    #Continue
    @discord.ui.button(label="✅Continue", style=discord.ButtonStyle.success)
    async def htp_continue(self, btn_interaction: discord.Interaction, button: discord.ui.Button):
        await btn_interaction.response.send_message(
            "Ready to Play Rock Paper Scissors?",
            view=rps_nav_obj.determine_view("RPS")
        )

    
    #Exit
    @discord.ui.button(label="🔚 Exit", style=discord.ButtonStyle.red)
    async def htp_exit(self, btn_interaction:discord.Interaction, button: discord.ui.Button):
        await btn_interaction.response.send_message(
            "Goodbye!"
        )
        
        

