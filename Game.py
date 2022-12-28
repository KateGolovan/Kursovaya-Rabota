from Base2 import working_process
import pygame as pg
import sys
WIN_SIZE = 750

class game_process:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([WIN_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.game_running = working_process(self)

    def new_game(self):
        self.game_running = working_process(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.new_game()

    def run(self):
        while True:
            self.game_running.run()
            self.check_events()
            pg.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = game_process()
    game.run()