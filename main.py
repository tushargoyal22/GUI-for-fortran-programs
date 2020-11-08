from tkinter import *
from tkinter import filedialog
from tkinter import font
import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
global edit
root = Tk()
root.title('LAP - GUI for Fortran')
root.geometry("450x420")

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


def openHelpWindow():
	helpWindow = Toplevel()
	helpWindow.title('Help')
	helpWindow.geometry("500x1000")

	img = Image.open("help.jpeg")
	img = img.resize((600, 1000), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(helpWindow, image=img)
	panel.pack(side = TOP, anchor = NE, fill = "both")

	helpWindow.mainloop()



def openEditWindow():
	editWindow = Tk()
	editWindow.title('Forward modelling')
	editWindow.geometry("450x550")
	
	global my_text
	my_text = Text(editWindow, width=40, height=10, font=("Helvetica", 16))
	my_text.pack(pady=20)

	open_button = Button(editWindow, text="Open dat File", command=open_txt)
	open_button.pack(pady=15)

	save_button = Button(editWindow, text="Save File", command=save_txt)
	save_button.pack(pady=15)

	run_button = Button(editWindow, text="Run", command=run_txt)
	run_button.pack(pady=15)

	PlotButton = Button(editWindow, text = "Plot", command = GraphFunction)
	PlotButton.pack(pady=15)

	helpButton = Button(editWindow, text = "Help", command = openHelpWindow)
	helpButton.pack(pady=15)

	editWindow.mainloop()


def openParameterEstimationWindow():
	parameterEstimationWindow = Tk()
	parameterEstimationWindow.title('Parameter estimation')
	parameterEstimationWindow.geometry("450x420")

	parameterEstimationWindow.mainloop()

def GraphFunction():
	edit = Toplevel()
	edit.title('Graph')
	edit.geometry("500x500")
	img =Image.open("download.png")
	img=img.resize((500,500),Image.ANTIALIAS)
	img= ImageTk.PhotoImage(img)
	panel = Label(edit, image=img)
	panel.pack(side=TOP,anchor=NE,fill="both")
	#reading output and time files
	output = pd.read_csv("output.dat", delimiter=r"\s+",header=None)
	time = pd.read_csv("in_2.dat", header = None)
	time = time[2:]
	#plotting graph of concentration vs time
	plt.plot(time,output[0], label="Experimental")	
	plt.plot(time,output[1], label="Simulated")
	plt.xlabel("Time")
	plt.ylabel("Concentration")
	plt.legend()
	plt.title("Concentration vs Time graph")
	plt.savefig('graph.png',dpi=100)
	#displays the image of graph
	img2 =Image.open("graph.png")
	img2=img2.resize((500,500),Image.ANTIALIAS)
	img2= ImageTk.PhotoImage(img2)
	panel.config(image=img2)
	panel.image = img2
	edit.mainloop()
	
editButton = Button(root, text = "Forward modelling", command = openEditWindow)
editButton.pack(expand = YES)

parameterEstimationButton = Button(root, text = "Parameter estimation", command = openParameterEstimationWindow)
parameterEstimationButton.pack(expand = YES)

root.mainloop()