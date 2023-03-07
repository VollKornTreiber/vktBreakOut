import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, start_pos, spd, x_constr):
        super().__init__()
        self.image = pygame.surface.Surface((90, 15))
        self.image.fill("white")
        self.rect = self.image.get_rect(midbottom = start_pos)
        self.speed = spd
        self.x_constr = x_constr

    def move(self):
        #input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.rect.left <= self.x_constr[0]:
                self.rect.left = self.x_constr[0]
            else:
                if keys[pygame.K_LSHIFT]:
                    self.rect.x -= self.speed + 5   #accelerate
                else:
                    self.rect.x -= self.speed   #regular speed

        if keys[pygame.K_RIGHT]:
            if self.rect.right >= self.x_constr[1]:
                self.rect.right = self.x_constr[1]
            else:
                if keys[pygame.K_LSHIFT]:
                    self.rect.x += self.speed + 5   #accelerate
                else:
                    self.rect.x += self.speed   #regular speed

    def update(self):
        self.move()