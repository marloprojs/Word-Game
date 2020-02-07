import pygame
from spellchecker import SpellChecker
import math

BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (252,186,3)
PALE_YELLOW = (255,253,194)
TURQ = (64,224,208)

pygame.init()

class Game:
    def __init__(self):
        self.height = 500
        self.width  = 700
        self.display = None
        self.letter_width = 50
        self.radius = 150
        self.font = pygame.font.Font("freesansbold.ttf", self.letter_width)
        self.input_font = pygame.font.Font("freesansbold.ttf", 25)
        self.midpoint = int(self.width/2), int(self.height/2 +50)
        self.letters = ["A","B","C","D","E","F","G"]

    def coordinates(self, angle):
        y = math.cos(angle)*self.radius
        x = math.sin(angle)*self.radius
        return (int(self.midpoint[0] + x), int(self.midpoint[1] - y))

    def adjust_coords(self, coords, letter):
        real_width, _ = self.font.size(letter)
        return (int(coords[0] - (real_width/2)), int(coords[1] - (self.letter_width/2)))

    def setup(self):
        self.display = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)
        pygame.display.set_caption("T9 Proj")

    def render(self):
        self.display.fill(YELLOW)
        pygame.draw.circle(self.display, WHITE, self.midpoint, self.radius)
        self.render_letters()
        self.render_input(self.text.upper())

    def render_letters(self, letters = None):
        if letters == None:
            letters = self.letters
        rendered_letters = []
        sep_angle = (2*math.pi) / len(letters)
        for li, letter in enumerate(letters):
            angle = sep_angle*li
            letter = letters[li]
            lx, ly = self.coordinates(angle)
            adj_location = self.adjust_coords((lx, ly), letter)
            pygame.draw.circle(self.display, WHITE, (lx, ly-2), int(self.letter_width/2+8))
            rendered_letter = self.font.render(letter, True, BLACK)
            self.display.blit(rendered_letter, adj_location)

    def render_input(self, text):
        rendered_input = self.input_font.render(text, True, PALE_YELLOW)
        pot_width, _ = self.input_font.size(text)
        location = self.midpoint[0] - pot_width/2
        self.display.blit(rendered_input, (int(location), 30))

    def run(self):
        self.text = ""
        self.correct_spelling = ""
        self.spell = SpellChecker()
        while True:
            self.render()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        self.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                        self.correct_spelling = spell.correction(self.text)
                        if(spell.unknown(self.text))



if __name__ == "__main__":
    G = Game()
    G.setup()
    G.run()
