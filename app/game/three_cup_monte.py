#an introduction
#explanation of rules of the game
#get the player's name via interactions object
#get the player's input. but instead of 0,1,2 it's 1,2,3
import random
import discord



def three_cup_monte_game(choice):
    monte_list = [" ","O", " "]
    random.shuffle(monte_list)
    if monte_list[choice - 1] == "O":
        return "You won!"
    else:
        return "Better luck next time! " + str(monte_list)



class MonteMenuView(discord.ui.View):

    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)


    # button 1
    @discord.ui.button(label="How to Play", style=discord.ButtonStyle.primary)
    async def how_to_play(self, btn_interaction: discord.Interaction, button: discord.ui.Button):
        await btn_interaction.response.send_message(
            "The rules are simple. I will shuffle three cups and you guess the one with the ball."
        )

    # button 2
    @discord.ui.button(label="Play Now", style=discord.ButtonStyle.success)
    async def play_now(self, btn_interaction: discord.Interaction, button: discord.ui.Button):
        await btn_interaction.response.send_message(
            "Pick a cup: 1, 2, or 3.",
            view=CupSelectionView()
        )

    #implement loop until user says to terminate



class CupButton(discord.ui.Button):
    def __init__(self, label, cup_number):
        super().__init__(label=label, style=discord.ButtonStyle.primary) #constructor
        self.cup_number = cup_number  # this is your “value”

    async def callback(self, interaction: discord.Interaction):
        # Here is where you get the user's choice
        choice = self.cup_number

        await interaction.response.send_message(
            f"You picked cup {choice}!"
        )
        #actual game
        result = three_cup_monte_game(choice)
        await interaction.followup.send(result)



class CupSelectionView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(CupButton("Cup 1", 1))
        self.add_item(CupButton("Cup 2", 2))
        self.add_item(CupButton("Cup 3", 3))
