class GameStats:
    """Track Statistics for Alien Invension."""

    def __init__(self, ai_Settings):
        """Initialize statistics."""
        self.ai_Settings = ai_Settings
        self.reset_status()

        # Start Alien Invasion in an active state.
        self.game_active = False

        self.high_score = 0

    def reset_status(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.ai_Settings.ship_limit
        self.score = 0
        self.level = 1
        

