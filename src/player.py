import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, start_pos, size_x, spd, x_constr):
        super().__init__()
        self.image = pygame.surface.Surface((size_x, 15))
        self.rect = self.image.get_rect(topleft = (0,0))
        pygame.draw.rect(self.image, "gray85",(0, 0, size_x, 15))
        pygame.draw.lines(self.image, "white", False, (self.rect.bottomleft, self.rect.topleft, self.rect.topright), 2)
        pygame.draw.lines(self.image, "gray42", False, (self.rect.bottomleft, self.rect.bottomright, self.rect.topright), 6)

        self.size_x = size_x
        self.speed = spd
        self.x_constr = x_constr

        #starting position
        self.rect.x = start_pos[0] - self.rect.width / 2
        self.rect.y = start_pos[1]

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