import discord, datetime
from game.rock_paper_scissors.utils.game_logic import (
        get_players_choice_value,
        get_bots_choice_value,
        rock_paper_scissors,
        get_state_emoji
    )

class RpsMainMenuView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)

    #How to play
    @discord.ui.button(label="❔How to Play", style=discord.ButtonStyle.primary)
    async def how_to_play(self, btn_interaction: discord.Interaction, button: discord.ui.Button):
        
        await btn_interaction.response.send_message(
            "Classic Rock, Paper, Scissors! Choose between the three, and we'll see if you win against me!",
            view=HowToPlayView()
        )


    #Play Now
    @discord.ui.button(label="🎮Play Now", style=discord.ButtonStyle.success)
    async def play_now(self, btn_interaction: discord.Interaction, button: discord.ui.Button):
        await btn_interaction.response.send_message(
            "Choose your move: Rock, Paper, or Scissors?",
            view = RpsMovesView()
        )
        
        
class HowToPlayView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180):
        super().__init__(timeout=timeout)
        
        
    #Continue
    @discord.ui.button(label="✅Continue", style=discord.ButtonStyle.success)
    async def htp_continue(self, btn_interaction: discord.Interaction, button: discord.ui.Button):
        await btn_interaction.response.send_message(
            "Ready to Play Rock Paper Scissors?",
            view=RpsMainMenuView()
        )

    
    #Exit
    @discord.ui.button(label="🔚 Exit", style=discord.ButtonStyle.red)
    async def htp_exit(self, btn_interaction:discord.Interaction, button: discord.ui.Button):
        await btn_interaction.response.send_message(
            "Goodbye!"
        )


class RpsButton(discord.ui.Button):
    def __init__(self, label, players_choice_int):
        super().__init__(label=label, style=discord.ButtonStyle.primary)
        self.players_choice = players_choice_int #this is the button value

    async def callback(self, interaction: discord.Interaction):
        players_choice = self.players_choice

        #get player's choice value
        players_choice_value = get_players_choice_value(players_choice)
        bots_choice_value = get_bots_choice_value()


        await interaction.response.send_message(
            f"{interaction.user.display_name} chose {players_choice_value}!"
        )
        
        
        await interaction.followup.send(
            f"Bot chose {bots_choice_value}!"
        )

        results = rock_paper_scissors(players_choice)
        results_emoji = get_state_emoji(results)
        await interaction.followup.send(
            f"{interaction.user.display_name} {results}s against Bot! {results_emoji}"
        )
        

class RpsMovesView(discord.ui.View):
    def __init__(self):
        super().__init__()
        todays_date_time = datetime.datetime.now()
        print(f"[RPS Views] New game initiated-------------------------------------------[{todays_date_time}]")
        self.add_item(RpsButton("🪨 Rock", 1)) 
        self.add_item(RpsButton("📰 Paper", 2))
        self.add_item(RpsButton("✂️ Scissors", 3))

