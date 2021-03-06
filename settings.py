class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3
        self.max_speed_upgrades = 10

        # Bullet settings
        self.bullet_speed = 0.35
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 0.25
        self.alien_speed = 0.10
        self.bullets_allowed = 3
        self.waves_required = 4

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 1

    def increase_speed(self):
        """Increase speed settings."""
        if self.max_speed_upgrades > 0:
            self.ship_speed *= self.speedup_scale
            self.max_speed_upgrades -= 1

        self.alien_speed *= self.speedup_scale
