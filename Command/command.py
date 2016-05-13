
class ElectronicDevice(object):

    def on(self):
        raise NotImplementedError('Subclasses should implement the on method')

    def off(self):
        raise NotImplementedError('Subclasses should implement the off method')

    def volumeUp(self):
        raise NotImplementedError('Subclasses should implement the volumeUp method')

    def volumeDown(self):
        raise NotImplementedError('Subclasses should implement the volumeDown method')

class Radio(ElectronicDevice):
    """ Receiver """
    def __init__(self):
        self.volume = 0

    def on(self):
        print "Radio is on"

    def off(self):
        print "Radio is off"

    def volumeUp(self):
        self.volume += 1
        print "Radio volume is at: " + str(self.volume)

    def volumeDown(self):
        self.volume -= 1
        print "Radio volume is at: " + str(self.volume)

class Television(ElectronicDevice):
    """ Receiver """
    def __init__(self):
        self.volume = 0

    def on(self):
        print "TV is on"

    def off(self):
        print "TV is off"

    def volumeUp(self):
        self.volume += 1
        print "TV volume is at: " + str(self.volume)

    def volumeDown(self):
        self.volume -= 1
        print "TV volume is at: " + str(self.volume)

class Command(object):
    """ Command """
    def execute(self):
        raise NotImplementedError('Subclasses should implement this')

    def undo(self):
        raise NotImplementedError('Subclasses should implement this')

class TurnTVOn(Command):

    def __init__(self, newDevice):
        self.device = newDevice

    def execute(self):
        self.device.on()

    def undo(self):
        self.device.off()

class TurnTVOff(Command):

    def __init__(self, newDevice):
        self.device = newDevice

    def execute(self):
        self.device.off()

    def undo(self):
        self.device.on()

class TurnTVUp(Command):

    def __init__(self, newDevice):
        self.device = newDevice

    def execute(self):
        self.device.volumeUp()

    def undo(self):
        self.device.volumeDown()

class TurnTVDown(Command):

    def __init__(self, newDevice):
        self.device = newDevice

    def execute(self):
        self.device.volumeDown()

    def undo(self):
        self.device.volumeUp()

class TurnAlloff(Command):
    def __init__(self, newDeviceList):
        self.deviceList = newDeviceList

    def execute(self):
        for device in self.deviceList:
            device.off()

    def undo(self):
        for device in self.deviceList:
            device.undo()

class DeviceButton(object):
    """ Invoker """
    def __init__(self, newCommand):
        self.command = newCommand

    def press(self):
        self.command.execute()

    def pressUndo(self):
        self.command.undo()

class TVRemote(object):

    def getDevice(self):

        return Television()


if __name__ == "__main__":

    # Open a tv using TVRemote and turn the volumne up
    tvRemote = TVRemote()
    newDevice = tvRemote.getDevice()
    tvOnCommand = TurnTVOn(newDevice)
    tvVolumeUpCommand = TurnTVUp(newDevice)
    onPressed = DeviceButton(tvOnCommand)
    onPressed.press()

    # Turn off all the devices: TV and Radio
    tv = Television()
    radio = Radio()
    allDevices = [tv, radio]
    turnOffDevice = TurnAlloff(allDevices)
    turnOffDevice.execute()
