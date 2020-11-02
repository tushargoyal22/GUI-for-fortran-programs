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


my_text = Text(root, width=40, height=10, font=("Helvetica", 16))
my_text.pack(pady=20)


open_button = Button(root, text="Open dat File", command=open_txt)
open_button.pack(pady=20)

save_button = Button(root, text="Save File", command=save_txt)
save_button.pack(pady=20)

root.mainloop()
