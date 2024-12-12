import objectbase
import timer
import random
from const import *

class BossStage2(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super(BossStage2, self).__init__(id, pos)
        self.direction = 0
        self.changeDirectionCD = 3
        self.timeCurChangeDirect = 0

    def checkPos(self):
        speed = self.getSpeed()
        left = LEFT_BORDER_FOR_BOSS_STAGE2 + speed[0]
        right =  RIGHT_BORDER_FOR_BOSS_STAGE2 - speed[0]
        up = UP_BORDER_FOR_BOSS_STAGE2 + speed[1]
        down = DOWN_BORDER_FOR_BOSS_STAGE2 - speed[1]
        touchBorder = -25 <= self.pos[0] - left <= 25 or -25 <= self.pos[0] - right <= 25\
                      or -25 <= self.pos[1] - up <= 25 or -25 <= self.pos[1] - down <= 25
        if timer.getTotalTime() - self.timeCurChangeDirect > self.changeDirectionCD or touchBorder:
            self.timeCurChangeDirect = timer.getTotalTime()
            self.direction = random.randint(0, 3)
        _ = super(BossStage2, self).checkPos()
        if _:
            if self.direction == 0 and self.pos[0] >= left:
                self.left = True
                self.right = False
                self.pos[0] -= speed[0]
            elif self.direction == 1 and self.pos[1] <= down:
                self.pos[1] += speed[1]
            elif self.direction == 2 and self.pos[0] <= right:
                self.left = False
                self.right = True
                self.pos[0] += speed[0]
            elif self.direction == 3 and self.pos[1] >= up:
                self.pos[1] -= speed[1]
        return _