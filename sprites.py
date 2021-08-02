import pygame as pg
from settings import *


class Player:
    def __init__(self, display, color, width, height, x_loc, y_loc):
        self.width = width
        self.height = height
        self.velo = 0
        self.x_loc = x_loc
        self.y_loc = y_loc

        self.image = pg.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc

    def update(self):

        if self.rect.x + self.rect.width >= WIDTH:    # if > not included can move off screen on 2nd press
            self.rect.x = WIDTH - self.rect.width
        elif self.rect.x <= 0:
            self.rect.x = 0

        self.x_loc += self.velo


class Enemy(pg.sprite.Sprite):
    def __init__(self, display, color, width, height, x_loc, y_loc):
        pg.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.velo = 3
        self.display = display

        self.image = pg.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc

    def update(self):
        if self.x_loc - self.rect.x >= 2*self.width:
            self.rect.y -= self.height // 2
            self.rect.x += self.velo
        elif self.rect.x - self.x_loc <= 2*self.width:
            self.rect.y -= self.height // 2
            self.rect.x += -self.velo


