import discord





class RpsNavigate(discord.ui.View):
    def __init__(self):
        self = self
        
        
    def determine_view(self, view_choice):
        self.view_choice = view_choice
        print(f"[RPS Navigate] Determining views to be passed: {self.view_choice}")

        #initialize views
        print("Initializing views...")
        from game.rock_paper_scissors.views.rps_views import (
                    RpsMainMenuView,
                    RpsMovesView
                )
        
        from game.rock_paper_scissors.views.how_to_play_views import (
                    HowToPlayView
                )
        rps_main_menu_view = RpsMainMenuView()
        how_to_play_view = HowToPlayView()
        rps_moves_view = RpsMovesView()


        if self.view_choice == "RPS":
            return rps_main_menu_view
        elif self.view_choice == "HTP":
            return how_to_play_view
        elif self.view_choice == "RMV":
            return rps_moves_view
        else:
            return rps_main_menu_view
        