# from main import *

class Barrel:
    volume = None  # 2.5 м^3 или 48Y (??? иностранный образец - около 4 м^3 ????)
    temp = None  # 55 по цельсию предел
    pressure = None  # Давление в резервуаре kPa
    itsWorking = None  # true / false
    index = None  # Индекс в Section1switches

    def __init__(self, itsWorking=None, volume=None, temp=None, pressure=None, index=None):
        self.volume = volume
        self.temp = temp
        self.pressure = pressure
        self.itsWorking = itsWorking
        self.index = index

    def set_vallue_barrel(self, temp=None, pressure=None):
        self.temp = temp
        self.pressure = pressure


    def get_info_barrel(self):
        return [self.itsWorking, self.volume, self.temp, self.pressure, self.index]


class MSens:
    index = None  # Индекс в массиве
    itsWorking = None  # true / false

    def __init__(self, index=None, itsWorking=None):
        self.index = index
        self.itsWorking = itsWorking