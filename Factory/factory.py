
from abc import ABCMeta, abstractmethod

class EnemyShip(object):
    """ Abstract Energyship class """
    __metaclass__ = ABCMeta

    def __init__(self):
        name = ''
        amtDamage = 0.0

    @abstractmethod
    def getName(self):
        return self.name

    @abstractmethod
    def setName(self, newName):
        self.name = newName

    @abstractmethod
    def getDamage(self):
        return amtDamage

    @abstractmethod
    def setDamage(self, newDamage):
        self.amtDamage = newDamage

    def followHeroShip(self):
        print self.getName() + " is following the hero"

    def displayEnemyShip(self):
        print self.getName() + " is on the screen"

    def enemyShipShoots(self):
        print self.getName() + " attachs and does " + self.getDamage() + " damage to hero"

class UFOEnemyShip(EnemyShip):

    def __init__(self):
        super(UFOEnemyShip, self).__init__()
    #EnemyShip.__init__(self)
    def setName(self):
        super(UFOEnemyShip, self).setName('UFO Enegy Ship')

    def getName(self):
        return super(UFOEnemyShip, self).getName()

    def setDamage(self):
        super(UFOEnemyShip, self).setDamage(20.0)

    def getDamage(self):
        return super(UFOEnemyShip, self).getDamage()

class EnemyShipFactory(object):
    """Enemy ship factory """
    def makeEnemyShip(self, newShipType):
        if newShipType == 'U':
            return UFOEnemyShip()
        elif newShipType =='R':
            return RocketEnemyShip()
        elif newShipType == 'B':
            return BigUFOEnemyShip()
        else:
            return None

if __name__ == "__main__":
    #newShip = EnemyShip()
    #newShip = UFOEnemyShip()
    shipFactory = EnemyShipFactory()
    UFOShip = shipFactory.makeEnemyShip('U')
    print type(UFOShip)
    UFOShip.setName()
    print UFOShip.getName()
    UFOShip.displayEnemyShip()
