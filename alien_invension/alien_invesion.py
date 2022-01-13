import sys
import pygame
from pygame.sprite import Group

from alien import Alien
from  settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_function as gf

#
def run_game():
    #initialize game and set initial screen
    pygame.init()

    ai_Settings = Settings()

    screen = pygame.display.set_mode((ai_Settings.screen_width,ai_Settings.screen_height))

    pygame.display.set_caption("Alien Invesion")

    #Make a play botton
    play_button = Button(ai_Settings,screen,"Play")

    #Make a ship, group of bullet and group of alien
    ship = Ship(ai_Settings,screen)

    #Make group to store bullets
    bullets = Group()
    aliens = Group()

    #set color 
    bg_color = (230,230,230)

    #crate fleet of alien
    #alien = Alien(ai_Settings,screen)
    gf.create_fleet(ai_Settings,screen,ship,aliens)

    #Initialize game stats
    stats = GameStats(ai_Settings)
    sb = Scoreboard(ai_Settings, screen, stats)

    #Start the game
    while(True):
        gf.check_events(ai_Settings,screen,stats, sb, play_button,ship,aliens,bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_Settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_Settings, screen, stats, sb, ship, aliens, bullets)

        gf.updateScreen(ai_Settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()