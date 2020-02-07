import pygame
import hunspell

class Game:
    def __init__(self):
        self.height = 600
        self.width  = 800
        self.display = None

    def setup(self):
        pygame.init()
        self.display = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)

    def render(self):
    	pygame.draw.circle(self.display, 255, (0,0), 500)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

if __name__ == "__main__":
    G = Game()
    G.setup()
    G.run()
