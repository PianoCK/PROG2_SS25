# pg template - skeleton for a new pg project
import pygame as pg

WIDTH = 800
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pg and create window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()
vec = pg.math.Vector2


class Sprite():
    def __init__(self, color, x, y):
        self.image = pg.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.center = self.pos

    def events(self):
        pass

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.image, self.rect)


class Wall(Sprite):
    pass


class Player(Sprite):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.vel = vec(0, 0)

    def events(self):
        self.vel.x, self.vel.y = 0, 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            self.vel.y = -3
        if keystate[pg.K_DOWN]:
            self.vel.y = 3
        if keystate[pg.K_LEFT]:
            self.vel.x = -3
        if keystate[pg.K_RIGHT]:
            self.vel.x = 3

    def update(self):
        self.pos += self.vel


class Collider():

    def collide_with_wall(self, sprite1: Sprite, spritegroup):
        sprite1.rect.x = sprite1.pos.x
        for sprite2 in spritegroup:
            self.collide_with_wall_dir("x", sprite1, sprite2)
        sprite1.rect.y = sprite1.pos.y
        for sprite2 in spritegroup:
            self.collide_with_wall_dir("y", sprite1, sprite2)

    def collide_with_wall_dir(self, dir, sprite1, sprite2):
        if dir == "x":
            if sprite1.rect.colliderect(sprite2.rect):
                if isinstance(sprite2, Wall):
                    if sprite1.vel.x >= 0:
                        sprite1.pos.x = sprite2.rect.left - sprite1.rect.width
                    if sprite1.vel.x <= 0:
                        sprite1.pos.x = sprite2.rect.right
                    sprite1.vel.x = 0
                    # sprite1.acc.x = 0
                    sprite1.rect.x = sprite1.pos.x

        if dir == "y":
            if sprite1.rect.colliderect(sprite2.rect):
                if isinstance(sprite2, Wall):
                    if sprite1.vel.y >= 0:
                        sprite1.pos.y = sprite2.rect.top - sprite1.rect.height
                    if sprite1.vel.y <= 0:
                        sprite1.pos.y = sprite2.rect.bottom
                    sprite1.vel.y = 0
                    # sprite1.acc.y = 0
                    sprite1.rect.y = sprite1.pos.y


sprites = []
sprites.append(Wall(WHITE, WIDTH / 2 + 100, HEIGHT / 2))
sprites.append(Wall(WHITE, 50, 50))
sprites.append(Wall(WHITE, WIDTH - 140, HEIGHT - 140))
player = Player(GREEN, WIDTH / 2, HEIGHT / 2)
sprites.append(player)

collider = Collider()

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)

    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
    for sprite in sprites:
        sprite.events()

    # Update
    for sprite in sprites:
        sprite.update()

    # Collision detection
    collider.collide_with_wall(player, sprites)

    # Render
    screen.fill(BLACK)
    for sprite in sprites:
        sprite.render(screen)

    # Double Buffering
    pg.display.flip()

pg.quit()
