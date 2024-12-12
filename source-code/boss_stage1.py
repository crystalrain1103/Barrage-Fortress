import objectbase
import timer
import time
import random
import normalbullet
import specialbullet
from const import *

class BossStage1(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super(BossStage1, self).__init__(id, pos)
        self.direction = 0
        self.changeDirectionCD = 10
        self.timeCurChangeDirect = 0
        self.lastShootTime = time.time()
        self.hasBullet = False
        self.shootType = 'special1'
        self.hasRevive = True

    def checkPos(self):
        speed = self.getSpeed()
        left = LEFT_BORDER_FOR_BOSS_STAGE1 + speed[0]
        right =  RIGHT_BORDER_FOR_BOSS_STAGE1 - speed[0]
        up = UP_BORDER_FOR_BOSS_STAGE1 + speed[1]
        down = DOWN_BORDER_FOR_BOSS_STAGE1 - speed[1]
        touchBorder = -25 <= self.pos[0] - left <= 25 or -25 <= self.pos[0] - right <= 25\
                      or -25 <= self.pos[1] - up <= 25 or -25 <= self.pos[1] - down <= 25
        if timer.getTotalTime() - self.timeCurChangeDirect > self.changeDirectionCD or touchBorder:
            self.timeCurChangeDirect = timer.getTotalTime()
            self.direction = random.randint(0, 3)
        _ = super(BossStage1, self).checkPos()
        if _:
            if self.direction == 0 and self.pos[0] > LEFT_BORDER_FOR_BOSS_STAGE1:
                self.left = True
                self.right = False
                self.pos[0] -= speed[0]
            elif self.direction == 1 and self.pos[1] < DOWN_BORDER_FOR_BOSS_STAGE1:
                self.pos[1] += speed[1]
            elif self.direction == 2 and self.pos[0] < RIGHT_BORDER_FOR_BOSS_STAGE1:
                self.left = False
                self.right = True
                self.pos[0] += speed[0]
            elif self.direction == 3 and self.pos[1] > UP_BORDER_FOR_BOSS_STAGE1:
                self.pos[1] -= speed[1]
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
            if self.shootType == 'special1':
                bullet = self.spawnBullet('special')
                self.shootType = 'normal'
            elif self.shootType == 'normal':
                bullet = self.spawnBullet('normal')
                self.shootType = 'special2'
            else:
                bullet = self.spawnBullet('special')
                self.shootType = 'special1'

            return bullet

    def spawnBullet(self, mode):
        bullet = []
        if mode == 'normal':
            for i in range(8):
                bullet.append(normalbullet.NormalBullet(NORMAL_BULLET_ID, self.pos))
        elif mode == 'special':
            for i in range(8):
                bullet.append(specialbullet.SpecialBullet(SPECIAL_BULLET_ID, self.pos))
        else:
            pass

        if len(bullet) != 0:
            bullet[0].setDirect(1, 0)
            bullet[1].setDirect(1, 1)
            bullet[2].setDirect(0, 1)
            bullet[3].setDirect(-1, 1)
            bullet[4].setDirect(-1, 0)
            bullet[5].setDirect(-1, -1)
            bullet[6].setDirect(0, -1)
            bullet[7].setDirect(1, -1)

        return bullet