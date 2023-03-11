#vktBreakOut - A simple BreakOut clone and personal exercise in game developing

import sys, pygame
from src.player import Player
from src.ball import Ball
from src.level import Level

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
        self.player_surf = Player((screen_W / 2, self.field_rect.height * .95), 90, 5, (screen_W / 2 - self.field_surf.get_width() / 2 + (self.wall_thickness / 2), screen_W / 2 + self.field_surf.get_width() / 2 - (self.wall_thickness / 2)))
        self.player = pygame.sprite.GroupSingle(self.player_surf)
        self.lives = 3

        #Ball setup
        self.ball_surf = Ball((screen_W/2, screen_H/2), 5, 4, (screen_W / 2 - self.field_surf.get_width() / 2 + (self.wall_thickness / 2), screen_W / 2 + self.field_surf.get_width() / 2 - (self.wall_thickness / 2)), self.wall_thickness / 2)
        self.ball = pygame.sprite.GroupSingle(self.ball_surf)

        #level setup
        self.level_class = Level()
        self.level = self.level_class.construct_level(screen_W, self.field_rect.width, lvl = 1)

    def draw_field(self):
        screen.blit(self.field_surf, (screen_W / 2 - self.field_surf.get_width() / 2, 0))
        pygame.draw.lines(self.field_surf, "darkgray", False, [self.field_rect.bottomleft, self.field_rect.topleft, self.field_rect.topright, self.field_rect.bottomright], self.wall_thickness)
        pygame.draw.lines(self.field_surf, "lightgray", False, [self.field_rect.bottomleft, self.field_rect.topleft, self.field_rect.topright, self.field_rect.bottomright], int(self.wall_thickness * .85))
        pygame.draw.lines(self.field_surf, "white", False, [self.field_rect.bottomleft, self.field_rect.topleft, self.field_rect.topright, self.field_rect.bottomright], int(self.wall_thickness * .6))

    def check_pad_collision(self):
        #top collision
        if self.player_surf.rect.collidepoint(self.ball_surf.rect.midbottom) and (self.player_surf.rect.collidepoint(self.ball_surf.rect.bottomleft) or self.player_surf.rect.collidepoint(self.ball_surf.rect.bottomright)):
            self.ball_surf.change_dir((1, -1))

        #right collision
        if self.player_surf.rect.collidepoint(self.ball_surf.rect.bottomright) and self.player_surf.rect.collidepoint(self.ball_surf.rect.midright) or self.player_surf.rect.collidepoint(self.ball_surf.rect.topright):
            self.ball_surf.change_dir((-1, 1))

        #left collision
        if self.player_surf.rect.collidepoint(self.ball_surf.rect.bottomleft) and self.player_surf.rect.collidepoint(self.ball_surf.rect.midleft) or self.player_surf.rect.collidepoint(self.ball_surf.rect.topleft):
            self.ball_surf.change_dir((-1, 1))

    def check_block_collision(self):
        if self.level.sprites():
            for block in self.level:
                pygame.sprite.spritecollide(self.ball.sprite, self.level, True)
                #bottom/top collision
                if (block.rect.collidepoint(self.ball_surf.rect.midtop) and (block.rect.collidepoint(self.ball_surf.rect.topright) or block.rect.collidepoint(self.ball_surf.rect.topleft))) or (block.rect.collidepoint(self.ball_surf.rect.midbottom) and (block.rect.collidepoint(self.ball_surf.rect.bottomright) or block.rect.collidepoint(self.ball_surf.rect.bottomleft))):
                    self.ball_surf.update_speed()
                    self.ball_surf.change_dir((1, -1))

                #left/right collision
                if (block.rect.collidepoint(self.ball_surf.rect.midleft) and (block.rect.collidepoint(self.ball_surf.rect.topleft) or block.rect.collidepoint(self.ball_surf.rect.bottomleft))) or (block.rect.collidepoint(self.ball_surf.rect.midright) and (block.rect.collidepoint(self.ball_surf.rect.topright) or block.rect.collidepoint(self.ball_surf.rect.bottomright))):
                    self.ball_surf.update_speed()
                    self.ball_surf.change_dir((-1, 1))
    
    def check_lives(self, amount):
        if self.lives <= 0:
            self.gameOver()

    def check_level_finished(self):
        if not self.level:
            print("DONE!")

    def gameOver(self, lives):
        if lives <= 0:
            while True:
                print("GAME OVER!")

    def run(self):
        #logic update
        self.player.update()
        self.ball.update()
        self.check_pad_collision()
        self.check_block_collision()
        self.check_level_finished()

        #image update
        self.draw_field()
        self.ball.draw(screen)
        self.player.draw(screen)
        self.level.draw(screen)
        


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
            #debug: ball reset
            if keys[pygame.K_SPACE]:
                game.ball_surf.reset(screen_H)
            
        
        screen.fill((50, 50, 50))
        game.run()
        game.check_lives(game.lives)
        pygame.display.flip()
        clock.tick(60)
