import pygame
from spellchecker import SpellChecker
import math

BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (252,186,3)
PALE_YELLOW = (255,253,194)
TURQ = (64,224,208)
RED = (237, 39, 28)
DARK_BLUE = (4, 47, 99)

pygame.init()

class Game:
    def __init__(self):
        self.height = 500
        self.width  = 700
        self.display = None
        self.letter_width = 50
        self.radius = 140
        self.font = pygame.font.Font("freesansbold.ttf", self.letter_width)
        self.input_font = pygame.font.Font("freesansbold.ttf", 35)
        self.guess_pts = 20
        self.guess_font = pygame.font.Font("freesansbold.ttf", self.guess_pts)
        self.midpoint = int(self.width/3), int(self.height/2 +50)
        self.letters = ["A","B","C","D","E","F","G"]
        self.input_color = PALE_YELLOW
        self.prev_letter = ""
        self.guess_color = WHITE
        self.real_guesses = []

    def coordinates(self, angle):
        y = math.cos(angle)*(self.radius-5)
        x = math.sin(angle)*(self.radius-5)
        return (int(self.midpoint[0] + x), int(self.midpoint[1] - y))

    def adjust_coords(self, coords, letter):
        real_width, _ = self.font.size(letter)
        return (int(coords[0] - (real_width/2)), int(coords[1] - (self.letter_width/2)))

    def setup(self):
        self.display = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)
        pygame.display.set_caption("Super Freq")

    def render(self):
        self.display.fill(YELLOW)
        pygame.draw.circle(self.display, WHITE, self.midpoint, self.radius)
        self.render_letters()
        self.render_input(self.text.upper())
        self.render_successes()

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
        rendered_input = self.input_font.render(text, True, self.input_color)
        pot_width, _ = self.input_font.size(text)
        location = self.midpoint[0] - pot_width/2
        underline_width = max(pot_width+10, 90)
        if pot_width < 350:
            pygame.draw.line(self.display, PALE_YELLOW, (int(self.midpoint[0] - underline_width/2), 65), (int(self.midpoint[0] + underline_width/2), 65), 4)
            self.display.blit(rendered_input, (int(location), 30))
        else:
            pygame.draw.line(self.display, PALE_YELLOW, (int(self.midpoint[0] - underline_width/2), 65), (int(self.midpoint[0]  + 350/2+5), 65), 4)
            self.display.blit(rendered_input, (int(self.midpoint[0] + 350/2 - pot_width), 30))

    def render_successes(self):
        for gi, guess in enumerate(self.real_guesses):
            loc = int(2*self.width/3), int((gi * self.guess_pts) + 80)
            text = self.guess_font.render(guess, True, self.guess_color)
            self.display.blit(text, loc)

    def validate(self, text):
        self.correct_spelling = self.spell.unknown([self.text])
        if self.text not in self.spell.word_frequency:
            self.input_color = RED
            return False
        else:
            self.add_correct_word(text)
            return True

    def is_adj(self, letter):
        i = 0
        for i in range(len(self.letters)):
            cur_letter = self.letters[i]
            print("cur_letter: \n", cur_letter)
            print("pre letter: \n", self.prev_letter)
            if cur_letter == letter:
                if i != 0 and i != (len(self.letters)-1):
                    if self.prev_letter == self.letters[i-1] or self.prev_letter == self.letters[i+1]:
                        return True
                elif i == 0:
                    if self.prev_letter == self.letters[i+1]:
                        return True
                elif i == len(self.letters)-1:
                    if self.prev_letter == self.letters[i-1]:
                        return True
        return False

    def add_correct_word(self, text):
        self.real_guesses.append(text.upper())
        self.real_guesses.sort()

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
                    self.input_color = PALE_YELLOW
                    if event.key == pygame.K_RETURN:
                        if self.validate(self.text) == True:
                            self.text = ""
                            self.prev_letter = ""
                            
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    elif event.unicode.upper() in self.letters and not self.is_adj(event.unicode.upper()):
                        self.text += event.unicode
                        self.prev_letter = event.unicode.upper()

if __name__ == "__main__":
    G = Game()
    G.setup()
    G.run()
