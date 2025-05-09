# pg template - skeleton for a new pg project
import pygame as pg
from tilemap import *
from sprites import *
from settings import *
from collider import *
from os import path


class SimpleCollider():

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


simpleCollider = SimpleCollider()

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.game_folder = path.dirname(__file__)
        self.clock = pg.time.Clock()
        self.running = True
        self.sprites = []
        self.walls = []
        self.txt1 = ""
        self.txt2 = ""
        self.collider = Collider()
        self.collisions = []
        self.vel = vec(0, 0)

    def new(self):
        # initialize all variables and do all the setup for a new game
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, 'map.txt'))
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    wall = Wall(self.game_folder + "/wall.png", col, row)
                    self.sprites.append(wall)
                    self.walls.append(wall)
                if tile == 'P':
                    self.player = Player(
                        self.game_folder + "/courli.png", col, row)
                    self.sprites.append(self.player)

    def draw_text(self, text, size, col, x, y):
        # utility function to draw text on screen
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, col)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_surface, text_rect)

    def checkCollisionsSimpleAABB(self):
        simpleCollider.collide_with_wall(self.player, self.walls)
        self.player.update_pos()

    def checkCollisionsSweptAABB(self):
        self.collisions = self.collider.collideSweptAABB(
            self.player, self.walls)
        for collision in self.collisions:
            self.player.vel = self.collider.ResolveDynamicRectVsRect(
                self.player.vel, collision["contact_time"], collision["contact_normal"])
        # Update Player Position
        self.player.update_pos()

    def checkCollisionsAABB(self):
        self.collisions = self.collider.collideAABB(self.player, self.walls)
        self.collider.resolveAABB(self.player, self.collisions)

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            # keep loop running at the right speed
            self.dt = self.clock.tick(FPS)

            # Process input (events)
            for event in pg.event.get():
                # check for closing window
                if event.type == pg.QUIT:
                    running = False
            for sprite in self.sprites:
                sprite.events()

            # Update
            for sprite in self.sprites:
                sprite.update()

            # Collisions: Beide Methoden funktionieren hier gut...
            #self.checkCollisionsSimpleAABB()
            # self.checkCollisionsSweptAABB()
            self.checkCollisionsAABB()

            # Render
            self.screen.fill(BLACK)
            for sprite in self.sprites:
                sprite.render(self.screen)

            # Draw normal vector to the collision objects
            for wall in self.collisions:
                wall["object"].mark(self.screen, wall["contact_normal"])

            # Double Buffering
            pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.run()
    g.show_go_screen()

pg.quit()
