from tkinter import *
from tkinter import filedialog
from tkinter import font
import os
import six
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import ttk 
from ttkthemes import themed_tk as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)

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
	