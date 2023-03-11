import pygame

class Level(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.block_height = 30

    def construct_level(self, screen_w, field_w, lvl):
        self.level_width = field_w - 100

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

        if color == "b":
            pygame.draw.rect(self.image, "orangered", (0, 0, width, height))
            pygame.draw.lines(self.image, "white", False, ((0, self.rect.h), (0, 0), (self.rect.w, 0)), 2)
            pygame.draw.lines(self.image, "tomato3", False, ((0, self.rect.h), (self.rect.w, self.rect.h), (self.rect.w, 0),), 6)

        if color == "c":
            pygame.draw.rect(self.image, "yellow", (0, 0, width, height))
            pygame.draw.lines(self.image, "white", False, ((0, self.rect.h), (0, 0), (self.rect.w, 0)), 2)
            pygame.draw.lines(self.image, "yellow3", False, ((0, self.rect.h), (self.rect.w, self.rect.h), (self.rect.w, 0),), 6)
        
        if color == "d":
            pygame.draw.rect(self.image, "lime", (0, 0, width, height))
            pygame.draw.lines(self.image, "white", False, ((0, self.rect.h), (0, 0), (self.rect.w, 0)), 2)
            pygame.draw.lines(self.image, "yellow4", False, ((0, self.rect.h), (self.rect.w, self.rect.h), (self.rect.w, 0),), 6)

        if color == "e":
            pygame.draw.rect(self.image, "blue", (0, 0, width, height))
            pygame.draw.lines(self.image, "white", False, ((0, self.rect.h), (0, 0), (self.rect.w, 0)), 2)
            pygame.draw.lines(self.image, "royalblue3", False, ((0, self.rect.h), (self.rect.w, self.rect.h), (self.rect.w, 0),), 6)

        if color == "f":
            pygame.draw.rect(self.image, "purple", (0, 0, width, height))
            pygame.draw.lines(self.image, "white", False, ((0, self.rect.h), (0, 0), (self.rect.w, 0)), 2)
            pygame.draw.lines(self.image, "mediumpurple", False, ((0, self.rect.h), (self.rect.w, self.rect.h), (self.rect.w, 0),), 6)

        #return self

lvl_list = [[#1
            "aaaaaaaa",
            "bbbbbbbb",
            "cccccccc",
            "dddddddd",
            "eeeeeeee",
            "ffffffff",
            "        ",
            "        "],

            [#2
            "   aa   ",
            "  bbbb  ",
            "cccccccc",
            " eeeeee ",
            "  eeee  ",
            "fffeefff",
            "feffffef",
            "        "],
        
            [#3
            "acccccca",
            " cffffc ",
            " cffffc ",
            " cccccc ",
            "bbb  bbb",
            "  dddd  ",
            "        ",
            "        "],
        
            [#4
            "        ",
            "eeeeeeee",
            "ccc  ccc",
            "cdc  cdc",
            "ccc  ccc",
            "eeeeeeee",
            " bb  bb ",
            "        "],

            [#5
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        "]
        ]