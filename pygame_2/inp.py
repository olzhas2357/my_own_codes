import pygame

class Ino(pygame.sprite.Sprite):
    """class one ino"""

    def __init__(self, screen):
        """first position"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/ghost.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += 0.3
        self.rect.y = self.y

