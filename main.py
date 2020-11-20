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
from graph_func import *
global edit
change = 0
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
			content[i] = "# " + valuesNames[i] + " #"

	newFile = open("in_1.tpl", 'w') 
	newFile.write("ptf #\n")
	for line in content:
		newFile.write(line)
		newFile.write("\n")
	newFile.close()


	newFile = open("in_1.par", 'w') 
	newFile.write("single point\n")
	global change
	for i in range(5):
		if entries[i].get() != "":
			change = change + 1
			newFile.write(valuesNames[i] + " " + entries[i].get() + " 1.0 1.0\n")
	newFile.close()


	cnt = int(content[5])
	print(cnt)

	newFile = open("output.ins", 'w') 
	newFile.write("pif #\n")

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
	os.system('pestgen test in_1.par measure.obf')
	pstfile = open("test.pst")
	string_list = pstfile.readlines()
	length = len(string_list)

	print(string_list[length-1], string_list[length-2], string_list[length-3], string_list[length-4], string_list[length-5], string_list[length-6])
	string_list[length-2] = "output.ins  output.dat\n"
	string_list[length-3] = "in_1.tpl  in_1.dat\n"
	string_list[length-5] = "test\n"

	pstfile = open("test.pst","w")
	new_file_contents = "".join(string_list)
	pstfile.write(new_file_contents)
	pstfile.close()


	os.system('pestchek test')
	os.system('pest test')



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


	helpButton = Button(window, text = "Help", command = openHelpWindow)
	helpButton.pack(expand = YES)

	if isPE : 
		guessButton = Button(window, text = "Guess Window", command = openGuessWindow)
		guessButton.pack(expand = YES)

		TableButton = Button(window, text = "K-L information statistics", command = tableKLStatistics)
		TableButton.pack(expand = YES)

		TableButton1 = Button(window, text = "Otimisation Results", command = tableParameterEstimation)
		TableButton1.pack(expand = YES)

	PlotButton = Button(window, text = "Plot", command = GraphFunction)
	PlotButton.pack(expand = YES)


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
	for i in range(start + 7, start + 7 + change):
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

editButton = Button(root, text = "Forward modelling", command = lambda : openWindow("Forward modelling"))
editButton.pack(expand = YES)

parameterEstimationButton = Button(root, text = "Parameter estimation", command = lambda : openWindow("Parameter estimation", True))
parameterEstimationButton.pack(expand = YES)

root.mainloop()
