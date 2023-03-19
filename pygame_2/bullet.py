import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """create the bullet in position of gun"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 250, 12)
        self.color = 112, 16, 24
        self.speed = 3
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """displacement of bullet"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet on display"""
        pygame.draw.rect(self.screen, self.color, self.rect)