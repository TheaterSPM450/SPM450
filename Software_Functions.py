from tkinter import *
import csv
import os


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
