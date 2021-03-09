from tkinter import *

root=Tk()
root.title('Non-interactable Slider')
root.geometry("800x400")

sliderValue = IntVar()
sliderValue.set(0)

def setSliderValue():
	sliderValue.set(int(textbox.get()))

	if sliderValue.get()==5:
		horiSlider.configure(bg="green")
	else:
		horiSlider.configure(bg="SystemButtonFace")


horiSlider = Scale(root, from_=0,to=10, orient=HORIZONTAL, variable=sliderValue, length=600,state=DISABLED)
horiSlider.pack()

textbox=Entry(root,width=10)
textbox.pack()

setSliderValueButton=Button(root,text="Set Value",command=setSliderValue)
setSliderValueButton.pack()

root.mainloop()