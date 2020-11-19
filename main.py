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
from matplotlib.backends.backend_gtk3agg import FigureCanvas
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)

global edit

root = tk.ThemedTk()
root.get_themes()# Returns a list of all themes that can be set
root.set_theme("radiance")
root.title('LAP - GUI for Fortran')
root.geometry("450x420")


valuesNames = ["qs", "qf", "omegaim", "omegasf", "alpha"]
entries = []


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


def guessSave():
	file_name = 'in_1.dat'
	text_file = open(file_name, 'r') 
	content = text_file.read()
	text_file.close()
	content = content.split('\n')

	for i in range(5):
		if entries[i].get() != "":
			content[i] = "#" + valuesNames[i] + " #"

	newFile = open("in_1.tpl", 'w') 
	newFile.write("ptf #\n")
	for line in content:
		newFile.write(line)
		newFile.write("\n")
	newFile.close()


	newFile = open("in_1.par", 'w') 
	newFile.write("single point\n")
	for i in range(5):
		if entries[i].get() != "":
			newFile.write(valuesNames[i] + " " + entries[i].get() + " 1.0 1.0\n")
	newFile.close()


	cnt = int(content[5])
	print(cnt)

	newFile = open("output.ins", 'w') 
	newFile.write("ptf #\n")

	for i in range(1,cnt+1):
		newFile.write("l1 (o"+str(i)+")19:26")
		newFile.write("\n")
	newFile.close()
    # (oi) is the observation point and it should go up to max. observation time steps



	newFile = open("measure.obf", 'w') 
# Saving experimental data from in_1.dat in measure.obf corresponding to observation
# number
	for i in range(6,len(content)-1):
		currobn = i-5
		newFile.write("o"+str(currobn)+" "+content[i])
		newFile.write("\n")

	newFile.close()


def openGuessWindow():
	window = Tk()
	window.title("Guess Window")
	window.geometry("300x350")

	global entries
	entries = []
	Label(window, text = " ").grid(row = 0)
	for i in range(5):
		Label(window, text = valuesNames[i]).grid(row = 2*i + 1)
		entry = Entry(window)
		entry.grid(row = 2*i + 1, column = 1)
		entries.append(entry)
		Label(window, text = " ").grid(row = 2*i + 2)

	Button(window, text="Save", command = guessSave).grid(row = 12, column = 1)

	window.mainloop()


def openWindow(header, isPE = False):
	window = tk.ThemedTk()
	window.get_themes()# Returns a list of all themes that can be set
	window.set_theme("radiance")

	window.title(header)
	window.geometry("450x600")
	
	global my_text
	my_text = Text(window, width=40, height=10, font=("Helvetica", 16))
	my_text.pack(expand = YES)

	open_button = Button(window, text="Open dat File", command=open_txt)
	open_button.pack(expand = YES)

	save_button = Button(window, text="Save File", command=save_txt)
	save_button.pack(expand = YES)

	run_button = Button(window, text="Run", command=run_txt)
	run_button.pack(expand = YES)

	PlotButton = Button(window, text = "Plot", command = GraphFunction)
	PlotButton.pack(expand = YES)

	helpButton = Button(window, text = "Help", command = openHelpWindow)
	helpButton.pack(expand = YES)

	if isPE : 
		guessButton = Button(window, text = "Guess Window", command = openGuessWindow)
		guessButton.pack(expand = YES)

		TableButton = Button(window, text = "K-L information statistics", command = tableKLStatistics)
		TableButton.pack(expand = YES)

		TableButton1 = Button(window, text = "Otimisation Results", command = tableParameterEstimation)
		TableButton1.pack(expand = YES)


	window.mainloop()
def render_mpl_table(data, col_width=3.0, row_height=0.75, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in  six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.box(on=None)
    plt.draw()
    fig = plt.gcf()
    plt.savefig('tableKLStatistics.png')

def tableKLStatistics():
	window = Toplevel()
	window.title('K-L information statistics')
	window.geometry("500x500")
	img =Image.open("download.png")
	img=img.resize((500,500),Image.ANTIALIAS)
	img= ImageTk.PhotoImage(img)
	panel = Label(window, image=img)
	panel.pack(side=TOP,anchor=NE,fill="both")
	df = pd.DataFrame()
	f = open("test.rec")
	lines = []
	col1 = []
	col2 = []
	for line in f: 
		lines.append(line)
	start = lines.index('K-L information statistics ----->\n')
	for i in range(start + 3, start + 7):
		col = lines[i].split('  ')
		col1.append(col[1])	
		col2.append(col[3])
	df['Name'] = col1
	df['Value'] = col2
	render_mpl_table(df, header_columns=0, col_width=2.0)
	
	img2 =Image.open("tableKLStatistics.png")
	img2=img2.resize((500,500),Image.ANTIALIAS)
	img2= ImageTk.PhotoImage(img2)
	panel.config(image=img2)
	panel.image = img2
	window.mainloop()

def tableParameterEstimation():
	window = Toplevel()
	window.title('OPTIMISATION RESULTS')
	window.geometry("1000x500")
	img =Image.open("download.png")
	img=img.resize((500,500),Image.ANTIALIAS)
	img= ImageTk.PhotoImage(img)
	panel = Label(window, image=img)
	panel.pack(side=TOP,anchor=NE,fill="both")
	df = pd.DataFrame()
	f = open("test.rec")
	lines = []
	col1 = []
	col2 = []
	col3 = []
	col4 = []

	for line in f: 
		lines.append(line)
	start = lines.index('                            OPTIMISATION RESULTS\n')
	for i in range(start + 7, start + 11):
		col = lines[i].split()
		col1.append(col[0])
		col2.append(col[1])
		col3.append(col[2])
		col4.append(col[3])

	df['Parameter'] = col1
	df['Estimated Value'] = col2
	df['Lower Limit'] = col3
	df['Upper Limit'] = col4

	render_mpl_table(df, header_columns=0, col_width=3.0)
	
	img2 =Image.open("tableKLStatistics.png")
	img2=img2.resize((1000,500),Image.ANTIALIAS)
	img2= ImageTk.PhotoImage(img2)
	panel.config(image=img2)
	panel.image = img2
	window.mainloop()

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


	
editButton = Button(root, text = "Forward modelling", command = lambda : openWindow("Forward modelling"))
editButton.pack(expand = YES)

parameterEstimationButton = Button(root, text = "Parameter estimation", command = lambda : openWindow("Parameter estimation", True))
parameterEstimationButton.pack(expand = YES)

root.mainloop()