import pygame
pygame.init()

icon = pygame.image.load("image/icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("GAME")

bg_x = 0

clock = pygame.time.Clock()
class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))

        self.dx, self.dy = 0, 0

    def update(self, *args):
        self.rect.x += self.dx
        self.dx = 0
        self.rect.y += self.dy
        self.dy = 0
width, height = 800, 400
screen = pygame.display.set_mode(size = (width, height))
player = Object(100, 200, "image/square.png")

running = True
while running:
    bg = pygame.image.load("image/swamp.png")
    screen.blit(bg, (bg_x, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        player.dx = 5
    if key[pygame.K_a]:
        player.dx = -5
    if key[pygame.K_s]:
        player.dy = 5
    if key[pygame.K_w]:
        player.dy = -5


    player.update()
    screen.blit(player.image, player.rect)
    clock.tick(60)
    pygame.display.flip()
