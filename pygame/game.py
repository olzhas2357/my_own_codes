import pygame

clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((600, 450)) # flags = pygame.NOFRAME
pygame.display.set_caption("LIGHT")
icon = pygame.image.load("image/icon.png")
pygame.display.set_icon(icon)
running = True

bg = pygame.image.load('image/sec_im.jpg').convert_alpha()
walk_right = [
    pygame.image.load('image/player/right/right_1.png'),
    pygame.image.load('image/player/right/right_2.png'),
    pygame.image.load('image/player/right/right_3.png'),
    pygame.image.load('image/player/right/right_4.png')
]
walk_left = [
    pygame.image.load('image/player/left/left_1.png'),
    pygame.image.load('image/player/left/left_2.png'),
    pygame.image.load('image/player/left/left_3.png'),
    pygame.image.load('image/player/left/left_4.png')
]

ghost = pygame.image.load('image/ghost.png').convert_alpha()
ghost_list_in_game = []

count = 0
bg_x = 0

player_speed = 5
player_x = 150
player_y = 330

is_jump = False
jump_count = 8

bg_sound = pygame.mixer.Sound('sounds/kahoot.mp3')
bg_sound.play()

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 3500)

label = pygame.font.Font('python_font/med.ttf', 40)
lose_label = label.render('You`re lose !!!', False, (171, 93, 55))
restart_label = label.render("Do you still want to play", False, (140, 80, 128))
restart_label_rect = restart_label.get_rect(topleft = (120, 200))

bullets_left = 5
bullet = pygame.image.load('image/bullet.png').convert_alpha()
bullets = []


gameplay = True

while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x+600, 0))
    # screen.blit(ghost, (ghost_x, 250))
    keys = pygame.key.get_pressed()

    if gameplay:
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game):
                screen.blit(ghost, el)
                el.x -= 10

                if el.x < -10:
                    ghost_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False

        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[count], (player_x, player_y))
        else:
            screen.blit(walk_right[count], (player_x, player_y))


        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 500:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -8:
                if jump_count > 0:
                    player_y -= (jump_count**2)/2
                else:
                    player_y += (jump_count ** 2) / 2

                jump_count -= 1
            else:
                is_jump = False
                jump_count = 8

        if count == 3:
            count = 0
        else:
            count += 1


        bg_x -= 2
        if bg_x == -600:
            bg_x = 0

        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 4

                if el.x > 600:
                    bullets.pop(i)

                if ghost_list_in_game:
                    for (index, ghost1) in enumerate(ghost_list_in_game):
                        if el.colliderect(ghost1):
                            ghost_list_in_game.pop(index)
                            bullets.pop(i)

    else:
        screen.fill((22, 119, 130))
        screen.blit(lose_label, (180, 100))
        screen.blit(restart_label, restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
            gameplay = True
            player_x = 150
            ghost_list_in_game.clear()
            bullets.clear()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(600, 330)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_w and bullets_left > 0:
            bullets.append(bullet.get_rect(topleft=(player_x+30, player_y+10)))
            bullets_left -= 1

    clock.tick(15)