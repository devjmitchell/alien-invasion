import json

saved_high_score = 'saved_high_score.json'

def load_high_score():
    with open(saved_high_score) as h_score:
        loaded_high_score = json.load(h_score)
        return loaded_high_score

class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        # self.high_score = 0 #DELETE THIS LINE SINCE USING SAVED HIGH SCORE?
        self.high_score = load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1