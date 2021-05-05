# spm_control_akogan.py
#
# AUTHOR: Alex Kogan
# Date: 3/12/2021
#
# OVERVIEW: (4/24/21 Revision) This file contains control math functions for the SPM450 software.
# Further information detailed in function comments.
#


from math import pi


# position_to_distance()
# IMPORTANT: the output of this function is only intended for GUI/user display purposes
#            not for control purposes
# takes position count, converts to distance in feet:
#   takes postion (motor pulses), transfer pulley diameter (inches), drive ratio
#   and calculates position from calibration start point (zero point) in feet 
# 
# calculates pulley circumference in feet
# returns distance by dividing position count by steps per revolution (200) * transfer pulley circumference * drive ratio
#
# INPUT: float, float, float
# OUTPUT: float
def position_to_distance(position, pulley_diameter, drive_ratio):
    pulley_circumference_ft = (pulley_diameter * pi) / 12
    return (position / 200) * pulley_circumference_ft * drive_ratio


# rpm_to_pulsesleep()
# takes a rpm value and returns a sleep duration
# value in terms of seconds for motor rpm control
#
# calculates 1 second divived by rpm value divided
# by 60, time 400(2 phase halfs times 200 pulses per revolution)
#
# INPUT: integer
# OUTPUT: float
def rpm_to_pulsesleep(rpm):
#    print((1 / (400.0 * (rpm / 60.0))))
    return (1 / (400.0 * (rpm / 60.0)))


# sleep_to_rpm()
# converts sleep delay to time (Speed) to rpm
#
#
#
def sleep_to_rpm(t):
    return ((1 / t) / (400)) * 60 # RPM = ((1 second / sleeptime) / (2 phases * 200 pulses_per_rotation)) * 60 seconds


# rpm_to_speed()
# takes rpm[integer] and pulley diameter[float] and returns
# a linear speed in miles/hr (mph)
#
# INPUT: float, float
# OUTPUT: float
def rpm_to_speed(rpm, diameter):
    minutes = 60.0
    inches_per_mile = 63360.0
    circumference = diameter * pi
    return ((circumference * rpm * minutes) / inches_per_mile)


# speed_to_rpm()
# takes speed[float] in miles per hour (mph) and pulley diameter[float]
# and returns an rpm[float]
#
# INPUT: float, float
# OUTPUT: float
def speed_to_rpm(speed, diameter):
    minutes = 60.0
    inches_per_mile = 63360.0
    circumference = diameter * pi
    return ((inches_per_mile * speed) / (minutes * circumference))


# speed_to_pulse_time()
# 
#
# INPUTS:
#   speed - speed of cart as a float value representing miles per hour
#   drive_pulley_diameter - diameter of driven pulley (not motor pulley) in inches as a float value
#   drive_ratio - final gear ratio of drive as a float value
#
# OUTPUT: float decimal representing fraction of a second between driver pulse phases
def speed_to_pulse_time(speed, driven_pulley_diameter, drive_ratio):
    return rpm_to_pulsesleep(speed_to_rpm(speed, driven_pulley_diameter) / drive_ratio)


# to test pulley diameter and ratio pulse times uncomment and plug in test values
# as (speed(mph), transfer pulley diameter(inches), ratio(if direct drive use 1.0))

pulseT = speed_to_pulse_time(1.5, .4375, 3.0)
rpm = sleep_to_rpm(pulseT)
print("\n========================================\n")
print("Pulse time: " + str(pulseT))
print("RPM: " + str(rpm))
print("distance: " + str(round(position_to_distance(200.0, 3.819718634, 1.0), 2)))
# print("RPM t: " + str(rpm_to_pulsesleep(60)))

print("\n========================================\n")