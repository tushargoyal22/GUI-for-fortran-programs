from tkinter import *
from tkinter import filedialog
from tkinter import font
import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import ttk 
from ttkthemes import themed_tk as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import FigureCanvas
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 

global edit

root = tk.ThemedTk()
root.get_themes()# Returns a list of all themes that can be set
root.set_theme("radiance")
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

	editWindow = tk.ThemedTk()
	editWindow.get_themes()# Returns a list of all themes that can be set
	editWindow.set_theme("radiance")

	editWindow.title('Forward modelling')
	editWindow.geometry("450x600")
	
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
	parameterEstimationWindow = tk.ThemedTk()
	parameterEstimationWindow.get_themes()# Returns a list of all themes that can be set
	parameterEstimationWindow.set_theme("radiance")

	parameterEstimationWindow.title('Parameter estimation')
	parameterEstimationWindow.geometry("450x600")

	global my_text
	my_text = Text(parameterEstimationWindow, width=40, height=10, font=("Helvetica", 16))
	my_text.pack(pady=20)

	open_button = Button(parameterEstimationWindow, text="Open dat File", command=open_txt)
	open_button.pack(pady=15)

	save_button = Button(parameterEstimationWindow, text="Save File", command=save_txt)
	save_button.pack(pady=15)

	run_button = Button(parameterEstimationWindow, text="Run", command=run_txt)
	run_button.pack(pady=15)

	# PlotButton = Button(editWindow, text = "Plot", command = GraphFunction)
	# PlotButton.pack(pady=15)

	helpButton = Button(parameterEstimationWindow, text = "Help", command = openHelpWindow)
	helpButton.pack(pady=15)

	parameterEstimationWindow.mainloop()

def GraphFunction():
	window = Tk() 
	window.title('Graphs') 
	window.geometry("700x500")
	tabControl = ttk.Notebook(window) 
	tab1 = ttk.Frame(tabControl) 
	tab2 = ttk.Frame(tabControl) 
	tab3 = ttk.Frame(tabControl)

	tabControl.add(tab1, text ='Experimental Data') 
	tabControl.add(tab2, text ='Simulated Data') 
	tabControl.add(tab3, text ='Combined Data') 
	tabControl.pack(expand = 1, fill ="both") 

	#reading output and time files
	output = pd.read_csv("output.dat", delimiter=r"\s+",header=None)
	time = pd.read_csv("in_2.dat", header = None)
	time = time[2:]

	fig = Figure(figsize=(5,4), dpi=100)
	ax = fig.add_subplot(111)
	ax.plot(time,output[0], label="Experimental")
	ax.set_xlabel("Time")
	ax.set_ylabel("Concentration")
	ax.legend()

	canvas = FigureCanvasTkAgg(fig, master = tab1)
	canvas.draw()
	canvas.get_tk_widget().pack()
	toolbar = NavigationToolbar2Tk(canvas, tab1)
	toolbar.update() 
	canvas.get_tk_widget().pack()

	fig2 = Figure(figsize=(5,4), dpi=100)
	ax2 = fig2.add_subplot(111)
	ax2.plot(time,output[1], label="Simulated")
	ax2.set_xlabel("Time")
	ax2.set_ylabel("Concentration")
	ax2.legend()

	canvas2 = FigureCanvasTkAgg(fig2, master = tab2)
	canvas2.draw()
	canvas2.get_tk_widget().pack()
	toolbar2 = NavigationToolbar2Tk(canvas2, tab2)
	toolbar2.update() 
	canvas2.get_tk_widget().pack()

	fig3 = Figure(figsize=(5,4), dpi=100)
	ax3 = fig3.add_subplot(111)
	ax3.plot(time,output[0], label="Experimental")
	ax3.plot(time,output[1], label="Simulated")
	ax3.set_xlabel("Time")
	ax3.set_ylabel("Concentration")
	ax3.legend()

	canvas3 = FigureCanvasTkAgg(fig3, master = tab3)
	canvas3.draw()
	canvas3.get_tk_widget().pack()
	toolbar3 = NavigationToolbar2Tk(canvas3, tab3)
	toolbar3.update() 
	canvas3.get_tk_widget().pack()
	window.mainloop()

	
editButton = Button(root, text = "Forward modelling", command = openEditWindow)
editButton.pack(expand = YES)

parameterEstimationButton = Button(root, text = "Parameter estimation", command = openParameterEstimationWindow)
parameterEstimationButton.pack(expand = YES)

root.mainloop()
