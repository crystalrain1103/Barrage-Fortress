import pygame
import data_button

class Button(object):
    def __init__(self, id, font, screen):
        self.id = id
        self.screen = screen
        self.x = self.getData()['X']
        self.y = self.getData()['Y']
        self.width = self.getData()['WIDTH']
        self.height = self.getData()['HEIGHT']
        self.buttonColor = self.getData()['BUTTON_COLOR']
        self.text = self.getData()['TEXT']
        self.textLoc = self.getData()['TEXT_LOC']
        self.textColor = self.getData()['TEXT_COLOR']
        self.button = pygame.Rect(self.x, self.y, self.width, self.height)
        self.words = font.render(self.text, True, self.textColor)

    def getData(self):
        return data_button.data[self.id]

    def draw(self):
        pygame.draw.rect(self.screen, self.buttonColor, self.button)
        self.screen.blit(self.words, self.textLoc)

    def isCollide(self, pos):
        return self.button.collidepoint(pos)

