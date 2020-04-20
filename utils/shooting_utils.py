import pygame
from bullet import Bullet
from utils import fleet_utils


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        shot_sound = pygame.mixer.Sound("music/shot_sound.wav")
        pygame.mixer.Sound.play(shot_sound)
        pygame.mixer.music.stop()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def update_aliens_bullets(aliens_bullets):
    aliens_bullets.update()

    for alien_bullet in aliens_bullets.copy():
        if alien_bullet.rect.bottom <= 0:
            aliens_bullets.remove()


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()

    stats.check_high_score(sb)
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()

        stats.level += 1
        sb.prep_level()

        fleet_utils.create_fleet(ai_settings, screen, ship, aliens)
