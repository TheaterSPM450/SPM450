# spm_control_akogan.py
#
# AUTHOR: Alex Kogan
# Date: 3/12/2021
#
# OVERVIEW: This file contains control functions for the SPM450 software


from math import pi


# calcRPM()
# takes a rpm value and returns a sleep duration
# value in terms of seconds for motor rpm control
#
# calculates 1 second divived by rpm value divided
# by 60, time 400(2 phase halfs times 200 pulses per revolution)
#
# INPUT: integer
# OUTPUT: float
def calcRPM_pulse(rpm):
#    print((1 / (400 * (rpm / 60))))
    return (1 / (400 * (rpm / 60)))


# rpm_to_speed()
# takes rpm[integer] and pulley diameter[float] and returns
# a linear speed in miles/hr (mph)
#
# INPUT: float, float
# OUTPUT: float
def rpm_to_speed(rpm, diameter):
    minutes = 60
    inches_per_mile = 63360
    r = diameter / 2 # calculate radius
    circumference = 2 * pi * r
    return ((circumference * rpm * minutes) / inches_per_mile)


# speed_to_rpm()
# takes speed[float] in miles per hour (mph) and pulley diameter[float]
# and returns an rpm[float]
#
# INPUT: float, float
# OUTPUT: float
def speed_to_rpm(speed, diameter):
    minutes = 60
    inches_per_mile = 63360
    r = diameter / 2 # calculate radius
    circumference = 2 * pi * r
    return ((inches_per_mile * speed) / (minutes * circumference))


# speed_to_pulse_time()
# 
#
# INPUTS:
#   speed - speed of cart as a float value representing miles per hour
#   drive_pulley_diameter - diameter of drive pulley in inches as a float value
#   drive_ratio - final gear ratio of drive as a float value
#
# OUTPUT: float decimal representing fraction of a second between driver pulse phases
def speed_to_pulse_time(speed, drive_pulley_diameter, drive_ratio):
    motor_speed = speed / drive_ratio
    return calcRPM_pulse(speed_to_rpm(motor_speed, drive_pulley_diameter))