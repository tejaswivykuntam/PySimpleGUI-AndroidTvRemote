import PySimpleGUI as sg
import subprocess
import androidtv

SYMBOL_UP =    '▲'
SYMBOL_DOWN =  '▼'

def collapse(layout, key):
    return sg.pin(sg.Column(layout, key = key))

Connection_section = [ [sg.Text("Input ip address to connect via adb")], [sg.InputText(key='-IP-')], [sg.Submit()], [sg.Text(size=(40,1), key='-OUTPUT-')], [sg.Button("Connect")], [sg.Button("Disconnect")] ]

App_section = [ [sg.Button("Spotify",key='spotify')], [sg.Button("Youtube",key="youtube")], [sg.Button("TV Manager",key="manager")], [sg.Button("Live TV",key="livetv") ] ]

layout =   [[sg.Text('Window with 2 collapsible sections')],
            [sg.Checkbox('Blank checkbox'), sg.Checkbox('Hide Section 2', enable_events=True, key='-OPEN SEC2-CHECKBOX')],
            #### Section 1 part ####
            [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC1-', text_color='yellow'), sg.T('Section 1', enable_events=True, text_color='yellow', k='-OPEN SEC1-TEXT')],
            [collapse(Connection_section, '-SEC1-')],
            #### Section 2 part ####
            [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC2-', text_color='purple'),
             sg.T('Section 2', enable_events=True, text_color='purple', k='-OPEN SEC2-TEXT')],
            [collapse(App_section, '-SEC2-')],
            #### Buttons at bottom ####
             sg.Button('Exit')]   
# Create the window
window = sg.Window("Remote", layout)

opened1, opened2 = True, True

#activity list
spotify = "adb shell monkey -p com.spotify.tv.android -c android.intent.category.LAUNCHER 1"
youtube = "adb shell monkey -p com.google.android.youtube.tv -c android.intent.category.LAUNCHER 1"
manager = "adb shell monkey -p com.xiaomi.mitv.tvmanager -c android.intent.category.LAUNCHER 1"
livetv = "adb shell monkey -p com.android.tv -c android.intent.category.LAUNCHER 1"
hotstar = "adb shell monkey -p in.startv.hotstar -c android.intent.category.LAUNCHER 1"

# Create an event loop
while True:
    event, values = window.read()
    
    if event.startswith('-OPEN SEC1-'):
        opened1 = not opened1
        window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened1 else SYMBOL_UP)
        window['-OPEN SEC1-'].update(visible=opened1)
    
    if event.startswith('-OPEN SEC2-'):
        opened2 = not opened2
        window['-OPEN SEC2-'].update(SYMBOL_DOWN if opened2 else SYMBOL_UP)
        window['-OPEN SEC2-'].update(visible=opened2)
        
    inputIP = values['-IP-']   
    connecttotv = "adb connect %s" % (inputIP)   
    disconnecttotv = "adb disconnect"                     
    if event == "Connect":
        print("IP address", inputIP)
        try:
            process = subprocess.Popen(connecttotv.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
    
    if event == "Disconnect":
        try:
            process = subprocess.Popen(disconnecttotv.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
        
    if event == "spotify":
        try:
            process = subprocess.Popen(spotify.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "youtube":
        try:
            process = subprocess.Popen(youtube.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "manager":
        try:
            process = subprocess.Popen(manager.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
       
    if event == sg.WIN_CLOSED or event == "Exit":
        break


window.close()