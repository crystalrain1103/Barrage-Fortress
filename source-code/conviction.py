import objectbase
import convictionbullet
import time
from const import *

class Conviction(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super(Conviction, self).__init__(id, pos)
        self.hasBullet = False
        self.hasBuffed = False
        self.hasDebuffed = False
        self.getBuffTime = 0
        self.lastShootTime = 0

    def doMove(self, key):
        speed = self.getSpeed()
        if key is K_a and self.pos[0] - speed[0] >= LEFT_BORDER_FOR_STAFF:
            self.pos[0] -= speed[0]
        elif key is K_s and self.pos[1] + speed[1] <= DOWN_BORDER_FOR_STAFF:
            self.pos[1] += speed[1]
        elif key is K_d and self.pos[0] + speed[0] <= RIGHT_BORDER_FOR_STAFF:
            self.pos[0] += speed[0]
        elif key is K_w and  self.pos[1] - speed[1] >= UP_BORDER_FOR_STAFF:
            self.pos[1] -= speed[1]

    def preSummon(self):
        self.hasBullet = True

    def hasSummon(self):
        return self.hasBullet

    def preBuffed(self, gameTime):
        self.hasBuffed = True
        self.getBuffTime = gameTime

    def removeBuffed(self):
        self.hasBuffed = False

    def isBuffed(self):
        return self.hasBuffed

    def preDebuffed(self):
        self.hasDebuffed = True

    def removeDebuffed(self):
        self.hasDebuffed = False

    def isDebuffed(self):
        return self.hasDebuffed

    def doSummon(self):
        if self.isBuffed():
            final_tears = self.tears / BUFF_BONUS
        else:
            final_tears = self.tears

        if self.isDebuffed():
            final_tears *= DEBUFF_EFFECT

        if time.time() - self.lastShootTime <= final_tears:
            return

        self.lastShootTime = time.time()
        if self.hasSummon():
            self.hasBullet = False
            if self.isBuffed():
                bullet1 = convictionbullet.ConvictionBullet(CONVICTION_BULLET_ID, (self.pos[0] + 20, self.pos[1]))
                bullet2 = convictionbullet.ConvictionBullet(CONVICTION_BULLET_ID, (self.pos[0] + 20, self.pos[1] + 25))
                bullet3 = convictionbullet.ConvictionBullet(CONVICTION_BULLET_ID, (self.pos[0] + 20, self.pos[1] + 50))
                return bullet1, bullet2, bullet3
            else:
                bullet = convictionbullet.ConvictionBullet(CONVICTION_BULLET_ID, (self.pos[0] + 20, self.pos[1] + 25))
                return bullet,