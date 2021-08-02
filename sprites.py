import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self, color, width, height, x_loc, y_loc):
        pg.sprite.Sprite.__init__(self)
        self.velo = 0
        self.x_loc = x_loc
        self.y_loc = y_loc

        self.image = pg.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc

    def update(self):

        if self.rect.x + self.rect.width >= WIDTH:  # if > not included can move off screen on 2nd press
            self.rect.x = WIDTH - self.rect.width
        elif self.rect.x <= 0:
            self.rect.x = 0

        self.x_loc += self.velo


class Enemy(pg.sprite.Sprite):
    def __init__(self, color, width, height, x_loc, y_loc):
        pg.sprite.Sprite.__init__(self)
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.velo = 1

        self.image = pg.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc

    def update(self):
        self.rect.x += self.velo
        if abs(self.rect.x - self.x_loc) == ENEMY_BOUNDARY or \
                abs((self.rect.x + self.rect.width) - self.x_loc) == WIDTH - ENEMY_BOUNDARY:
            self.rect.y += self.rect.height // 2
            self.velo *= -1
