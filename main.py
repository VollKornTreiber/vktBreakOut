#vktBreakOut - A simple BreakOut clone and personal exercise in game delevoping

import sys, pygame
from player import Player

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
        player_sprite = Player((screen_W / 2, self.field_rect.height * .95), 5, [screen_W / 2 - self.field_surf.get_width() / 2 + (self.wall_thickness / 2), screen_W / 2 + self.field_surf.get_width() / 2 - (self.wall_thickness / 2)])
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def draw_field(self):
        screen.blit(self.field_surf, (screen_W / 2 - self.field_surf.get_width() / 2, 0))
        pygame.draw.lines(self.field_surf, "darkgray", False, [self.field_rect.bottomleft, self.field_rect.topleft, self.field_rect.topright, self.field_rect.bottomright], self.wall_thickness)
        pygame.draw.lines(self.field_surf, "lightgray", False, [self.field_rect.bottomleft, self.field_rect.topleft, self.field_rect.topright, self.field_rect.bottomright], int(self.wall_thickness * .85))
        pygame.draw.lines(self.field_surf, "white", False, [self.field_rect.bottomleft, self.field_rect.topleft, self.field_rect.topright, self.field_rect.bottomright], int(self.wall_thickness * .6))

    def run(self):
        #logic update
        self.player.update()

        #image update
        self.draw_field()
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
