import pygame
from load_image import load_image
from players import playersgroup

platformgroup = pygame.sprite.Group()


class LevelPlatform(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, text, color, allsprites):
        super().__init__(allsprites, platformgroup)
        self.text = text
        font = pygame.font.Font(None, 100)
        string_rendered = font.render(text, 1, pygame.Color(color))
        self.image = load_image("platform.png")
        self.rect = string_rendered.get_rect()
        self.image.blit(string_rendered, self.rect)
        pygame.draw.rect(self.image, color, self.rect, width=5)
        self.rect.x = x
        self.rect.y = y
        screen.blit(self.image, self.rect)

    def update(self):
        info = pygame.sprite.spritecollide(self, playersgroup, False)
        if len(info) == len(playersgroup):
            print(f"СРОЧНО ЗАПУСКАЙ УРОВЕНЬ {self.text}")