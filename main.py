#vktBreakOut - A simple BreakOut clone and personal exercise in game delevoping

import sys, pygame
from player import Player

class Game:
    def __init__(self):
        #Field setup
        self.field_surf = pygame.Surface((screen_W * .6, screen_H))
        self.field_surf.fill((20, 20, 20))
        
        #Player setup
        self.player = Player((self.field_surf.get_width() / 2, self.field_surf.get_height() * .95), 5, self.field_surf.get_width())

    def run(self):
        screen.blit(self.field_surf, (screen_W / 2 - self.field_surf.get_width() / 2, 0))    #screen_W / 2 - self.field_surf.get_width() / 2


if __name__ == "__main__":

    def end():
        pygame.quit()
        sys.exit()
    
    #Setup
    pygame.init()
    screen_W = 1200
    screen_H = 900
    screen = pygame.display.set_mode((screen_W, screen_H))
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
