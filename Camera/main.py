# pg template - skeleton for a new pg project
import pygame as pg
from tilemap import *
from sprites import *
from settings import *
from simplecollider import SimpleCollider
from os import path


class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.SCALED)
        pg.display.set_caption(TITLE)
        self.game_folder = path.dirname(__file__)
        self.clock = pg.time.Clock()
        self.running = True
        self.sprites = []
        self.collider = SimpleCollider()

    def new(self):
        # initialize all variables and do all the setup for a new game
        game_folder = path.dirname(__file__)

        # Make Dictionary of Images
        self.images = {}
        self.images['B'] = Image(self.game_folder + "/tileset_112.png")
        self.images['1'] = Image(self.game_folder + "/wall.png")
        self.images['P'] = Image(self.game_folder + "/courli.png")

        self.map = Map(path.join(game_folder, 'map2.txt'))
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    self.sprites.append(Wall(self.images['1'], col, row))
                if tile == 'B':
                    self.sprites.append(Block(self.images['B'], col, row))
                if tile == 'P':
                    self.player = Player(self.images['P'], col, row)
                    self.sprites.append(self.player)
        # Init Camera
        self.camera = Camera(self.map.width, self.map.height)

    def draw_text(self, text, size, col, x, y):
        # utility function to draw text on screen
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, col)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_surface, text_rect)

    def run(self):
        # Game Loop
        self.dt = self.clock.tick(FPS)

        # Process input (events)
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                self.running = False
        for sprite in self.sprites:
            sprite.events()

        # Update
        for sprite in self.sprites:
            sprite.update()
        self.camera.update(self.player)

        # Collision detection
        self.collider.collide_with_wall(self.player, self.sprites)

        # Render
        self.screen.fill(BLACK)
        for sprite in self.sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # txt = "acc: ({:.2f}, {:.2f})".format(self.player.acc.x, self.player.acc.y)
        # self.draw_text(txt, 25, WHITE, 5, 5)
        # txt = "vel: ({:.2f}, {:.2f})".format(self.player.vel.x, self.player.vel.y)
        # self.draw_text(txt, 25, WHITE, 205, 5)

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
g.new()
while g.running:
    g.run()
pg.quit()
