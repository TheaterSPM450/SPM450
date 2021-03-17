from tkinter import *

root=Tk()
root.title('Non-interactable Slider') #title of the program
root.geometry("800x400") #size of the program

sliderValue = IntVar() #declaring an int in tkinter
sliderValue.set(0) #initializing it to zero

def setSliderValue(): #sets the slider value
	sliderValue.set(int(textbox.get())) #set the variable equal to the value in textbox

	if sliderValue.get()==5: #check if value is 5
		horiSlider.configure(bg="green") #if it is, change the color to green
	else:
		horiSlider.configure(bg="SystemButtonFace") #if it is not, change the color back to default

#initialize a horizontal slider
horiSlider = Scale(root, from_=0,to=10, orient=HORIZONTAL, variable=sliderValue, length=600,state=DISABLED)
horiSlider.pack() #pack the slider

textbox=Entry(root,width=10) #adds a textbox
textbox.pack()

setSliderValueButton=Button(root,text="Set Value",command=setSliderValue) #button to set the value
setSliderValueButton.pack()

root.mainloop()