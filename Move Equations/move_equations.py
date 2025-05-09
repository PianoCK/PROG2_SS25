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

# Motion variables
PLAYER_ACC = 0.3 * 60 / FPS
PLAYER_FRICTION = -0.03


# initialize pg and create window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()


class Player():
    def __init__(self):
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.ax, self.ay = 0, 0
        self.x, self.y = (WIDTH / 2, HEIGHT / 2)
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.move_4way()
        # equations of motion
        self.ax += self.vx * PLAYER_FRICTION
        self.ay += self.vy * PLAYER_FRICTION
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx + 0.5 * self.ax
        self.y += self.vy + 0.5 * self.ay

        # borders
        if self.x + self.rect.width < 0:
            self.x = WIDTH
        if self.x > WIDTH:
            self.x = -self.rect.width
        if self.y + self.rect.height < 0:
            self.y = HEIGHT
        if self.y > HEIGHT:
            self.y = -self.rect.height

        self.rect.x = self.x
        self.rect.y = self.y

    def move_4way(self):
        self.ax = 0
        self.ay = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            self.ay = -PLAYER_ACC
        if keystate[pg.K_DOWN]:
            self.ay = PLAYER_ACC
        if keystate[pg.K_LEFT]:
            self.ax = -PLAYER_ACC
        if keystate[pg.K_RIGHT]:
            self.ax = PLAYER_ACC
        if self.ax != 0 and self.ay != 0:
            self.ax *= 0.7071
            self.ay *= 0.7071

    def render(self, screen):
        screen.blit(self.image, self.rect)


sprites = []
player = Player()
sprites.append(player)

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

    # Update
    for sprite in sprites:
        sprite.update()

    # Render
    screen.fill(BLACK)
    for sprite in sprites:
        sprite.render(screen)

    # Double Buffering
    pg.display.flip()

pg.quit()
