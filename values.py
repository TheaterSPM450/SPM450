# Global variable file must be imported by files needing access
#    initialized by mainGUI



def init():
    global START_limit, END_limit, pulley_diameter, drive_ratio, do_loop, SPEED, POSITION, DESTINATION, threads
    global tempStartPosition, tempEndPosition, END_position, CALIBRATED

    START_limit = 0 # always zero
    END_position = 0 # set during calibration
    pulley_diameter = 1.5 # diameter in inches, if changed by user or durring profile load, recalibration is needed
    drive_ratio = 1.0 # set in calibration and profile, if changed by user or durring profile load, recalibration is needed
    do_loop = False # used for thread termination, could be changed to "motor_enable" or something similar
    CALIBRATED = False # set False is calibration needed. Should prevent auto motor operation when false. MUST STILL ALLOW MANUAL OPERATION
    SPEED = .0005 # pulse sleep time, in seconds as a float
    POSITION = 0 # an accumulator variable which can be used for current position tracking
    DESTINATION = 0 # destination to reach durring profile program execution
    threads = [] # thread queue

    tempStartPosition = 0 #temp start position used for calibration before the user presses confirm
    tempEndPosition = 0 #temp start position used for calibration before the user presses confirm
