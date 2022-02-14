"""
the purpose of this code is to allow the user to run PDF2TXT graphically.
As it stands, running PDF2TXT is a complicated process that requires terminal usage.
To make the first step in the pipeline accessible to members of the nano lab, who may have limited skills with the
Linux terminal, a graphical version is designed here.
Ultimately, this program is just a form to fill out that will store the entries and pass that stuff off to the already
existing pdf2txt converter.
"""
import os

# build the window and graphics with tkinter
from tkinter import *

# the code that handles the installation of pdf2txt and its dependencies
# check if the filepath exists
if os.path.exists('~/Packages/pdf2txt_venv_gui/'):
    # this block checks for updates
    os.system('cd ~/Packages/pdf2txt_venv_gui')
    os.system('source ~/Packages/pdf2txt_venv_gui/PDF2TXT/bin/activate')
    os.system('pip3 install farm-haystack -U')

    # this will run if the log file does not exist, meaning this is the first time this program is run
else:
    print('PDF2TXT_GUI has not previously been run. Installing PDF2TXT and dependencies\n\n')

    # the following will create the file structure
    os.system('mkdir ~/Packages/pdf2txt_venv_gui')
    os.system('python3 -m venv ~/Packages/pdf2txt_venv_gui')
    os.system('source ~/Packages/pdf2txt_venv_gui/PDF2TXT/bin/activate')
    os.system('cd ~/Packages/pdf2txt_venv_gui/PDF2TXT')

    # this downloads the program and its dependencies
    os.system('git clone https://github.com/NLPatVCU/PDF2TXT.git')
    os.system('pip3 install farm-haystack')


"""
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
"""