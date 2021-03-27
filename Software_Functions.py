from tkinter import *
import csv
import os

# This tracks the position of the prop, and is used in the position_up and position_down functions.
# (as of 3-27-201 it is only for testing)
position = 0


def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries


def fetch(entries):
    csv_list = []
    text = ''
    for entry in entries:
        text  = entry[1].get()
        if entry[0] == 'filename':
            break
        csv_list.append(text)
    filename = os.getcwd() + "/csv/" + text + '.csv'
    file = open(filename, 'w')
    writer = csv.writer(file)
    writer.writerow(csv_list)


def delete_profile(entries):
    profile_entry = entries[4]
    os.remove(os.getcwd() + "/csv/" + profile_entry[1].get() + '.csv')


#This function reads in all the names of the csv profiles, and prints them to a new window
def readProfiles():
    global loadedFiles
    root.filename = filedialog.askopenfilename(initialdir="/home/pi/Desktop/SPM450Files/SPM450/csv/", title= "popup", filetypes=(("csv files","*.csv"),("all files", "*.*")))
    loadedFiles = root.filename
    # for file in glob.glob("*.csv"):
    #     profiles.append(file)
    # top = Toplevel()
    # top.title("List of profiles")
    # for i in profiles:
    #     Label(top, text=i).pack()
    label1 = Label(root, text=loadedFiles)
    label1.pack()

####################################################################################
# These are just test functions. It is attached to the left and right move button
# It simulates the position of the stage pro changing
# This function is designed to test the slider to make sure it is reading in a value
# Eventually that slider should read in an actual calculated position value
# The parameter is takes in is the entire slider widget


def position_up(horizontalSlider):
    global position
    if position < 1000:
        position += 0.2
        horizontalSlider.set(position)


def position_down(horizontalSlider):
    global position
    if position > 0:
        position -= 0.2
        horizontalSlider.set(position)

######################################################################
