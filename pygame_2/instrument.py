import pygame, sys
from bullet import Bullet
from inp import Ino
import time


def events(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # right
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            # right
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False


def update(bg_color, screen,stats, sc, gun, inp, bullets):
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inp.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc, inps, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inps, True, True)
    if collisions:
        for inps in collisions.values():
            stats.score += 10*len(inps)
        sc.image_score()

    if len(inps) == 0:
        bullets.empty()
        create_army(screen, inps)


def gun_kill(stats, screen, gun, inps, bullets):
    """столкновение пушки и армии"""
    if stats. guns_left > 0:
        stats.guns_left -= 1
        inps.empty()
        bullets.empty()
        create_army(screen, inps)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_inos(stats, screen, gun, inps, bullets):
    inps.update()
    if pygame.sprite.spritecollideany(gun, inps):
       gun_kill(stats, screen, gun, inps, bullets)
    inos_check(stats, screen, gun, inps, bullets)



def inos_check(stats, screen, gun, inps, bullets):
    screen_rect = screen.get_rect()
    for inp in inps.sprites():
        if inp.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, inps, bullets)
            break

def create_army(screen, inps):
    inp = Ino(screen)
    inp_width = inp.rect.width
    number_inp_x = int((700 - 2* inp_width) / inp_width)
    inp_height = inp.rect.height
    number_inp_y = int((800 - 100 - 2*inp_height) / inp_height)

    for row_number in range(number_inp_y-1):
        for inp_number in range(number_inp_x):
            inp = Ino(screen)
            inp.x = inp_width + (inp_width * inp_number)
            inp.y = inp_height + (inp_height * row_number)
            inp.rect.x = inp.x
            inp.rect.y = inp.rect.height + (inp.rect.height * row_number)
            inps.add(inp)
