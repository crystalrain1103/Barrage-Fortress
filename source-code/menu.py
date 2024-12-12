import pygame
import button
import image
from const import *

han_font = pygame.font.SysFont('fangsong', FONT_SIZE)
font = pygame.font.SysFont(None, FONT_SIZE)

class Menu(object):
    def __init__(self, screen):
        self.background = image.Image(MENU_BACKGROUND_PATH, 0,
                                      False, False, None, False, None,
                                      False, None, 0,
                                      False, None, 0,
                                      ORIGIN, SCREEN_SIZE, 0)
        self.screen = screen
        self.lastTime = ('00', '00')
        self.lastPoints = 0
        self.mainTitle = han_font.render(MAIN_MENU_TITLE, True, WHITE)
        self.difficultyTitle = font.render('Select a difficulty', True, WHITE)
        self.settings_button = button.Button(SETTINGS_BUTTON_ID, font, self.screen)
        self.start_button = button.Button(START_BUTTON_ID, font, self.screen)
        self.quit_button = button.Button(QUIT_BUTTON_ID, font, self.screen)
        self.PRESENT_button = button.Button(PRESENT_BUTTON_ID, font, self.screen)
        self.FUTURE_button = button.Button(FUTURE_BUTTON_ID, font, self.screen)
        self.BEYOND_button = button.Button(BEYOND_BUTTON_ID, font, self.screen)
        self.difficulty_back_button = button.Button(DIFFICULTY_BACK_BUTTON_ID, font, self.screen)
        self.settings_temp = button.Button(SETTINGS_TEMP_DIALOG_ID, font, self.screen)

    def draw(self, menu_type):
        self.background.draw(self.screen)
        if menu_type == 'main':
            self.renderLastScore()
            self.renderMainTitle()
            self.drawMainButtons()
        elif menu_type == 'difficulty':
            difficultyPic = pygame.image.load(DIFFICULTY_PIC_PATH)
            difficultyPic = pygame.transform.scale(difficultyPic, DIFFICULTY_PIC_SIZE)
            self.screen.blit(difficultyPic, DIFFICULTY_PIC_RECT)
            self.renderDifficultyTitle()
            self.drawDifficultyButtons()
        else:
            pass

    def drawMainButtons(self):
        self.settings_button.draw()
        self.start_button.draw()
        self.quit_button.draw()

    def drawDifficultyButtons(self):
        self.PRESENT_button.draw()
        self.FUTURE_button.draw()
        self.BEYOND_button.draw()
        self.difficulty_back_button.draw()

    def renderMainTitle(self):
        self.screen.blit(self.mainTitle, MAIN_TITLE_LOC)

    def renderDifficultyTitle(self):
        self.screen.blit(self.difficultyTitle, DIFFICULTY_TITLE_LOC)

    def drawSettings(self):
        self.settings_temp.draw()
        pygame.display.update()
        pygame.time.wait(1000)

    def drawQuit(self):
        pass

    def isClicked(self, button_type, pos):
        if button_type == 'settings':
            if self.settings_button.isCollide(pos):
                return True
        elif button_type == 'start':
            if self.start_button.isCollide(pos):
                return True
        elif button_type == 'quit':
            if self.quit_button.isCollide(pos):
                return True
        elif button_type == 'PRESENT':
            if self.PRESENT_button.isCollide(pos):
                return True
        elif button_type == 'FUTURE':
            if self.FUTURE_button.isCollide(pos):
                return True
        elif button_type == 'BEYOND':
            if self.BEYOND_button.isCollide(pos):
                return True
        elif button_type == 'difficulty_back':
            if self.difficulty_back_button.isCollide(pos):
                return True
        else:
            return False

    def getLastScore(self, time, points):
        self.lastTime = time
        self.lastPoints = points

    def renderLastScore(self):
        textImage = font.render("Last Time : " + str(self.lastTime[0]) + ":" + str(self.lastTime[1]), True, BLACK)
        self.screen.blit(textImage, TIME_SHADOW_COLOR_FONT_LOC)
        textImage = font.render("Last Time : " + self.lastTime[0] + ":" + self.lastTime[1], True, WHITE)
        self.screen.blit(textImage, TIME_MAIN_COLOR_FONT_LOC)

        textImage = font.render("Last Points : " + str(self.lastPoints), True, BLACK)
        self.screen.blit(textImage, POINTS_SHADOW_COLOR_FONT_LOC)
        textImage = font.render("Last Points : " + str(self.lastPoints), True, WHITE)
        self.screen.blit(textImage, POINTS_MAIN_COLOR_FONT_LOC)