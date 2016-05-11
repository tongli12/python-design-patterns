from abc import ABCMeta, abstractmethod

class Flys(object):
    """ Abstract class of Flys """
    __metaclass__=ABCMeta

    @abstractmethod
    def fly(self):
        pass

class ItFlys(Flys):

    def fly(self):
        return "Flying High"

class CantFly(Flys):

    def fly(self):
        return "I can't fly"

class Animal(object):
    """ Animal class """

    def __init__(self):
        name = ""
        height = 0.0
        weight = 0
        favFood = ""
        speed = 0
        sound = ""

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def setHeight(self, newHeight):
        if newWeight > 0:
            self.height = newHeight
        else:
            print "Height must be bigger than 0"

    def getHeight(self):
        return self.height

    def setWeight(self, newWeight):
        if newWeight > 0:
            self.weight = newWeight
        else:
            print "Weight must be bigger than 0"

    def getHeight(self):
        return self.weight

    def setFavFood(self, newFavFood):
        self.favFood = newFavFood

    def getFavFood(self):
        return self.favFood

    def setSound(self, newSound):
        self.sound = newSound

    def getSound(self):
        return self.sound

    @abstractmethod
    def tryToFly(self):
        pass

    def setFlyingAbility(self, newFlyingType):
        self.flyingType = newFlyingType

class Dog(Animal):

    def __init__(self):
        super(Dog, self).__init__()
        super(Dog, self).setSound('Bark')
        self.flyingType = CantFly()

    def tryToFly(self):
        return self.flyingType.fly()

class Bird(Animal):
    def __init__(self):
        super(Bird, self).__init__()
        super(Bird, self).setSound('Tweet')
        self.flyingType = ItFlys()

    def tryToFly(self):
        return self.flyingType.fly()

if __name__=="__main__":
    sparky = Dog()
    tweety = Bird()

    print "Dog: " + sparky.tryToFly()
    print "Bird: " + tweety.tryToFly()

    sparky.setFlyingAbility(ItFlys())
    print "Dog: " + sparky.tryToFly()
