class GameStats:
    """Monitorowanie danych statystycznych w grze"""

    def __init__(self, ai_game):
        """Inicjallizacja danych statystycznych"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Inicjalizacja danych statystcznych, które mogą zmianiać się w trakcie gry"""
        self.ships_left = self.settings.ship_limit