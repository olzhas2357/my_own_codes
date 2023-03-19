import pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
test_font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()

sky_surface = pygame.image.load("image/Sky.png").convert_alpha()
ground_surface = pygame.image.load("image/ground.png").convert_alpha()

# score_surf = test_font.render("My game", False, (0, 0, 0))
# score_2_surf = test_font.render("You`re lose", False, (25, 45, 48))
# score_rect = score_surf.get_rect(center = (400, 50))

def display_store():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f"{current_time}", False, (0, 0, 0))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

snail_surface = pygame.image.load("image/snail/snail.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600, 300))

player_surface = pygame.image.load("image/player/player_walk_1.png")
player_rect = player_surface.get_rect(midbottom = (80, 300))

game_active = True
start_time = 0
score = 0

player_stand = pygame.image.load("image/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 320))

player_gravity = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks ()/1000)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, 'Pink', score_rect)
        # pygame.draw.rect(screen, 'Pink', score_rect, 12)
        # pygame.draw.ellipse(screen, 'Yellow', pygame.Rect(12, 12, 100, 100))
        # screen.blit(score_surf, score_rect)

        score = display_store()

        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)


        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        screen.blit(player_surface, player_rect)

        if snail_rect.colliderect(player_rect):
            game_active = False

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        score_message = test_font.render(f"Your score: {score}", False, (11, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(game_name, game_name_rect)
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
    pygame.display.flip()

    clock.tick(60)