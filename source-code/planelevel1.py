import objectbase
import time
import normalbullet
from const import *

class PlaneLevel1(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super(PlaneLevel1, self).__init__(id, pos)
        self.hasBullet = False
        self.lastShootTime = time.time()

    def checkPos(self):
        speed = self.getSpeed()
        _ = super(PlaneLevel1, self).checkPos()
        if _:
            self.pos = self.pos[0] + speed[0] , self.pos[1] + speed[1]
        return _

    def preSummon(self):
        self.hasBullet = True

    def hasSummon(self):
        return self.hasBullet

    def doSummon(self):
        if time.time() - self.lastShootTime <= self.tears:
            return

        self.lastShootTime = time.time()

        if self.hasSummon():
            self.hasBullet = False
            bullet = normalbullet.NormalBullet(NORMAL_BULLET_ID, self.pos)
            bullet.setDirect(-1, 0)
            return bullet,