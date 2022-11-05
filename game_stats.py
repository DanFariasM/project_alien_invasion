class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.retrieve_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def retrieve_high_score(self):
        """Retrieving the all time high score, except for 1st time players.
        1st time players will start with a 0 high score."""
        try:
            filename = "high_score.txt"
            with open(filename) as file_object:
                self.high_score = int(file_object.read())
        except FileNotFoundError:
            self.high_score = 0


