#vktBreakOut - A simple BreakOut clone and personal exercise in game developing

import sys, pygame
from src.player import Player
from src.ball import Ball

#tweeks
FULLSCREEN = 0

class Game:
    def __init__(self):
        #Field setup
        self.field_surf = pygame.Surface((screen_W * .5, screen_H))
        self.field_surf.fill((20, 20, 20))
        self.field_rect = self.field_surf.get_rect(topleft = (0, 0))
        self.wall_thickness = 30
        
        #Player setup
        self.player_surf = Player((screen_W / 2, self.field_rect.height * .95), 5, (screen_W / 2 - self.field_surf.get_width() / 2 + (self.wall_thickness / 2), screen_W / 2 + self.field_surf.get_width() / 2 - (self.wall_thickness / 2)))
        self.player = pygame.sprite.GroupSingle(self.player_surf)

        #Ball setup
        self.ball_surf = Ball((screen_W/2, screen_H/2), 5, 4, (screen_W / 2 - self.field_surf.get_width() / 2 + (self.wall_thickness / 2), screen_W / 2 + self.field_surf.get_width() / 2 - (self.wall_thickness / 2)), self.wall_thickness / 2)
        self.ball = pygame.sprite.GroupSingle(self.ball_surf)

    def draw_field(self):
        screen.blit(self.field_surf, (screen_W / 2 - self.field_surf.get_width() / 2, 0))
        pygame.draw.lines(self.field_surf, "darkgray", False, [self.field_rect.bottomleft, self.field_rect.topleft, self.field_rect.topright, self.field_rect.bottomright], self.wall_thickness)
        pygame.draw.lines(self.field_surf, "lightgray", False, [self.field_rect.bottomleft, self.field_rect.topleft, self.field_rect.topright, self.field_rect.bottomright], int(self.wall_thickness * .85))
        pygame.draw.lines(self.field_surf, "white", False, [self.field_rect.bottomleft, self.field_rect.topleft, self.field_rect.topright, self.field_rect.bottomright], int(self.wall_thickness * .6))

    def check_pad_collision(self):
        if pygame.sprite.spritecollide(self.ball.sprite, self.player, False):
            if self.ball_surf.rect.y <= self.player_surf.rect.top:
                self.ball_surf.change_dir((1, -1))
            else:
                if self.ball_surf.rect.x <= self.player_surf.rect.right or self.ball_surf.rect.x >= self.player_surf.rect.left:
                    self.ball_surf.change_dir((-1, 1))


    def run(self):
        #logic update
        self.player.update()
        self.ball.update()
        self.check_pad_collision()

        #image update
        self.draw_field()
        self.ball.draw(screen)
        self.player.draw(screen)
        


if __name__ == "__main__":

    def end():
        pygame.quit()
        sys.exit()
    
    #Setup
    pygame.init()
    screen_W = 1200
    screen_H = 675

    if FULLSCREEN: 
        screen = pygame.display.set_mode((screen_W, screen_H), pygame.FULLSCREEN|pygame.SCALED)
    else:
        screen = pygame.display.set_mode((screen_W, screen_H))

    pygame.display.set_caption("BreakOut Clone by VollKornTreiber")
    clock = pygame.time.Clock()

    #Game-Instance
    game = Game()

    while True:

        #input
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                end()
            
        
        screen.fill((50, 50, 50))
        game.run()
        pygame.display.flip()
        clock.tick(60)
