class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_limit = 2

        self.bullet_width = 1200
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 20

        self.fleet_drop_speed = 10

        #Latwa zmiana szybkości gry
        self.speedup_scale = 1.1
        #Latwa zmiana liczby punktów
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #Inicjalizacja zmiennych ustawień gry
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1

        #Punktacja
        self.alien_score = 50

    def increase_speed(self):
        #Zmiana ustawień dotyczących szybkości i liczby przyznawanych punktów
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_score = int(self.alien_score * self.score_scale)