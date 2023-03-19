import pygame, instrument
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Friends")
    icon = pygame.image.load("images/wow.png")
    pygame.display.set_icon(icon)
    bg_color = (15, 54, 45)
    gun = Gun(screen)
    bullets = Group()
    inps = Group()
    instrument.create_army(screen, inps)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        instrument.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            instrument.update(bg_color, screen, stats, sc, gun, inps, bullets)
            instrument.update_bullets(screen, stats, sc, inps, bullets)
            instrument.update_inos(stats, screen, gun, inps, bullets)

run()


