from tkinter import *
from tkinter import filedialog
from tkinter import font

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


def openEditWindow():
	editWindow = Tk()
	editWindow.title('Forward modelling')
	editWindow.geometry("450x420")

	global my_text
	my_text = Text(editWindow, width=40, height=10, font=("Helvetica", 16))
	my_text.pack(pady=20)

	open_button = Button(editWindow, text="Open dat File", command=open_txt)
	open_button.pack(pady=20)

	save_button = Button(editWindow, text="Save File", command=save_txt)
	save_button.pack(pady=20)

	editWindow.mainloop()


def openParameterEstimationWindow():
	parameterEstimationWindow = Tk()
	parameterEstimationWindow.title('Parameter estimation')
	parameterEstimationWindow.geometry("450x420")

	parameterEstimationWindow.mainloop()



editButton = Button(root, text = "Forward modelling", command = openEditWindow)
editButton.pack()

parameterEstimationButton = Button(root, text = "Parameter estimation", command = openParameterEstimationWindow)
parameterEstimationButton.pack()

root.mainloop()