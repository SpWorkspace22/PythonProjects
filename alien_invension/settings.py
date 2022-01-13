class Settings:
    """A class to store all settings """

    def __init__(self):
        """Initalize game settings """
        #Screen Settings 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)

        #Ship Settings
        self.ship_speed = 1.5  
        self.ship_limit = 3    

        #Bullet Settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0,0,0
        self.bullets_allowed = 5

        #Alien Setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        
        # fleet direction 1 represent right : -1 reprent left
        self.fleet_direction = 1

        #How quickely the game speed up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Inirialize seetings that change throughtout the game."""
        self.ship_speed = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # Scoring
        self.alien_points = 50

        #fleet direction of 1 respresnt right : -1 represnet left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)




