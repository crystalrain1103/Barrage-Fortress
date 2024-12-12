import objectbase

class NormalBullet(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super(NormalBullet, self).__init__(id, pos)
        self.direct = (1, 1)

    def setDirect(self, a, b):
        self.direct = (a, b)

    def checkPos(self):
        speed = self.getSpeed()
        direct = self.direct
        _ = super(NormalBullet, self).checkPos()
        if _:
            self.pos = self.pos[0] + speed[0] * direct[0], self.pos[1] + speed[1] * direct[1]
        return _