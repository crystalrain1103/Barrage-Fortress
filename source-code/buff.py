import objectbase

class Buff(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super(Buff, self).__init__(id, pos)
        self.hasBuff = True

    def checkPos(self):
        speed = self.getSpeed()
        _ = super(Buff, self).checkPos()
        if _:
            self.pos = ( self.pos[0] + speed[0] , self.pos[1] + speed[1] )
        return _