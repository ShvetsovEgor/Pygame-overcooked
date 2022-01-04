import pygame.sprite
from load_image import load_image

playersgroup = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, allsprites):
        super().__init__(allsprites, playersgroup)
        self.frames = []
        self.cut_sheet(load_image("walk.png"), 4, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.image = load_image("red.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        go = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            go = True

        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            go = True

        if keys[pygame.K_UP]:
            self.rect.y -= 5
            go = True

        if keys[pygame.K_DOWN]:
            self.rect.y += 5
            go = True
        # if go:
        #     self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        #     self.image = self.frames[self.cur_frame]


class SecondPlayer(pygame.sprite.Sprite):
    def __init__(self, x, y, allsprites):
        super().__init__(allsprites, playersgroup)
        self.image = load_image("green.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5

        if keys[pygame.K_d]:
            self.rect.x += 5

        if keys[pygame.K_w]:
            self.rect.y -= 5

        if keys[pygame.K_s]:
            self.rect.y += 5
