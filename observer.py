
# coding: utf-8


from abc import ABCMeta, abstractmethod
from threading import Thread


class Subject(object):
    
    #def __init__(self, )
    
    def register(self, newObserver):
        self.action()
        
    def unregister(self, deleteObserver):
        self.action()
    
    def notifyObserver(self):
        self.action()
    
    def action(self):
        raise NotImplementedError('action must be defined')
        
class Observer(object): #(metaclass=ABCMeta):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def update(self, ibmPrice, aaplPrice, googPrice):
        pass

class StockGrabber(Subject):
    
    def __init__(self):
        self.observers = []
        self.ibmPrice = 0.0
        self.aaplPrice = 0.0
        self.googPrice = 0.0
        
    def register(self, newObserver):
        
        self.observers.append(newObserver)
        
    def unregister(self, deleteObserver):
        
        if deleteObserver in self.observers:
            del self.observers[deleteObserver]
    
    def notifyObserver(self):
        
        for observer in self.observers:
            observer.update(self.ibmPrice, self.aaplPrice, self.googPrice)
    
    def setIBMPrice(self, newIBMPrice):
        
        self.ibmPrice = newIBMPrice
        self.notifyObserver()
        
    def setAAPLPrice(self, newAAPLPrice):
        
        self.aaplPrice = newAAPLPrice
        self.notifyObserver()
        
    def setGOOGPrice(self, newGOOGPrice):
        
        self.googPrice = newGOOGPrice
        self.notifyObserver()
        
class StockObserver(Observer):
    
    def __init__(self, stockGrabber):
        
        self.stockGrabber = stockGrabber
        self.stockGrabber.register(self)
    
    def update(self, ibmPrice, aaplPrice, googPrice):
        
        self.ibmPrice = ibmPrice
        self.aaplPrice = aaplPrice
        self.googPrice = googPrice
        
        self.printThePrices()
        
    def printThePrices(self):
        
        print ("IBM: " + str(self.ibmPrice) + "\nAAPL: " + str(self.aaplPrice) +                "\nGOOGPrice: " + str(self.googPrice) + "\n")
        

class GrabStocks(object):
    
    def run(self):
        stockGrabber = StockGrabber()

        stockObserver1 = StockObserver(stockGrabber)

        stockGrabber.setIBMPrice(197.00)
        stockGrabber.setAAPLPrice(667.60)
        stockGrabber.setGOOGPrice(676.40)

        stockObserver2 = StockObserver(stockGrabber)

        stockGrabber.setIBMPrice(197.00)
        stockGrabber.setAAPLPrice(667.60)
        stockGrabber.setGOOGPrice(676.40)

class GetTheStock(object):
    pass

    
if __name__=="__main__":
    test = GrabStocks()
    test.run()
