from tkinter import *
import time
import configparser
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

#We should run this snippet of code at the top, then update variables using "set" upon choosing a certain speed and so on

# instantiate
config = ConfigParser()
# parse existing file
config.read('spmProps.ini')

# read values from a section
globalUser = config.get('section_a', 'string_val_user')
globalMetricForSpeed = config.get('section_a', 'string_val_inchFeetCentimeterPerSecond')
globalSysOnOff = config.getboolean('section_a', 'bool_val_SystemOnMeansTrue')
globalPropPosition = config.getint('section_a', 'int_val_propPosition')
globalSpeed = config.getfloat('section_a', 'float_val_speed')

print(globalUser)
print(globalMetricForSpeed)
print(globalSysOnOff)
print(globalPropPosition)
print(globalSpeed)

# update existing value
config.set('section_a', 'string_val_user', 'Arman')

# add a new section and some values
config.add_section('section_b')
config.set('section_b', 'Krishna', 'tallAF')
config.set('section_b', 'Josh', 'TheBoss')

# save to a file just for testing
with open('test_update.ini', 'w') as configfile:
    config.write(configfile)