import objectbase

class PlaneIce(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super(PlaneIce, self).__init__(id, pos)
        self.hasBullet = False
        self.hasDebuff = True

    def checkPos(self):
        speed = self.getSpeed()
        _ = super(PlaneIce, self).checkPos()
        if _:
            self.pos = self.pos[0] + speed[0] , self.pos[1] + speed[1]
        return _