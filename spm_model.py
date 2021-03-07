import tkinter as tk
import csv
import os
from tkinter import *


# global variable for storing names of profile.csv
profiles = []

def fetch(entries):
    csv_list = []
    text = ''
    for entry in entries:
        text  = entry[1].get()
        if entry[0] == 'Profile Name':
            break
        csv_list.append(text)
    filename = text + '.csv'
    file = open(filename, 'w')
    writer = csv.writer(file)
    writer.writerow(csv_list)

def delete_profile(entries):
    profile_entry = entries[2]
    os.remove(profile_entry[1].get() + '.csv')


def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

import glob


#This function reads in all the names of the csv profiles, and prints them to a new window
def readProfiles():
    for file in glob.glob("*.csv"):
        profiles.append(file)
    top = Toplevel()
    top.title("List of profiles")
    for i in profiles:
        Label(top, text=i).pack()
