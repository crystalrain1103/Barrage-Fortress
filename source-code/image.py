import pygame

class Image(pygame.sprite.Sprite):
    def __init__(self, pathFmt, pathIndex,
                 direction, left, leftPathFmt, right, rightPathFmt,
                 revive, revivePathFmt, revivePathIndexCount,
                 die, diePathFmt, diePathIndexCount,
                 pos, size = None, pathIndexCount = 0):
        self.pathFmt = pathFmt
        self.pathIndex = pathIndex
        self.direction = direction
        self.left = left
        self.leftPathFmt = leftPathFmt
        self.right = right
        self.rightPathFmt = rightPathFmt
        self.revive = revive
        self.revivePathFmt = revivePathFmt
        self.revivePathIndexCount = revivePathIndexCount
        self.die = die
        self.diePathFmt = diePathFmt
        self.diePathIndexCount = diePathIndexCount
        self.pos = list(pos)
        self.size = size
        self.pathIndexCount = pathIndexCount
        self.updateImage()

    def updateImage(self):
        if self.revive:
            path = self.revivePathFmt
        elif self.die:
            path = self.diePathFmt
        else:
            if self.direction:
                if self.left:
                    path = self.leftPathFmt
                else:
                    path = self.rightPathFmt
            else:
                path = self.pathFmt
        if self.pathIndexCount != 0:
            path = path % self.pathIndex
        self.image = pygame.image.load(path)
        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)

    def updateIndex(self, pathIndex):
        self.pathIndex = pathIndex
        self.updateImage()

    def updateSize(self, size):
        self.size = size
        self.updateImage()

    def getRect(self):
        rect = self.image.get_rect()
        rect.x, rect.y = self.pos
        return rect

    def draw(self, screen):
        screen.blit(self.image, self.getRect())