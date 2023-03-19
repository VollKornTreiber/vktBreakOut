import pygame

class Level(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.block_height = 30

    def construct_level(self, screen_w, field_w, lvl):
        self.level_width = field_w - 100
        if lvl <= len(lvl_list):
            for index_row, row in enumerate(lvl_list[lvl-1]):
                for index_col, col in enumerate(row):
                    if not col == " ":
                        self.block_surf = Block(self.level_width / 8, self.block_height, col, (screen_w / 2 - self.level_width / 2) + self.level_width / 8 * (index_col), 100 + self.block_height * (index_row))
                        self.add(self.block_surf)

        return self

class Block(pygame.sprite.Sprite):
    def __init__(self, width, height, color, pos_x, pos_y):
        super().__init__()
        
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft = (pos_x, pos_y))

        if color == "a":
            pygame.draw.rect(self.image, "red", (0, 0, width, height))
            pygame.draw.lines(self.image, "white", False, ((0, self.rect.h), (0, 0), (self.rect.w, 0)), 2)
            pygame.draw.lines(self.image, "salmon", False, ((0, self.rect.h), (self.rect.w, self.rect.h), (self.rect.w, 0),), 6)
            self.value = 500
            self.sound = pygame.mixer.Sound("audio/A.ogg")

        if color == "b":
            pygame.draw.rect(self.image, "orange", (0, 0, width, height))
            pygame.draw.lines(self.image, "white", False, ((0, self.rect.h), (0, 0), (self.rect.w, 0)), 2)
            pygame.draw.lines(self.image, "tomato3", False, ((0, self.rect.h), (self.rect.w, self.rect.h), (self.rect.w, 0),), 6)
            self.value = 300
            self.sound = pygame.mixer.Sound("audio/B.ogg")

        if color == "c":
            pygame.draw.rect(self.image, "yellow", (0, 0, width, height))
            pygame.draw.lines(self.image, "white", False, ((0, self.rect.h), (0, 0), (self.rect.w, 0)), 2)
            pygame.draw.lines(self.image, "yellow3", False, ((0, self.rect.h), (self.rect.w, self.rect.h), (self.rect.w, 0),), 6)
            self.value = 250
            self.sound = pygame.mixer.Sound("audio/C.ogg")
        
        if color == "d":
            pygame.draw.rect(self.image, "lime", (0, 0, width, height))
            pygame.draw.lines(self.image, "white", False, ((0, self.rect.h), (0, 0), (self.rect.w, 0)), 2)
            pygame.draw.lines(self.image, "yellow4", False, ((0, self.rect.h), (self.rect.w, self.rect.h), (self.rect.w, 0),), 6)
            self.value = 200
            self.sound = pygame.mixer.Sound("audio/D.ogg")

        if color == "e":
            pygame.draw.rect(self.image, "blue", (0, 0, width, height))
            pygame.draw.lines(self.image, "white", False, ((0, self.rect.h), (0, 0), (self.rect.w, 0)), 2)
            pygame.draw.lines(self.image, "royalblue3", False, ((0, self.rect.h), (self.rect.w, self.rect.h), (self.rect.w, 0),), 6)
            self.value = 150
            self.sound = pygame.mixer.Sound("audio/E.ogg")

        if color == "f":
            pygame.draw.rect(self.image, "purple", (0, 0, width, height))
            pygame.draw.lines(self.image, "white", False, ((0, self.rect.h), (0, 0), (self.rect.w, 0)), 2)
            pygame.draw.lines(self.image, "mediumpurple", False, ((0, self.rect.h), (self.rect.w, self.rect.h), (self.rect.w, 0),), 6)
            self.value = 100
            self.sound = pygame.mixer.Sound("audio/F.ogg")

    def play_sound(self):
        self.sound.play()


lvl_list = [[#1
            "aaaaaaaa",
            "bbbbbbbb",
            "cccccccc",
            "dddddddd",
            "eeeeeeee",
            "ffffffff"],

            [#2
            "   aa   ",
            "  bbbb  ",
            "cccccccc",
            " eeeeee ",
            "  eeee  ",
            "fffeefff",
            "feffffef",
            "   ff   "],
        
            [#3
            "acccccca",
            " caaaac ",
            " caaaac ",
            " cccccc ",
            "bbb  bbb",
            "  dddd  ",
            "   dd   ",
            "   dd   "],
        
            [#4
            "        ",
            "eeeeeeee",
            "ccc  ccc",
            "cdc  cdc",
            "ccc  ccc",
            "eeeeeeee",
            " bb  bb ",
            "ee    ee",
            "ccc  ccc",
            "e e  e e"],

            [#5
            "dd dd dd",
            " cd  dc ",
            "  cbbc  ",
            " cd  dc ",
            "dd dd dd",
            " cd  dc ",
            "  cbbc  ",
            " cd  dc ",
            "dd dd dd",
            " cd  dc "],

            [#6
            "        ",
            "bbbbbbbb",
            "        ",
            "ff    ff",
            " ffaaff ",
            "  ffff  ",
            " ffbbff ",
            "ffb  bff",
            "        ",
            "bbbbbbbb",
            "bbbbbbbb"],

            [#7
            "        ",
            " bbbbbb ",
            "bbbbbbbb",
            " aaaaaa ",
            "dddddddd",
            "cccccccc",
            "bbbbbbbb",
            " bbbbbb ",
            "        "],

            [#8
            " bcabca ",
            "b abca c",
            "cabaabca",
            "aaa  aaa",
            "        ",
            "de de de",
            "efd  def",
            "fd fd fd",
            "  f  f  ",
            "        ",
            " a aa a ",
            "abcabcba",
            " cabcab "],

            [#9
            " fff    ",
            "fff aa  ",
            "ff   aa ",
            "ff   aa ",
            "fff aa  ",
            " fff    ",
            "    aaa ",
            "  ff aaa",
            " ff   aa",
            " ff   aa",
            "  ff aaa",
            "    aaa "],

            [#10
            " eeeeee ",
            "e      e",
            "e cccc e",
            "e c  c e",
            "e cddc e",
            "e c  c e",
            "e cccc e",
            "e c  c e",
            "e cddc e",
            "e c  c e",
            "e cccc e",
            "e      e",
            " eeeeee "],

            [#11
            "aaaaaaaa",
            "bbbbbbbb",
            "cccccccc",
            "dddddddd",
            "e e e e ",
            " f f f f",
            "        ",
            "aaaaaaaa",
            "bbbbbbbb",
            "cccccccc",
            "dddddddd",
            " e e e e",
            "f f f f ",
            "        "],

            [#signalize and triggers end screen
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        "]
        ]