import PySimpleGUI as sg      
import subprocess      
import os      
import sys      

""" Demo_Toolbar - A floating toolbar with quick launcher     One cool PySimpleGUI demo. Shows borderless windows, grab_anywhere, tight button layout You can setup a specific program to launch when a button is clicked, or use the Combobox to select a .py file found in the root folder, and run that file. """      

ROOT_PATH = './'      

def Launcher():      

    def print(line):      
        window.Element('output').Update(line)      

    sg.ChangeLookAndFeel('Dark')      

    namesonly = [f for f in os.listdir(ROOT_PATH) if f.endswith('.py') ]      

    sg.SetOptions(element_padding=(0,0), button_element_size=(12,1), auto_size_buttons=False)      
    layout =  [[#sg.Combo(values=namesonly, size=(35,30), key='demofile'),    
                    sg.Button('DSLAM'),      
                    sg.Button('PSF'),      
                    sg.Button('MOD', button_color=('white', '#35008B')),      
                    sg.Button('EXIT', button_color=('white','firebrick3'))],      
                    [sg.T('', text_color='white', size=(50,1), key='output')]]      

    window = sg.Window('Floating Toolbar', layout, no_titlebar=True, keep_on_top=True)

    # ---===--- Loop taking in user input (events) --- #      
    while True:      
        (event, value) = window.Read()      
        if event ==  'EXIT'  or event is None:      
            break # exit button clicked      
        if event ==  'DSLAM':      
            print('Running DSLAM')      
        elif event ==  'PSF':      
            print('Running PSF')      
        elif event ==  'MOD':       
            print('Running MOD')    
        else:      
            print(event)      

def ExecuteCommandSubprocess(command, *args, wait=False):      
    try:      
        if sys.platwindow == 'linux':      
            arg_string = ''      
            for arg in args:      
                 arg_string += ' '  + str(arg)      
            sp = subprocess.Popen(['python3'  + arg_string, ], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)      
        else:      
            sp = subprocess.Popen([command, list(args)], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)      

        if wait:      
            out, err = sp.communicate()      
            if out:      
                print(out.decode("utf-8"))      
            if err:      
                print(err.decode("utf-8"))      
    except: pass      



if __name__ == '__main__':      
    Launcher() 
