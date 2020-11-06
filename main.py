from tkinter import *
from tkinter import filedialog
from tkinter import font
import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

root = Tk()
root.title('LAP - GUI for Fortran')
root.geometry("450x420")

global panel

def open_txt():
	global file_name
	file_name = filedialog.askopenfilename(title="Open dat file", filetypes=(("dat files", "*.dat"), ))
	text_file = open(file_name, 'r')# Read only r 
	stuff = text_file.read()

	my_text.insert(END, stuff)
	text_file.close()


def save_txt():
	text_file = open(file_name, 'w') 
	text_file.write(my_text.get(1.0, END))

def run_txt():
	os.system('test.exe')

def plt_txt():
	
	output = pd.read_csv("output.dat", delimiter=r"\s+",header=None)
	time = pd.read_csv("in_2.dat", header = None)
	time = time[2:]
	plt.plot(output[0], time)	
	plt.plot(output[1], time)
	plt.savefig('graph.png',dpi=100)
	img2 =Image.open("graph.png")
	img2=img2.resize((600,300),Image.ANTIALIAS)
	img2= ImageTk.PhotoImage(img2)
	panel.config(image=img2)
	panel.image = img2

def openEditWindow():
	editWindow = Tk()
	editWindow.title('Forward modelling')
	editWindow.geometry("450x650")
	
	global my_text
	my_text = Text(editWindow, width=40, height=10, font=("Helvetica", 16))
	my_text.pack(pady=20)

	open_button = Button(editWindow, text="Open dat File", command=open_txt)
	open_button.pack(pady=20)

	save_button = Button(editWindow, text="Save File", command=save_txt)
	save_button.pack(pady=20)

	run_button = Button(editWindow, text="Run", command=run_txt)
	run_button.pack(pady=20)

	plot_button = Button(editWindow, text="Plot", command=plt_txt)
	plot_button.pack(pady=20)

	editWindow.mainloop()


def openParameterEstimationWindow():
	parameterEstimationWindow = Tk()
	parameterEstimationWindow.title('Parameter estimation')
	parameterEstimationWindow.geometry("450x420")

	parameterEstimationWindow.mainloop()

img =Image.open("download.png")
img=img.resize((200,200),Image.ANTIALIAS)
img= ImageTk.PhotoImage(img)
panel = Label(root, image=img,width=200)
panel.pack(side=TOP,anchor=NE,fill="both")

editButton = Button(root, text = "Forward modelling", command = openEditWindow)
editButton.pack()

parameterEstimationButton = Button(root, text = "Parameter estimation", command = openParameterEstimationWindow)
parameterEstimationButton.pack()

root.mainloop()