import pygame

class Player:
    def __init__(self, pos, spd, constraint):
        super().__init__()
        self.image = pygame.surface.Surface((50, 10))
        self.rect = self.image.get_rect(midbottom = pos)
        self.pos = pos
        self.speed = spd
        self.x_constraint = constraint

