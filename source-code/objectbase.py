import image
import time
import data_object
from const import HITBOX


class ObjectBase(image.Image):
    def __init__(self, id, pos):
        self.id = id
        self.hp = self.getHP()
        self.tears = self.getTears()
        self.dmg = self.getDamage()
        self.timeCurSummon = 0
        self.timeCurIndex = 0
        self.timeCurPos = 0
        self.doRevive = False
        self.doDie = False
        self.tearShield = False
        self.hasRevive = False
        self.hasDebuff = False
        self.hasBuff = False
        self.hasHeal = False
        super(ObjectBase, self).__init__(
            self.getData()['PATH'],
            0,
            self.getData()['DIRECTION'],
            self.getData()['LEFT'],
            self.getData()['LEFT_PATH'],
            self.getData()['RIGHT'],
            self.getData()['RIGHT_PATH'],
            self.getData()['REVIVE'],
            self.getData()['REVIVE_PATH'],
            self.getData()['REVIVE_INDEX_MAX'],
            self.getData()['DIE'],
            self.getData()['DIE_PATH'],
            self.getData()['DIE_INDEX_MAX'],
            pos,
            self.getData()['SIZE'],
            self.getData()['IMAGE_INDEX_MAX']
        )

    def getData(self):
        return data_object.data[self.id]

    def getPosCD(self):
        return self.getData()['POS_CD']

    def getSummonCD(self):
        return self.getData()['SUMMON_CD']

    def getIndexCD(self):
        return self.getData()['IMAGE_INDEX_CD']

    def getSpeed(self):
        return self.getData()['SPEED']

    def getHP(self):
        return self.getData()['HP']

    def getTears(self):
        return self.getData()['TEARS']

    def getDamage(self):
        return self.getData()['DAMAGE']

    def getHPBarIndex(self):
        return self.getData()['HP_BAR_INDEX']

    def isCollide(self, other):
        return self.getRect().colliderect( other.getRect() )

    def checkHit(self, other):
        a = 0 < self.pos[0] - 50 - other.pos[0] < HITBOX
        b = -HITBOX < self.pos[1] - 57 - other.pos[1] < HITBOX
        return a and b

    def update(self):
        self.checkSummon()
        self.checkImageIndex()
        self.checkPos()

    def checkSummon(self):
        if time.time() - self.timeCurSummon <= self.getSummonCD():
            return
        self.timeCurSummon = time.time()
        self.preSummon()

    def checkImageIndex(self):
        if time.time() - self.timeCurIndex <= self.getIndexCD():
            return
        self.timeCurIndex = time.time()

        idx = self.pathIndex + 1
        if self.revive:
            pathIndexCount = self.revivePathIndexCount
        elif self.die:
            pathIndexCount = self.diePathIndexCount
        else:
            pathIndexCount = self.pathIndexCount

        if idx >= pathIndexCount:
            idx = 0
        self.updateIndex(idx)

    def checkPos(self):
        if self.revive or self.die:
            return False

        if time.time() - self.timeCurPos <= self.getPosCD():
            return False
        self.timeCurPos = time.time()
        return True

    def drawHPBar(self, screen, color1, color2):
        image.pygame.draw.rect(screen, color1, (self.pos[0], self.pos[1], self.getHP() * self.getHPBarIndex(), 8))
        image.pygame.draw.rect(screen, color2, (self.pos[0] + self.hp * self.getHPBarIndex(), self.pos[1], (self.getHP() - self.hp) * self.getHPBarIndex(), 8))

    def preSummon(self):
        pass

    def hasSummon(self):
        pass

    def doSummon(self):
        pass