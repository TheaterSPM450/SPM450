from tkinter import *
import time
import threading

#vars
do_loop = FALSE

tk = Tk() # tk object


# loop function to run on thread
def startloopevent():
    global do_loop
    do_loop = TRUE
    x = 0
    countlim = 1000
    while(do_loop and x < countlim):
        tk.configure(bg='green')
        print("ON")
        time.sleep(.1)
        tk.configure(bg='yellow')
        print("OFF")
        time.sleep(.1)
        x += 1


# stop thread function
def stoploopevent():
    global do_loop
    do_loop = FALSE
    # th.destroy()
    # th.join()


# thread start function
def st_thread():
    th = threading.Thread(target=startloopevent) # create new thread running startloopevent function
    th.start()


def exitProgram():
	print("Exit Button pressed")
	tk.destroy()


spinLeftButton = Button(tk, text="START Thread", command=st_thread, height = 5, width =10 )
spinLeftButton.pack()

stopButton = Button(tk, text="STOP Thread", command=stoploopevent, height = 5, width =10)
stopButton.pack()

exitButton  = Button(tk, text = "Exit", command = exitProgram, height =2 , width = 10) 
exitButton.pack(side = BOTTOM)

tk.mainloop()