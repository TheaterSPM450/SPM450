# SPM450
Theater Project for CSE453

User Manual
To Start
When first opening up the program, you will be notified to calibrate the positions. There are instructions on the calibration page.
To establish the left-most stage position, use the manual left or right buttons to move the cart to the left-most position as desired. Then hit the “Start Point” button.
To establish the right-most stage position, use the manual left or right buttons to move the cart to the right-most position as desired. Then hit the “End Point” button.
Press the “Confirm” button.
When the cart is moving at any speed, there is a slow start of about 1.5 to 2 seconds to avoid a sudden acceleration. Manually sliding the slider does not affect the position and does not perform any function.

Elements of the GUI
Slider - visual representation of where the cart is relative to the start and end positions set by calibration. 
Speed - indicates the speed at which the cart will move at, measured in feet per second
Position - measures the distance between the current position and the motor, in feet
Drive Ratio - the ratio of the driver pulley and driven pulley


Home Page
Speed: displays the currently set speed
Position: displays the current distance from the motor to the cart in the current position, in feet
Drive Ratio: displays the currently set drive ratio (default is 1.0)


Calibrate: a button that when pressed, takes the user to the calibration page
Profile: a button that when pressed, takes the user to the profiles page
Exit: a button that when pressed, closes the program

Speed: adjustable using the plus or minus buttons, in increments of 0.05 ft/s
Drive Ratio: adjustable using the text field to indicate the ratio between
Left Button: a button to press to manually move the cart closer to the motor
Right Button: a button to press to manually move the cart further from the motor


Calibration Page
Start Point: establishes the left-most point of the stage
End Point: establishes the right-most point of the stage
Confirm: confirms the established start and end points of the stage
Set: confirms the entered drive ratio


Profile Page
Done: a button that when pressed, returns the user to the home page
Run: execute the motor/program according to the values currently written in the text fields
Save: save the values in the text fields and write to a csv file stored in the Raspberry Pi
Delete: deletes the csv file indicated in the “Filename” field
Load: opens up stored csv files to load values into text fields

Speed: The speed of the motor is accessible and modifiable in the profile page
Left and Right: manual movements of the motor are accessible and modifiable in the profile page



