import pygame
import random
import sys
import os
from const import *

## keeping path right when packing .exe
def source_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

cd = source_path('')
os.chdir(cd)
##

pygame.init()

##Screen
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
##Title
title = TITLE[random.randint(0, len(TITLE) - 1)]
pygame.display.set_caption(title)
##Icon
icon = pygame.image.load(ICON_PATH)
pygame.display.set_icon(icon)
##Key
pygame.key.stop_text_input()
pygame.key.set_repeat(KEY_DELAY, KEY_INTERVAL)

##game running
import timer
import menu
import game
isPaused = False
isStartedGame = False
isStartedTimer = True
menu = menu.Menu(SCREEN)

while True:
    while not isStartedGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if menu.isClicked('settings', event.pos):
                    menu.drawSettings()
                elif menu.isClicked('start', event.pos):

                    while True:
                        back = False
                        difficulty = None
                        for event2 in pygame.event.get():
                            if event2.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event2.type == pygame.MOUSEBUTTONDOWN:
                                if menu.isClicked('difficulty_back', event2.pos):
                                    back = True
                                elif menu.isClicked('PRESENT', event2.pos):
                                    isStartedGame = True
                                    isStartedTimer = False
                                    difficulty = 'present'
                                elif menu.isClicked('FUTURE', event2.pos):
                                    isStartedGame = True
                                    isStartedTimer = False
                                    difficulty = 'future'
                                elif menu.isClicked('BEYOND', event2.pos):
                                    isStartedGame = True
                                    isStartedTimer = False
                                    difficulty = 'beyond'
                                else:
                                    pass

                        if difficulty is not None:
                            newGame = game.Game(SCREEN, difficulty)

                        if back or isStartedGame:
                            break

                        menu.draw('difficulty')
                        pygame.display.update()

                elif menu.isClicked('quit', event.pos):
                    menu.drawQuit()
                    pygame.quit()
                    sys.exit()

        menu.draw('main')
        pygame.display.update()

    while isStartedGame:
        if not isStartedTimer:
            timer.start()
            isStartedTimer = True

        while not isPaused:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key in PAUSE and timer.pausePreDetect() > DETECT_TIME:
                        isPaused = True
                        timer.pause()
                    else:
                        newGame.keyPressedHandler(event.key)

            if newGame.gameEnd():
                menu.getLastScore(timer.fTime(), newGame.killCnt)
                isStartedGame = False
                timer.end()
                break

            newGame.update()
            newGame.draw()
            pygame.display.update()

        while isPaused:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key in PAUSE and timer.resumePreDetect() > DETECT_TIME:
                        isPaused = False
                        timer.resume()

            newGame.showPause()
            pygame.display.update()
