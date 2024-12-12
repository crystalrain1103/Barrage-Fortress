import objectbase

class Heal(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super(Heal, self).__init__(id, pos)
        self.hasHeal = True

    def checkPos(self):
        speed = self.getSpeed()
        _ = super(Heal, self).checkPos()
        if _:
            self.pos = ( self.pos[0] + speed[0] , self.pos[1] + speed[1] )
        return _