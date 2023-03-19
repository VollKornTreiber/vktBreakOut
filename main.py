#vktBreakOut - A simple Pygame-BreakOut clone and personal exercise in coding and game development.
#Created by VollKornTreiber - 2023
#Based on several "Clear Code" tutorials on Youtube.
#Font Pixeled.ttf by "OmegaPC777", as used in the aforementioned tutorials.

import sys, pygame
from src.player import Player
from src.ball import Ball
from src.level import Level

VER = "1.0"

#tweaks
FULLSCREEN = True
START_LEVEL = 1
CHEAT_MODE = False

class Game:
    def __init__(self):
        #State setup
        self.game_state = 1
        self.lives = 3
        self.current_level = START_LEVEL
        self.score = 0
        self.bonus = 0

        #GUI setup
        self.font_large = pygame.font.Font("font/Pixeled.ttf", 20)
        self.font_medium = pygame.font.Font("font/Pixeled.ttf", 15)
        self.font_small = pygame.font.Font("font/Pixeled.ttf", 10)
        self.lives_surf = pygame.Surface((16, 16))
        self.lives_icon = pygame.draw.rect(self.lives_surf, "white", (0, 0, 16, 16), border_radius = 8)
        self.lives_start_pos = (screen_W - (self.lives_surf.get_size()[0] + 50), screen_H - screen_H * .1)
        self.score_start_pos = (50, screen_H - screen_H * .2)

        #Start menu setup
        self.title_bg = pygame.Surface((screen_W, screen_H))
        self.title_bg.get_rect(topleft = (0, 0))
        self.title_bg.fill((0, 0, 0))
        self.title_bg.set_alpha(127)
        self.font_title = pygame.font.Font("font/Pixeled.ttf", 60)

        #Field setup
        self.field_surf = pygame.Surface((screen_W * .5, screen_H))
        self.field_surf.fill((20, 20, 20))
        self.field_rect = self.field_surf.get_rect(topleft = (0, 0))
        self.wall_thickness = 30
        
        #Player setup
        self.player_surf = Player((screen_W / 2, self.field_rect.height * .95), 90, 5, (screen_W / 2 - self.field_surf.get_width() / 2 + (self.wall_thickness / 2), screen_W / 2 + self.field_surf.get_width() / 2 - (self.wall_thickness / 2)))
        self.player = pygame.sprite.GroupSingle(self.player_surf)

        #Ball setup
        self.ball_surf = Ball(5, 4, (screen_W / 2 - self.field_surf.get_width() / 2 + (self.wall_thickness / 2), screen_W / 2 + self.field_surf.get_width() / 2 - (self.wall_thickness / 2)), self.wall_thickness / 2)
        self.ball = pygame.sprite.GroupSingle(self.ball_surf)

        #Audio setup
        pygame.mixer.set_num_channels(24)
        self.pad_sound = pygame.mixer.Sound("audio/pad.ogg")
        self.pad_sound.set_volume(.5)
        self.wall_sound = pygame.mixer.Sound("audio/wall.ogg")
        self.wall_sound.set_volume(.5)
        self.progress_sound = pygame.mixer.Sound("audio/progress.ogg")
        self.victory_sound = pygame.mixer.Sound("audio/victory.ogg")
        self.miss_sound = pygame.mixer.Sound("audio/miss.ogg")
        self.gameOver_sound = pygame.mixer.Sound("audio/game_over.ogg")

        #level setup
        self.level_class = Level()
        self.level = self.level_class.construct_level(screen_W, self.field_rect.width, self.current_level)
        self.progress_sound.play()
        

    def draw_field(self):
        screen.blit(self.field_surf, (screen_W / 2 - self.field_surf.get_width() / 2, 0))
        pygame.draw.lines(self.field_surf, "darkgray", False, [self.field_rect.bottomleft, self.field_rect.topleft, self.field_rect.topright, self.field_rect.bottomright], self.wall_thickness)
        pygame.draw.lines(self.field_surf, "lightgray", False, [self.field_rect.bottomleft, self.field_rect.topleft, self.field_rect.topright, self.field_rect.bottomright], int(self.wall_thickness * .85))
        pygame.draw.lines(self.field_surf, "white", False, [self.field_rect.bottomleft, self.field_rect.topleft, self.field_rect.topright, self.field_rect.bottomright], int(self.wall_thickness * .6))

    def check_pad_collision(self):
        #top collision
        if self.player_surf.rect.collidepoint(self.ball_surf.rect.midbottom) and (self.player_surf.rect.collidepoint(self.ball_surf.rect.bottomleft) or self.player_surf.rect.collidepoint(self.ball_surf.rect.bottomright)):
            self.ball_surf.change_dir((1, -1))
            self.pad_sound.play()

        #right collision
        if self.player_surf.rect.collidepoint(self.ball_surf.rect.bottomright) and self.player_surf.rect.collidepoint(self.ball_surf.rect.midright) or self.player_surf.rect.collidepoint(self.ball_surf.rect.topright):
            self.ball_surf.change_dir((-1, 1))
            self.pad_sound.play()

        #left collision
        if self.player_surf.rect.collidepoint(self.ball_surf.rect.bottomleft) and self.player_surf.rect.collidepoint(self.ball_surf.rect.midleft) or self.player_surf.rect.collidepoint(self.ball_surf.rect.topleft):
            self.ball_surf.change_dir((-1, 1))
            self.pad_sound.play()

    def check_block_collision(self):
        if self.level.sprites():
            for block in self.level:
                #bottom/top collision
                if (block.rect.collidepoint(self.ball_surf.rect.midtop) and (block.rect.collidepoint(self.ball_surf.rect.topright) or block.rect.collidepoint(self.ball_surf.rect.topleft))) or (block.rect.collidepoint(self.ball_surf.rect.midbottom) and (block.rect.collidepoint(self.ball_surf.rect.bottomright) or block.rect.collidepoint(self.ball_surf.rect.bottomleft))):
                    self.ball_surf.update_speed()
                    if not CHEAT_MODE:
                        self.ball_surf.change_dir((1, -1))
                    self.score += int(block.value + (self.ball_surf.speed_pts * 10))
                    self.bonus += int(block.value + (self.ball_surf.speed_pts * 10))
                    self.check_extraLife()
                    block.play_sound()
                    block.kill()

                #left/right collision
                if (block.rect.collidepoint(self.ball_surf.rect.midleft) and (block.rect.collidepoint(self.ball_surf.rect.topleft) or block.rect.collidepoint(self.ball_surf.rect.bottomleft))) or (block.rect.collidepoint(self.ball_surf.rect.midright) and (block.rect.collidepoint(self.ball_surf.rect.topright) or block.rect.collidepoint(self.ball_surf.rect.bottomright))):
                    self.ball_surf.update_speed()
                    if not CHEAT_MODE:
                        self.ball_surf.change_dir((-1, 1))
                    self.score += int(block.value + (self.ball_surf.speed_pts * 10))
                    self.bonus += int(block.value + (self.ball_surf.speed_pts * 10))
                    self.check_extraLife()
                    block.play_sound()
                    block.kill()

    def check_miss(self):
        if self.ball_surf.rect.y >= screen_H + self.ball_surf.rect.width:
            screen.fill((255, 0, 0))
            self.ball_surf.deactivate()
            if not CHEAT_MODE:
                self.lives -= 1
            self.miss_sound.play()
            if self.lives <= 0:
                self.game_state = 0 #Game Over!
                self.gameOver_sound.play()

    def check_level_finished(self):
        if not self.level:
            self.progress_sound.play()
            self.ball_surf.deactivate()
            self.current_level += 1
            self.level_class = Level()
            self.level = self.level_class.construct_level(screen_W, self.field_rect.width, self.current_level)
            if not self.level:
                #all levels finished
                self.game_state = 3
                self.victory_sound.play()

    def check_extraLife(self):
        if self.bonus >= 25000:
            if self.lives < 5:
                self.lives += 1
            self.progress_sound.play()
            self.bonus -= 25000

    def show_title(self):
        self.title = self.font_large.render("BreakOut Clone", False, "white")
        self.author = self.font_medium.render("by VollKornTreiber", False, "white")
        screen.blit(self.title, (25, 30))
        screen.blit(self.author, (25, 70))

    def show_lives(self):
        if CHEAT_MODE:
            self.lives_box = self.font_large.render("Lives", False, "gray45")
        elif self.lives >= 2:
            self.lives_box = self.font_large.render("Lives", False, "white")
        elif self.lives == 1:
            self.lives_box = self.font_large.render("Lives", False, "red")

        screen.blit(self.lives_box, (screen_W - screen_W * .2, screen_H - screen_H * .2))
        for life in range(self.lives - 1):
            x = self.lives_start_pos[0] - (life * (self.lives_surf.get_size()[0] + 10))
            screen.blit(self.lives_surf, (x, self.lives_start_pos[1]))

    def show_level(self):
        self.level_textbox = self.font_large.render("Level", False, "white")
        self.level_box = self.font_large.render(f"{self.current_level}", False, "white")
        screen.blit(self.level_textbox, (50, screen_H - screen_H * .3))
        screen.blit(self.level_box, (180, screen_H - screen_H * .3))

    def show_score(self):
        self.score_textbox = self.font_large.render("Score", False, "white")
        self.score_box = self.font_large.render(f"{self.score}", False, "white")
        screen.blit(self.score_textbox, (50, screen_H - screen_H * .2))
        screen.blit(self.score_box, (50, screen_H - screen_H * .15))

    def reset(self):
        self.lives = 3
        self.current_level = 1
        self.score = 0
        self.ball_surf.deactivate()
        self.level_class = Level()
        self.level = self.level_class.construct_level(screen_W, self.field_rect.width, self.current_level)
        self.player_surf.rect.centerx = (screen_W / 2)
        self.progress_sound.play()

    def run(self):

        if self.game_state == 2:
            #Play mode
            #logic update
            self.player.update()
            self.ball.update()
            self.check_pad_collision()
            self.check_block_collision()
            self.check_level_finished()
            self.check_miss()
            #image update
            self.show_title()
            self.show_level()
            self.show_lives()
            self.show_score()
            

        #image update
        self.draw_field()
        self.ball.draw(screen)
        self.player.draw(screen)
        self.level.draw(screen)
        
        if self.game_state == 0:
            #Game over!
            screen.blit(self.title_bg, (0, 0))
            self.gameOver_text = self.font_title.render("GAME OVER!", False, "red")
            self.gameOver_box = self.gameOver_text.get_rect(center = (screen_W / 2, screen_H / 2))
            screen.blit(self.gameOver_text, self.gameOver_box)
            self.show_score()
            self.pressBut_text = self.font_large.render("-Press Space to return-", False, "white")
            self.pressBut_box = self.pressBut_text.get_rect(center = (screen_W / 2, self.gameOver_box.y + 250))
            screen.blit(self.pressBut_text, self.pressBut_box)

        if self.game_state == 1:
            #menu mode
            screen.blit(self.title_bg, (0, 0))
            self.title_text = self.font_title.render("BreakOut Clone", False, "white")
            self.title_box = self.title_text.get_rect(center = (screen_W / 2, screen_H / 2 - 100))
            screen.blit(self.title_text, self.title_box)
            screen.blit(self.font_large.render("by VollKornTreiber", False, "white"), (self.title_box.bottomleft[0], self.title_box.y + 150))
            if not CHEAT_MODE:
                self.pressBut_text = self.font_large.render("-Press Enter to start-", False, "white")
            else: 
                self.pressBut_text = self.font_large.render("-Press Enter to start-", False, "red")
            self.pressBut_box = self.pressBut_text.get_rect(center = (screen_W / 2, self.title_box.y + 350))
            screen.blit(self.pressBut_text, self.pressBut_box)

        if self.game_state == 3:
            #Beaten the game!
            screen.blit(self.title_bg, (0, 0))
            if not CHEAT_MODE:
                self.win_text = self.font_title.render("CONGRATULATIONS!", False, "gold")
            else:
                self.win_text = self.font_title.render("CHEATER!", False, "red")
                self.score = 0
            self.win_box = self.win_text.get_rect(center = (screen_W / 2, screen_H / 2))
            screen.blit(self.win_text, self.win_box)
            self.show_score()
            self.pressBut_text = self.font_large.render("-Press Space to return-", False, "white")
            self.pressBut_box = self.pressBut_text.get_rect(center = (screen_W / 2, self.win_box.y + 250))
            screen.blit(self.pressBut_text, self.pressBut_box)
        


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
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()

    #Game-Instance
    game = Game()

    while True:

        #input
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()

            if game.game_state == 0 or game.game_state == 3:
                #while "game over" or win screen
                if keys[pygame.K_SPACE]:
                    game.reset()
                    game.game_state = 1
                if keys[pygame.K_ESCAPE]:
                    end()

            if game.game_state == 1:
                #while main menu
                if keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
                    game.game_state = 2
                if keys[pygame.K_LSHIFT] and keys[pygame.K_RIGHT]:
                    if game.current_level in range(1, 11):
                        game.current_level += 1
                        game.level_class = Level()
                        game.level = game.level_class.construct_level(screen_W, game.field_rect.width, game.current_level)
                if keys[pygame.K_LSHIFT] and keys[pygame.K_LEFT]:
                    if game.current_level in range(2, 12):
                        game.current_level -= 1
                        game.level_class = Level()
                        game.level = game.level_class.construct_level(screen_W, game.field_rect.width, game.current_level)
                if keys[pygame.K_ESCAPE]:
                    end()
                if keys[pygame.K_LSHIFT] and keys[pygame.K_END]:
                    CHEAT_MODE = not CHEAT_MODE
            
            if game.game_state == 2:
                #while game
                if keys[pygame.K_SPACE]:
                    if not game.ball_surf.activated:
                        game.ball_surf.activate(game.player_surf.rect.centerx, game.player_surf.rect.y, game.player_surf.rect.width)
                if keys[pygame.K_ESCAPE]:
                    game.reset()
                    game.game_state = 1 #return to main menu

            if keys[pygame.K_f]:
                FULLSCREEN = not FULLSCREEN
                if FULLSCREEN: 
                    screen = pygame.display.set_mode((screen_W, screen_H), pygame.FULLSCREEN|pygame.SCALED)
                else:
                    screen = pygame.display.set_mode((screen_W, screen_H))
        
        screen.fill((50, 50, 50))
        game.run()
        pygame.display.flip()
        clock.tick(60)
