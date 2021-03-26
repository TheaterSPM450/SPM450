#import tkinter as tk
import csv
import os
from tkinter import *
from tkinter import filedialog
#from time import sleep
#import RPi.GPIO as GPIO



# global variable for storing names of profile.csv
profiles = []
loadedFiles = ""
fields = ["speed", "ratio", "diameter", "position", "filename"]
path = os.getcwd()

def fetch(entries):
    csv_list = []
    text = ''
    for entry in entries:
        text = entry[1].get()
        if entry[0] == 'filename':
            break
        csv_list.append(text)
    filename = path + "/csv/" + text + '.csv'
    file = open(filename, 'w')
    writer = csv.writer(file)
    writer.writerow(csv_list)

def delete_profile(entries):
    profile_entry = entries[4]
    os.remove(path + "/csv/" + profile_entry[1].get() + '.csv')


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

import glob


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
    

if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = Button(root, text='Save',command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(root, text='Delete',command=(lambda e=ents: delete_profile(e)))
    b3.pack(side=LEFT, padx=5, pady=5)
    b4 = Button(root, text='Load', command= readProfiles)
    b4.pack(side=LEFT, padx=5, pady=5)


    root.mainloop()
    #top.mainloop()