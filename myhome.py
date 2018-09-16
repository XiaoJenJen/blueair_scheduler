from blueair import BlueAir
import config
from datetime import datetime


class MyHome:

    def __init__(self):
        self.ap = BlueAir()

    def set_fan_bedroom(self, level):
        print(f"{datetime.now()}: Set bedroom fan to {level}", flush=True)
        self.ap.set_fan(config.uuid_bedroom, level)

    def set_fan_living_room(self, level):
        print(f"{datetime.now()}: Set living room fan to {level}", flush=True)
        self.ap.set_fan(config.uuid_livingroom, level)
