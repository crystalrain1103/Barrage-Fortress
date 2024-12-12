import objectbase

class ConvictionBullet(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super(ConvictionBullet, self).__init__(id, pos)

    def checkPos(self):
        speed = self.getSpeed()
        _ = super(ConvictionBullet, self).checkPos()
        if _:
            self.pos = self.pos[0] + speed[0] , self.pos[1] + speed[1]
        return _