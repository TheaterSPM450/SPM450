<<<<<<< HEAD
from tkinter import *

root = Tk()
root.title("Status Bar")

number_list = [1,2,3,4,5,6,7,8,9,10]
# myLabel is for testing and debugging purposes
myLabel = Label(root, text="Number " + str(number_list[0]) + " and index is 0")
myLabel.grid(row=0, column=0, columnspan=3)

def rightClick(currentIndex): # currentIndex refers to the index of number_list CURRENTLY displayed
	global myLabel, rightButton, leftButton
	global oneb, twob, threeb, fourb, fiveb, sixb, sevenb, eightb, nineb, tenb

	myLabel.grid_forget() # this needs to be modified... to display updated element, you must remove it from the grid
	myLabel = Label(text="Number " + str(number_list[currentIndex+1]) + " which is index & newCurrentIndex" + str(currentIndex+1))
	newCurrentIndex = currentIndex + 1 # newCurrentIndex refers to index of number_list that SHOULD BE NOW displayed
	rightButton = Button(root, text="Right", command=lambda: rightClick(newCurrentIndex)) # call the same functions again, but this time, with the new argument (since we changed currentIndex and newCurrentIndex)
	leftButton = Button(root, text="Left", command=lambda: leftClick(newCurrentIndex)) # call the same functions again, but this time, with the new argument (since we changed currentIndex and newCurrentIndex)

	if newCurrentIndex == 9: # if current number displayed == 10, rightButton cannot be clicked
		rightButton = Button(root, text="Right", state=DISABLED)
		
	myLabel.grid(row=0, column=0, columnspan=3) # this has been modified, and to display it, you must put it back onto the grid
	leftButton.grid(row=2, column=0)
	rightButton.grid(row=2, column=2)

	# reverts the previously selected/green button back to normal default color button
	button_list[currentIndex].grid_forget()
	button_list[currentIndex] = Button(root, text=str(currentIndex+1), height=1, width=3)
	button_list[currentIndex].grid(row=1,column=currentIndex)
	# changes the new button to a green button
	button_list[newCurrentIndex].grid_forget()
	button_list[newCurrentIndex] = Button(root, text=str(newCurrentIndex+1), height=1, width=3, bg="light green")
	button_list[newCurrentIndex].grid(row=1,column=newCurrentIndex)

def leftClick(currentIndex): # currentIndex refers to the index of number_list CURRENTLY displayed
	global myLabel, rightButton, leftButton
	global oneb, twob, threeb, fourb, fiveb, sixb, sevenb, eightb, nineb, tenb

	myLabel.grid_forget() # this needs to be modified... to display updated element, you must remove it from the grid
	myLabel = Label(text="Number " + str(number_list[currentIndex-1]) + " which is index & newCurrentIndex" + str(currentIndex-1))
	newCurrentIndex = currentIndex - 1
	rightButton = Button(root, text="Right", command=lambda: rightClick(newCurrentIndex))
	leftButton = Button(root, text="Left", command=lambda: leftClick(newCurrentIndex))
	
	if newCurrentIndex == 0: # if current number displayed == 1, rightButton cannot be clicked
		leftButton = Button(root, text="Left", state=DISABLED)
		
	myLabel.grid(row=0, column=0, columnspan=3) # this has been modified, and to display it, you must put it back onto the grid
	leftButton.grid(row=2, column=0)
	rightButton.grid(row=2, column=2)

	# reverts the previously selected/green button back to normal default color button
	button_list[currentIndex].grid_forget()
	button_list[currentIndex] = Button(root, text=str(currentIndex+1), height=1, width=3)
	button_list[currentIndex].grid(row=1,column=currentIndex)
	# changes the new button to a green button
	button_list[newCurrentIndex].grid_forget()
	button_list[newCurrentIndex] = Button(root, text=str(newCurrentIndex+1), height=1, width=3, bg="light green")
	button_list[newCurrentIndex].grid(row=1,column=newCurrentIndex)

# initiates the leftButton and rightButton
leftButton = Button(root, text="Left", state=DISABLED)
leftButton.grid(row=2, column=0)
rightButton = Button(root, text="Right", command=lambda: rightClick(0)) #program will start at 1, and can only go right, so rightButton will have function
rightButton.grid(row=2, column=2)

# creates all numbered buttons, from 1 to 10
# these buttons will have no function, and at the start, only oneb (numbered 1) will have color
oneb = Button(root, text="1", height=1, width=3, bg="light green")
oneb.grid(row=1,column=0)
twob = Button(root, text="2", height=1, width=3)
twob.grid(row=1,column=1)
threeb = Button(root, text="3", height=1, width=3)
threeb.grid(row=1,column=2)
fourb = Button(root, text="4", height=1, width=3)
fourb.grid(row=1,column=3)
fiveb = Button(root, text="5", height=1, width=3)
fiveb.grid(row=1,column=4)
sixb = Button(root, text="6", height=1, width=3)
sixb.grid(row=1,column=5)
sevenb = Button(root, text="7", height=1, width=3)
sevenb.grid(row=1,column=6)
eightb = Button(root, text="8", height=1, width=3)
eightb.grid(row=1,column=7)
nineb = Button(root, text="9", height=1, width=3)
nineb.grid(row=1,column=8)
tenb = Button(root, text="10", height=1, width=3)
tenb.grid(row=1,column=9)
button_list = [oneb, twob, threeb, fourb, fiveb, sixb, sevenb, eightb, nineb, tenb]

root.mainloop()
=======
from tkinter import *

root = Tk()
root.title("Status Bar")

number_list = [1,2,3,4,5,6,7,8,9,10]
# myLabel is for testing and debugging purposes
myLabel = Label(root, text="Number " + str(number_list[0]) + " and index is 0")
myLabel.grid(row=0, column=0, columnspan=3)

def rightClick(currentIndex): # currentIndex refers to the index of number_list CURRENTLY displayed
	global myLabel, rightButton, leftButton
	global oneb, twob, threeb, fourb, fiveb, sixb, sevenb, eightb, nineb, tenb

	myLabel.grid_forget() # this needs to be modified... to display updated element, you must remove it from the grid
	myLabel = Label(text="Number " + str(number_list[currentIndex+1]) + " which is index & newCurrentIndex" + str(currentIndex+1))
	newCurrentIndex = currentIndex + 1 # newCurrentIndex refers to index of number_list that SHOULD BE NOW displayed
	rightButton = Button(root, text="Right", command=lambda: rightClick(newCurrentIndex)) # call the same functions again, but this time, with the new argument (since we changed currentIndex and newCurrentIndex)
	leftButton = Button(root, text="Left", command=lambda: leftClick(newCurrentIndex)) # call the same functions again, but this time, with the new argument (since we changed currentIndex and newCurrentIndex)

	if newCurrentIndex == 9: # if current number displayed == 10, rightButton cannot be clicked
		rightButton = Button(root, text="Right", state=DISABLED)
		
	myLabel.grid(row=0, column=0, columnspan=3) # this has been modified, and to display it, you must put it back onto the grid
	leftButton.grid(row=2, column=0)
	rightButton.grid(row=2, column=2)

	# reverts the previously selected/green button back to normal default color button
	button_list[currentIndex].grid_forget()
	button_list[currentIndex] = Button(root, text=str(currentIndex+1), height=1, width=3)
	button_list[currentIndex].grid(row=1,column=currentIndex)
	# changes the new button to a green button
	button_list[newCurrentIndex].grid_forget()
	button_list[newCurrentIndex] = Button(root, text=str(newCurrentIndex+1), height=1, width=3, bg="light green")
	button_list[newCurrentIndex].grid(row=1,column=newCurrentIndex)

def leftClick(currentIndex): # currentIndex refers to the index of number_list CURRENTLY displayed
	global myLabel, rightButton, leftButton
	global oneb, twob, threeb, fourb, fiveb, sixb, sevenb, eightb, nineb, tenb

	myLabel.grid_forget() # this needs to be modified... to display updated element, you must remove it from the grid
	myLabel = Label(text="Number " + str(number_list[currentIndex-1]) + " which is index & newCurrentIndex" + str(currentIndex-1))
	newCurrentIndex = currentIndex - 1
	rightButton = Button(root, text="Right", command=lambda: rightClick(newCurrentIndex))
	leftButton = Button(root, text="Left", command=lambda: leftClick(newCurrentIndex))
	
	if newCurrentIndex == 0: # if current number displayed == 1, rightButton cannot be clicked
		leftButton = Button(root, text="Left", state=DISABLED)
		
	myLabel.grid(row=0, column=0, columnspan=3) # this has been modified, and to display it, you must put it back onto the grid
	leftButton.grid(row=2, column=0)
	rightButton.grid(row=2, column=2)

	# reverts the previously selected/green button back to normal default color button
	button_list[currentIndex].grid_forget()
	button_list[currentIndex] = Button(root, text=str(currentIndex+1), height=1, width=3)
	button_list[currentIndex].grid(row=1,column=currentIndex)
	# changes the new button to a green button
	button_list[newCurrentIndex].grid_forget()
	button_list[newCurrentIndex] = Button(root, text=str(newCurrentIndex+1), height=1, width=3, bg="light green")
	button_list[newCurrentIndex].grid(row=1,column=newCurrentIndex)

# initiates the leftButton and rightButton
leftButton = Button(root, text="Left", state=DISABLED)
leftButton.grid(row=2, column=0)
rightButton = Button(root, text="Right", command=lambda: rightClick(0)) #program will start at 1, and can only go right, so rightButton will have function
rightButton.grid(row=2, column=2)

# creates all numbered buttons, from 1 to 10
# these buttons will have no function, and at the start, only oneb (numbered 1) will have color
oneb = Button(root, text="1", height=1, width=3, bg="light green")
oneb.grid(row=1,column=0)
twob = Button(root, text="2", height=1, width=3)
twob.grid(row=1,column=1)
threeb = Button(root, text="3", height=1, width=3)
threeb.grid(row=1,column=2)
fourb = Button(root, text="4", height=1, width=3)
fourb.grid(row=1,column=3)
fiveb = Button(root, text="5", height=1, width=3)
fiveb.grid(row=1,column=4)
sixb = Button(root, text="6", height=1, width=3)
sixb.grid(row=1,column=5)
sevenb = Button(root, text="7", height=1, width=3)
sevenb.grid(row=1,column=6)
eightb = Button(root, text="8", height=1, width=3)
eightb.grid(row=1,column=7)
nineb = Button(root, text="9", height=1, width=3)
nineb.grid(row=1,column=8)
tenb = Button(root, text="10", height=1, width=3)
tenb.grid(row=1,column=9)
button_list = [oneb, twob, threeb, fourb, fiveb, sixb, sevenb, eightb, nineb, tenb]

root.mainloop()
>>>>>>> 04c5c638b093ec6725c2f11d7bca650962592ced
