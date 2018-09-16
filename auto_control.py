#!/usr/bin/python

import time
import schedule

from myhome import MyHome

print('START', flush=True)
home = MyHome()
print('Home instance is initialized.', flush=True)


def reset_home():
    global home
    home = MyHome()


def set_fan(room, level):

    def bed():
        home.set_fan_bedroom(level)

    def liv():
        home.set_fan_living_room(level)

    if room == 'bed':
        return bed

    if room == 'liv':
        return liv


# schedule reset client
schedule.every().day.at("01:00").do(reset_home)

# schedule for living room air purifier
schedule.every().day.at("07:00").do(set_fan('liv', 3))
schedule.every().day.at("07:30").do(set_fan('liv', 2))
schedule.every().day.at("10:00").do(set_fan('liv', 3))
schedule.every().day.at("11:00").do(set_fan('liv', 2))
schedule.every().day.at("13:00").do(set_fan('liv', 0))
schedule.every().day.at("16:30").do(set_fan('liv', 3))
schedule.every().day.at("17:00").do(set_fan('liv', 2))
schedule.every().day.at("19:00").do(set_fan('liv', 1))
schedule.every().day.at("23:00").do(set_fan('liv', 0))

# schedule for bedroom air purifier
schedule.every().day.at("07:00").do(set_fan('bed', 2))
schedule.every().day.at("23:00").do(set_fan('bed', 1))

while True:
    schedule.run_pending()
    time.sleep(1)
