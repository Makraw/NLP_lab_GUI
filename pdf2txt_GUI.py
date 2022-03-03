"""
the purpose of this code is to allow the user to run PDF2TXT graphically.
As it stands, running PDF2TXT is a complicated process that requires terminal usage.
To make the first step in the pipeline accessible to members of the nano lab, who may have limited skills with the
Linux terminal, a graphical version is designed here.

Ultimately, this program is just a form to fill out that will store the entries and pass that stuff off to the already
existing pdf2txt converter.

THIS IS A DEFUNCT VERSION. IT DOES NOT WORK. NO FURTHER UPDATES EXPECTED.
"""
import os

# build the window and graphics with tkinter
from tkinter import *


def run_converter():
    command = ''
    # attempt to build the command string from the entered values
    try:
        input_filepath = str(file_path_in.get())
        output_filepath = str(file_path_out.get())
        convert_whole = (whole_folder > 0)

        # check for complete entry. Crash if entry is bad
        if input_filepath == '':
            raise Exception('Input file path not specified')
        if output_filepath == '':
            raise Exception('Output file path not specified')

        # create the string to run
        if convert_whole:
            command = 'python3 ~/Packages/pdf2txt_venv/PDF2TXT/pdf2txt/pdf2txt.py -d ' + input_filepath + ' -o ' + output_filepath
        else:
            command = 'python3 ~/Packages/pdf2txt_venv/PDF2TXT/pdf2txt/pdf2txt.py -f ' + input_filepath + ' -o ' + output_filepath

    except:
        print('an error has occurred and the program has failed.')

    # initialize the venv as needed for pdf2txt
    os.system('source ~/Packages/pdf2txt_venv/bin/activate')

    # use system.os to run the command in terminal to do the conversion
    os.system(command)


class Window:
    def __init__(self, window):
        # use a label to prompt the user to enter the data needed to do the conversion
        self.lbl1 = Label(window, text='Enter the input file path:')
        self.lbl1.place(x=30, y=10)
        # create text fields to take in the input file path
        self.file_path_in = Entry(window, text='filepath in')
        self.file_path_in.place(x=30, y=35)

        # now label and gather the output file path
        self.lbl2 = Label(window, text='Enter the output file path:')
        self.lbl2.place(x=30, y=60)
        self.file_path_out = Entry(window, text='destination folder')
        self.file_path_out.place(x=30, y=85)

        # check if the user wants to convert an entire folder or just a single file
        whole_folder = IntVar()
        self.c1 = Checkbutton(window, text='Convert whole folder', variable=whole_folder)
        self.c1.place(x=30, y=120)

        # create a button to take in and run the user's entry
        self.run = Button(window, text='run')
        self.run.place(x=90, y=150)

        # bind the button to execute the code
        self.run.bind(run_converter())

    # when the run button is clicked, send the appropriate arguments to the PDF2TXT program


window =Tk()
converter=Window(window)

# create the basic window and the name of the program
window.title('PDF to Text')
window.geometry('250x200')
window.mainloop()
