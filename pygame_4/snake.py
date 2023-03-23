import pygame
import time
import random

pygame.init()
pygame.display.set_caption("SNAKE")

width, height = 800, 600
screen = pygame.display.set_mode(size=(width, height))

icon = pygame.image.load("image/snake.png")
pygame.display.set_icon(icon)

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 102)

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 30

font = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 15)

def Your_score(score):
    value = score_font.render("Your score: "+ str(score), True, yellow)
    screen.blit(value, (0, 0))

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [width//6, height//3])

def gameLoop():
    game_over = True
    game_close = False

    x1, y1 = width//2, height//2
    x1_change, y1_change = 0, 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, width - snake_block) / 10.0) * 10.0


    while game_over:
        while game_close == True:
            screen.fill(white)
            message("You Lost! Press W or C-play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        game_over = False
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:

            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill("blue")
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        # pygame.draw.rect(screen, black, [x1, y1, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_list)
        Your_score(length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

gameLoop()
