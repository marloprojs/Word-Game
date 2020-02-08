import pygame
import hunspell
import math

BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()

class Game:
    def __init__(self):
        self.height = 600
        self.width  = 800
        self.display = None
        self.font = pygame.font.Font("freesansbold.ttf", 32)

    def setup(self):
        self.display = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)
        pygame.display.set_caption("T9 Proj")

    def render(self):
    	pygame.draw.circle(self.display, 255, (0,0), 500)

    def render_letters(self, letters = ["A","B","C","D","E","F","G"]):
        rendered_letters = []
        sep_angle = 360 / len(letters)
        for li, angle in enumerate(range(0, 360, sep_angle)):
            letter = letters[li]
            rendered_letter = self.font.render(letter, True, BLACK)
            self.display.blit(rendered_letter,(0,0))

    def run(self):
        while True:
            self.render()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

if __name__ == "__main__":
    G = Game()
    G.setup()
    G.run()
