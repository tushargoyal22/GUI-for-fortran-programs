from tkinter import *
from tkinter.filedialog import askopenfilename
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







valuesName3 = [
	"nz", 
	"nm", 
	"Length (Le)", 
	"Bulk density of porous media (𝜌𝑏)", 
	"Run time (Tmax)", 
	"Pulse time (Tp)", 
	"∆𝑡", 
	"∆𝑥"
]

valuesName1 = [
	"Mesopore seepage velocity (𝑞𝑠 )", 
	"Macropore seepage velocity (𝑞𝑓 )",
	"Solute mass transfer rate b/w meso-micropore (ωim)", 
	"Solute mass transfer rate b/w meso-macropore (ωsf)", 
	"Dispersivity (å𝐿 )", 
	"No. of observation time steps", 
	"Experimental data (Input from txt file or excel copy paste)"
]

valuesName2 = [
	"No. of observation distances to print", 
	"Observation distances (According to No.of observation distances)", 
	"Time steps (Input from txt file or excel copy paste)"
]

valuesNamesArr = [valuesName1, valuesName2, valuesName3]









defaultValuesADE = [
	"Porosity of the mesopore region (𝜃𝑠)", 
	"Porosity of the micropore region (𝜃𝑖𝑚)",
	"Instantaneous sorption fraction in macropore region (𝐹𝑓)", 
	"Instantaneous sorption fraction in mesopore region (𝐹𝑠)",
	"Instantaneous sorption fraction in micropore region (𝐹𝑖𝑚)", 
	"Fraction of sorption site available for macropore region (𝑓𝑓)", 
	"Fraction of sorption site available for mesopore region (𝑓𝑠)",	
	"Fraction of sorption site available for immobile region (𝑓𝑖𝑚)",
	"Equilibrium sorption coefficient in mesopore region (𝐾𝑠)", 
	"Equilibrium sorption coefficient in micropore region (𝐾𝑖𝑚)", 
	"Rate-limited sorbed coefficient in macropore region (𝑘𝑓)", 
	"Rate-limited sorbed coefficient in mesopore region (𝑘𝑠)", 
	"Rate-limited sorbed coefficient in micropore region (𝑘𝑖𝑚)", 
	"Mesopore seepage velocity (𝑞𝑠 )", 
	"Solute mass transfer rate b/w meso-micropore (ωim)", 
	"Solute mass transfer rate b/w meso-macropore (ωsf)"
]


askValuesADE = [
	"Porosity of the macropore region (𝜃𝑓)", 
	"Equilibrium sorption coefficient in macropore region (𝐾𝑓)", 
	"Macropore seepage velocity (𝑞𝑓 )",
	"Dispersivity (å𝐿 )"
]



defaultValuesMIM = [
	"Porosity of the mesopore region (𝜃𝑠)", 
	"Porosity of the micropore region (𝜃𝑖𝑚)",
	"Instantaneous sorption fraction in micropore region (𝐹𝑖𝑚)", 
	"Fraction of sorption site available for immobile region (𝑓𝑖𝑚)",
	"Equilibrium sorption coefficient in micropore region (𝐾𝑖𝑚)", 
	"Rate-limited sorbed coefficient in macropore region (𝑘𝑓)", 
	"Rate-limited sorbed coefficient in mesopore region (𝑘𝑠)", 
	"Rate-limited sorbed coefficient in micropore region (𝑘𝑖𝑚)", 
	"Mesopore seepage velocity (𝑞𝑠 )", 
	"Solute mass transfer rate b/w meso-micropore (ωim)"
]



askValuesMIM = [
	"Porosity of the macropore region (𝜃𝑓)", 
	"Instantaneous sorption fraction in macropore region (𝐹𝑓)", 
	"Instantaneous sorption fraction in mesopore region (𝐹𝑠)",
	"Fraction of sorption site available for macropore region (𝑓𝑓)", 
	"Fraction of sorption site available for mesopore region (𝑓𝑠)",	
	"Equilibrium sorption coefficient in macropore region (𝐾𝑓)", 
	"Equilibrium sorption coefficient in mesopore region (𝐾𝑠)", 
	"Macropore seepage velocity (𝑞𝑓 )",
	"Solute mass transfer rate b/w meso-macropore (ωsf)", 
	"Dispersivity (å𝐿 )", 
]



defaultValuesMPNE = [
	"Porosity of the micropore region (𝜃𝑖𝑚)",
	"Instantaneous sorption fraction in micropore region (𝐹𝑖𝑚)", 
	"Fraction of sorption site available for immobile region (𝑓𝑖𝑚)",
	"Equilibrium sorption coefficient in micropore region (𝐾𝑖𝑚)", 
	"Rate-limited sorbed coefficient in micropore region (𝑘𝑖𝑚)", 
	"Solute mass transfer rate b/w meso-micropore (ωim)", 
]




askValuesMPNE = [
	"Porosity of the macropore region (𝜃𝑓)", 
	"Porosity of the mesopore region (𝜃𝑠)", 
	"Instantaneous sorption fraction in macropore region (𝐹𝑓)", 
	"Instantaneous sorption fraction in mesopore region (𝐹𝑠)",
	"Fraction of sorption site available for macropore region (𝑓𝑓)", 
	"Fraction of sorption site available for mesopore region (𝑓𝑠)",	
	"Equilibrium sorption coefficient in macropore region (𝐾𝑓)", 
	"Equilibrium sorption coefficient in mesopore region (𝐾𝑠)", 
	"Rate-limited sorbed coefficient in macropore region (𝑘𝑓)", 
	"Rate-limited sorbed coefficient in mesopore region (𝑘𝑠)", 
	"Mesopore seepage velocity (𝑞𝑠 )", 
	"Macropore seepage velocity (𝑞𝑓 )",
	"Solute mass transfer rate b/w meso-macropore (ωsf)", 
	"Dispersivity (å𝐿 )"
]




defaultValuesDADE = [
	"Porosity of the micropore region (𝜃𝑖𝑚)",
	"Instantaneous sorption fraction in macropore region (𝐹𝑓)", 
	"Instantaneous sorption fraction in mesopore region (𝐹𝑠)",
	"Instantaneous sorption fraction in micropore region (𝐹𝑖𝑚)", 
	"Fraction of sorption site available for macropore region (𝑓𝑓)", 
	"Fraction of sorption site available for mesopore region (𝑓𝑠)",	
	"Fraction of sorption site available for immobile region (𝑓𝑖𝑚)",
	"Equilibrium sorption coefficient in macropore region (𝐾𝑓)", 
	"Equilibrium sorption coefficient in mesopore region (𝐾𝑠)", 
	"Equilibrium sorption coefficient in micropore region (𝐾𝑖𝑚)", 
	"Rate-limited sorbed coefficient in macropore region (𝑘𝑓)", 
	"Rate-limited sorbed coefficient in mesopore region (𝑘𝑠)", 
	"Rate-limited sorbed coefficient in micropore region (𝑘𝑖𝑚)", 
	"Solute mass transfer rate b/w meso-micropore (ωim)"
]




askValuesDADE = [
	"Porosity of the macropore region (𝜃𝑓)", 
	"Porosity of the mesopore region (𝜃𝑠)", 
	"Mesopore seepage velocity (𝑞𝑠 )", 
	"Macropore seepage velocity (𝑞𝑓 )",
	"Solute mass transfer rate b/w meso-macropore (ωsf)", 
	"Dispersivity (å𝐿 )"
]


defaultValuesALL = []


askValuesALL = [
	"Porosity of the macropore region (𝜃𝑓)", 
	"Porosity of the mesopore region (𝜃𝑠)", 
	"Porosity of the micropore region (𝜃𝑖𝑚)",
	"Instantaneous sorption fraction in macropore region (𝐹𝑓)", 
	"Instantaneous sorption fraction in mesopore region (𝐹𝑠)",
	"Instantaneous sorption fraction in micropore region (𝐹𝑖𝑚)", 
	"Fraction of sorption site available for macropore region (𝑓𝑓)", 
	"Fraction of sorption site available for mesopore region (𝑓𝑠)",	
	"Fraction of sorption site available for immobile region (𝑓𝑖𝑚)",
	"Equilibrium sorption coefficient in macropore region (𝐾𝑓)", 
	"Equilibrium sorption coefficient in mesopore region (𝐾𝑠)", 
	"Equilibrium sorption coefficient in micropore region (𝐾𝑖𝑚)", 
	"Rate-limited sorbed coefficient in macropore region (𝑘𝑓)", 
	"Rate-limited sorbed coefficient in mesopore region (𝑘𝑠)", 
	"Rate-limited sorbed coefficient in micropore region (𝑘𝑖𝑚)", 
	"Mesopore seepage velocity (𝑞𝑠 )", 
	"Macropore seepage velocity (𝑞𝑓 )",
	"Solute mass transfer rate b/w meso-micropore (ωim)", 
	"Solute mass transfer rate b/w meso-macropore (ωsf)", 
	"Dispersivity (å𝐿 )"
]



oneValue = [
	"Instantaneous sorption fraction in macropore region (𝐹𝑓)", 
	"Fraction of sorption site available for macropore region (𝑓𝑓)"
]



def getContent(fileName, sep = None):
	text_file = open(fileName, 'r') 
	content = text_file.read()
	text_file.close()
	return content.split(sep)


def saveContent(newContent, fileName, valuesToUpdate):
	oldContent = getContent(fileName, '\n')
	file = open(fileName, 'w') 

	valueNames = valuesNamesArr[int(fileName[3]) - 1]

	vi = 0
	for line in oldContent:
		values = line.split(' ')
		if vi < len(valueNames):
			for i in range(len(values)):
				if valueNames[vi] in valuesToUpdate:
					values[i] = newContent[valuesToUpdate.index(valueNames[vi])].get()
				vi = vi + 1
		file.write(" ".join(values) + "\n")
	file.close()



def open_txt_exper(window):
	
	file_name = askopenfilename(parent = window, title="Open file", filetypes=(("text files", "*.txt"), ))
	data_file = open(file_name, 'r')# Read only r 
	stuff = data_file.read()
	stuff = stuff.split('\n')
	data_file.close()
	while len(stuff) and stuff[-1]== '':
		stuff.pop()

	cnt = len(stuff)
	

	file = open('in_1.dat', 'r') 
	content = file.read()
	file.close()

	content = content.split('\n')


	file = open('in_1.dat', 'w') 
	for i in range(5):
		file.write(content[i] + '\n')

	file.write(str(cnt) + '\n')

	for i in range(cnt):
		file.write(stuff[i] + '\n')

	file.close()

def open_txt_time(window):
	
	file_name = askopenfilename(parent = window, title="Open file", filetypes=(("text files", "*.txt"), ))
	data_file = open(file_name, 'r')# Read only r 
	stuff = data_file.read()
	stuff = stuff.split('\n')
	data_file.close()
	while len(stuff) and stuff[-1]== '':
		stuff.pop()

	cnt = len(stuff)
	

	file = open('in_2.dat', 'r') 
	content = file.read()
	content = content.split('\n')
	file.close()


	file = open('in_2.dat', 'w') 
	for i in range(2):
		file.write(content[i] + '\n')

	for i in range(cnt):
		file.write(stuff[i] + '\n')

	file.close()



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


def guessSave(wind):
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
		if(i != cnt):
			newFile.write("\n")
	newFile.close()
    # (oi) is the observation point and it should go up to max. observation time steps



	newFile = open("measure.obf", 'w') 
# Saving experimental data from in_1.dat in measure.obf corresponding to observation
# number
	for i in range(6,6+cnt):
		currobn = i-5
		newFile.write("o"+str(currobn)+" "+content[i])
		if(i != cnt+5):
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

	wind.destroy()

def openGuessWindow():
	window = Tk()
	window.title("Guess Window")
	window.geometry("300x350")


	global entries
	entries = []
	Label(window, text = " ").grid(row = 0)
	# Label(window, text = "Fields not filled would be considered Determined").grid(row = 0)

	for i in range(5):
		Label(window, text = valuesNames[i]).grid(row = 2*i + 1)
		entry = Entry(window)
		entry.grid(row = 2*i + 1, column = 1)
		entries.append(entry)
		Label(window, text = " ").grid(row = 2*i + 2)


	Button(window, text="Save", command = lambda : guessSave(window)).grid(row = 13, column = 1)

	window.mainloop()



def estimateWindow():

	window = tk.ThemedTk()
	window.get_themes()
	window.set_theme("radiance")
	window.geometry("450x420")


	guessButton = Button(window, text = "Guess Window", command = openGuessWindow)
	guessButton.pack(expand = YES)
	# guessButton.grid(row = 1, column = 2)

	TableButton = Button(window, text = "K-L information statistics", command = tableKLStatistics)
	TableButton.pack(expand = YES)

	# TableButton.grid(row = 2, column = 2)

	TableButton1 = Button(window, text = "Optimisation Results", command = tableParameterEstimation)
	TableButton1.pack(expand = YES)

	# TableButton1.grid(row = 3, column = 2)
	PlotButton = Button(window, text = "Plot", command = GraphFunction)
	PlotButton.pack(expand=YES)

	window.mainloop()





def entriesWindow(header, defaultValues, askValues):
	top = Tk()

	def save():
		saveContent(fileEntries, "in_1.dat", valuesName3 + defaultValues + askValues)
		saveContent(fileEntries, "in_2.dat", valuesName3 + defaultValues + askValues)
		saveContent(fileEntries, "in_3.dat", valuesName3 + defaultValues + askValues)
		top.destroy()


	fileEntries = []

	for i in range(len(valuesName3)):
		Label(top, text = valuesName3[i]).grid(row = i, column = 0)
		entry = Entry(top)
		entry.grid(row = i, column = 1)
		fileEntries.append(entry)



	for i in range(len(defaultValues)):
		# Label(top, text = defaultValues[i]).grid(row = i, column = 0)
		entry = Entry(top)
		defVal = "1E-16"
		if defaultValues[i] in oneValue:
			defVal = "1"
		entry.insert(END, defVal)
		# entry.grid(row = i, column = 1)
		fileEntries.append(entry)

	for i in range(len(askValues)):
		Label(top, text = askValues[i]).grid(row = i + len(valuesName3), column = 0)
		entry = Entry(top)
		entry.grid(row = i + len(valuesName3), column = 1)
		fileEntries.append(entry)

	Button(top, text = 'Save', command = save).grid()







def openWindow(header, isPE = False):
	window = tk.ThemedTk()
	window.get_themes()
	window.set_theme("radiance")
	window.title(header)
	window.geometry("450x420")


	headers = [
		"Equilibrium solute transport model (ADE)", 
		"Dual-Porosity Single Permeability Models (MIM)", 
		"Dual porosity single permeability two site model (MPNE)", 
		"Single porosity dual permeability two site model (DADE)", 
		"Triple porosity dual permeability three site model"
	]

	
	Button(window, text = headers[0], command = lambda : entriesWindow(headers[0], defaultValuesADE, askValuesADE)).pack(expand = YES)
	Button(window, text = headers[1], command = lambda : entriesWindow(headers[1], defaultValuesMIM, askValuesMIM)).pack(expand = YES)
	Button(window, text = headers[2], command = lambda : entriesWindow(headers[2], defaultValuesMPNE, askValuesMPNE)).pack(expand = YES)
	Button(window, text = headers[3], command = lambda : entriesWindow(headers[3], defaultValuesDADE, askValuesDADE)).pack(expand = YES)
	Button(window, text = headers[4], command = lambda : entriesWindow(headers[4], defaultValuesALL, askValuesALL)).pack(expand = YES)


	expdata = Button( window, text="Upload Experimental data", command= lambda:open_txt_exper(window))
	expdata.pack(expand = YES)

	timedata = Button( window, text="Upload Time Stamps", command= lambda:open_txt_time(window))
	timedata.pack(expand = YES)


	if isPE == False:
		PlotButton = Button(window, text = "Plot", command = GraphFunction)
		PlotButton.pack(expand = YES)

		run_button = Button(window, text="Run", command=run_txt)
		run_button.pack(expand = YES)
	else:
		Estimate = Button(window, text = "Estimate Parameters", command = estimateWindow)
		Estimate.pack(expand = YES)

	root.destroy()
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
	img2=img2.resize((1000,200 + 50*change),Image.ANTIALIAS)
	img2= ImageTk.PhotoImage(img2)
	panel.config(image=img2)
	panel.image = img2
	window.mainloop()

#logo display
image = Image.open("./logo.png")
image = image.resize((round(image.size[0]*0.5), round(image.size[1]*0.5)))
logo = ImageTk.PhotoImage(image)
panel = Label(root, image = logo)
panel.pack(side="left", fill = "x")
panel.place(x=0,y=0)

#heading
heading = Label(root, text = "GUI for Fortran Programs", font = "tkDefaultFont 12 bold")
heading.pack(side = "top")
heading.place(x=190,y=50)

editButton = Button(root, text = "Forward modelling", command = lambda : openWindow("Forward modelling"))
editButton.pack(side = "top",fill="x")
editButton.place(x=130,y=200)

parameterEstimationButton = Button(root, text = "Parameter estimation", command = lambda : openWindow("Parameter Estimation", True))
parameterEstimationButton.pack(side="top", fill="x")
parameterEstimationButton.place(x=120,y=250)

root.mainloop()
