# __BlueAir Air Purifier Scheduler__


## __Stack__
* auto_control.py (you can use supervisor to control this process)
* myhome.py (define your IoT devices at your home)
* blueair.py (blueair API)
* config.py (config file for blueair API)

## __Introduction__
* This is a BlueAir purifier automatic scheduler, which makes life easier. You can schedule running mode and time of the BlueAir air purifier to control the air quality in your home automatically.

## __Get started__
1. Change your email and password in _config.py_.
2. `from blueair import BlueAir`
3. `bl = BlueAir()`
4. `print(bl.get_device_info())  # get uuid of your air purifier and copy to config.py`
5. Change your myhome.py and/or auto_control.py to manage your devices at home and your schedule.
6. Run auto_control.py (you can use a supervisor to manage the process)

## __Reference__
[homebridge-blueair](https://github.com/mylesgray/homebridge-blueair)

