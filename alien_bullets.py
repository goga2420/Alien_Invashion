import pygame
from pygame.sprite import Sprite

class AliensBullets(Sprite):
    def __init__(self, ai_settings, screen, alien):
        super(AliensBullets, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(alien.rect.centerx, alien.rect.bottom, ai_settings.aliens_bullets_width, ai_settings.aliens_bullets_height)
        self.rect.top = alien.rect.top

        self.y = float(self.rect.y)

        self.ab_color = ai_settings.aliens_bullets_color
        self.ab_speed_factor = ai_settings.aliens_bullets_speed_factor


    def update(self):
        self.y += self.ab_speed_factor

        self.rect.y = self.y


    def draw_aliens_bullets(self):
        pygame.draw.rect(self.screen, self.ab_color, self.rect)