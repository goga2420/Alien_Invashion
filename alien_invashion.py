import pygame
from pygame.sprite import Group

import game_functions
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from settings import Settings
from ship import Ship

from utils import fleet_utils, shooting_utils


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    stats.high_score = stats.read_high_score()
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    aliens_bullets = Group()

    fleet_utils.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        game_functions.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            shooting_utils.update_aliens_bullets(aliens_bullets)
            shooting_utils.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            game_functions.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        game_functions.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, aliens_bullets)
        ship.blitme()

run_game()
