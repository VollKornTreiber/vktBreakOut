import pygame
from random import choice
from math import floor

class Ball(pygame.sprite.Sprite):
    def __init__(self, start_pos, radius, speed, constr_x, constr_top):
        super().__init__()
        self.image = pygame.surface.Surface((radius*2, radius*2))
        self.rect = self.image.get_rect(center = (0, 0))
        pygame.draw.rect(self.image, "white", (0, 0, radius*2, radius*2), border_radius = radius)
        
        self.speed = speed
        self.rect.x = start_pos[0]
        self.rect.y = start_pos[1]

        self.constr_x = constr_x
        self.constr_top = constr_top
        self.base_speed = speed
        self.speed_pts = 0
        self.activated = False

        self.dir_x = choice((1, -1))
        self.dir_y = -1

    def move(self):
        self.rect.x += self.dir_x * self.speed
        self.rect.y += self.dir_y * self.speed
        
    def check_wall_collision(self):
        if self.rect.left <= self.constr_x[0] or self.rect.right >= self.constr_x[1]:
            self.change_dir((-1, 1))
        if self.rect.top <= self.constr_top:
            self.change_dir((1, -1))

    def update_speed(self):
        if not self.speed >= 8:
            self.speed_pts += .1
            self.speed = int(floor(self.base_speed + self.speed_pts))

    def change_dir(self, dir):
        self.dir_x *= dir[0]
        self.dir_y *= dir[1]

    def activate(self, player_x, player_y, playerwidth):
        self.dir_x = choice((1, -1))
        if self.dir_x == 1:
            self.rect.x = player_x - (playerwidth / 2) + (self.rect.width)
        else:
            self.rect.x = player_x + (playerwidth / 2) - (self.rect.width)

        self.dir_y = 1
        self.rect.y = player_y - playerwidth + 20
        self.activated = True
    
    def update(self):
        if self.activated:
            self.move()
            self.check_wall_collision()