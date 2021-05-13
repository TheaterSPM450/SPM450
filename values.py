# Global variable file must be imported by files needing access
#    initialized by mainGUI
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

config = ConfigParser()
config.read('spmProps.ini')


def init():
    global START_limit, END_limit, pulley_diameter, drive_ratio, do_loop, SPEED, POSITION, DESTINATION, threads
    global tempStartPosition, tempEndPosition, END_limit, CALIBRATED, go

    START_limit = 0 # always zero
    END_limit = 0 # set during calibration
    pulley_diameter = float(config.get('section_a', 'pulley_diameter')) # diameter in inches, if changed by user or durring profile load, recalibration is needed
    drive_ratio = float(config.get('section_a', 'drive_ratio'))  # set in calibration and profile, if changed by user or durring profile load, recalibration is needed
    do_loop = False # used for thread termination, could be changed to "motor_enable" or something similar
    CALIBRATED = False # set False is calibration needed. Should prevent auto motor operation when false. MUST STILL ALLOW MANUAL OPERATION
    SPEED = float(config.get('section_a', 'speed'))  # pulse sleep time, in seconds as a float (inits to 1 ft/sec)
    POSITION = 0 # an accumulator variable which can be used for current position tracking
    DESTINATION = 0 # destination to reach durring profile program execution
    threads = [] # thread queue

    tempStartPosition = 0 #temp start position used for calibration before the user presses confirm
    tempEndPosition = 0 #temp start position used for calibration before the user presses confirm
    positionDisplayList = []
    go = True
