class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.path = ai_game.path

        # Start alien invasion in an active state
        self.game_active = False

        # High score should not be reset
        with open(self.path+"/high_score.txt","r") as f:
            self.high_score = int(f.read())

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1