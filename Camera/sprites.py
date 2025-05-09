import pygame as pg
from settings import *
vec = pg.math.Vector2


class Sprite():
    def __init__(self, imageclass, x, y):
        self.image = imageclass.image
        # print(id(self.image))
        self.rect = self.image.get_rect()
        self.pos = vec(x * TILESIZE, y * TILESIZE)
        self.rect.topleft = self.pos
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.solid = False

    def events(self):
        pass

    def update(self):
        pass


class Wall(Sprite):
    def __init__(self, imageclass, x, y):
        Sprite.__init__(self, imageclass, x, y)
        self.solid = True


class Block(Sprite):
    def __init__(self, imageclass, x, y):
        Sprite.__init__(self, imageclass, x, y)
        self.solid = True


class Player(Sprite):

    def events(self):
        self.acc.x, self.acc.y = 0, 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            self.acc.y = -PLAYER_ACC
        if keystate[pg.K_DOWN]:
            self.acc.y = PLAYER_ACC
        if keystate[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

    def update(self):
        # apply friction
        self.acc += self.vel * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # self.rect.topleft = self.pos
