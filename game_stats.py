class GameStats:
    """Monitorowanie danych statystycznych w grze"""

    def __init__(self, ai_game):
        """Inicjallizacja danych statystycznych"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

        #Najlepszy wynik ever
        self.high_score = 0

    def reset_stats(self):
        """Inicjalizacja danych statystcznych, które mogą zmianiać się w trakcie gry"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1