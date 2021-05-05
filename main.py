import PySimpleGUI as sg
import subprocess
import androidtv
from subprocess import check_output, CalledProcessError
sg.theme('DarkBlack')
status = [('\u2B24'+' Disconnected', 'red'), ('\u2B24'+' Connected', 'green')]
state = 0

def open_keyboard():
    layout = [[sg.Button("Q",key="q",size=(4,1)), sg.Button("W",key="w",size=(4,1)), sg.Button("E",key="e",size=(4,1)), sg.Button("R",key="r",size=(4,1)), sg.Button("T",key="t",size=(4,1)), sg.Button("Y",key="y",size=(4,1)), sg.Button("U",key="u",size=(4,1)), sg.Button("I",key="i",size=(4,1)), sg.Button("O",key="o",size=(4,1)), sg.Button("P",key="p",size=(4,1))],
             [sg.Button("A",key="a",size=(4,1)), sg.Button("S",key="s",size=(4,1)), sg.Button("D",key="d",size=(4,1)), sg.Button("F",key="f",size=(4,1)), sg.Button("G",key="g",size=(4,1)), sg.Button("H",key="h",size=(4,1)), sg.Button("J",key="j",size=(4,1)), sg.Button("K",key="k",size=(4,1)), sg.Button("L",key="l",size=(4,1))],
             [sg.Button("Z",key="z",size=(4,1)), sg.Button("X",key="x",size=(4,1)), sg.Button("C",key="c",size=(4,1)), sg.Button("V",key="v",size=(4,1)), sg.Button("B",key="b",size=(4,1)), sg.Button("N",key="n",size=(4,1)), sg.Button("M",key="m",size=(4,1))],
             [sg.Button("Quit",key="quit",size=(4,1))]]
    window = sg.Window("Keyboard", layout, modal=True, element_justification='c')
    while True:
        event, values = window.read()
        if event == "quit" or event == sg.WIN_CLOSED:
            break
    window.close()
    
def open_numpad():
    layout = [[sg.Button("7",key="7",size=(4,1)), sg.Button("8",key="8",size=(4,1)), sg.Button("9",key="9",size=(4,1))],
             [sg.Button("4",key="4",size=(4,1)), sg.Button("5",key="5",size=(4,1)), sg.Button("6",key="6",size=(4,1))],
             [sg.Button("1",key="1",size=(4,1)), sg.Button("2",key="2",size=(4,1)), sg.Button("3",key="3",size=(4,1))],
             [sg.Button("0",key="0",size=(4,1))],
             [sg.Button("Quit",key="quit",size=(4,1))]]
    window = sg.Window("Numpad", layout, modal=True, element_justification='c')
    while True:
        event, values = window.read()
        if event == "quit" or event == sg.WIN_CLOSED:
            break
    window.close()

layout = [[sg.Button("Input source",key="inputsource"), sg.Text("Input IP address to connect via ADB", justification='c'), sg.Text(text=status[state][0], text_color=status[state][1], size=(20, 1),
          justification='right', key='INDICATOR')], [sg.InputText(key='-IP-')], [sg.Button("Connect"), sg.Button("Disconnect")], [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button("Netflix",key='netflix', button_color=('black', 'red')), sg.Button("Spotify",key='spotify', button_color=('white', 'green')), sg.Button("Youtube",key="youtube", button_color=('white', 'red')), sg.Button("Hotstar", key="hotstar", button_color=('white', 'blue')), sg.Button("TV Manager",key="manager"), sg.Button("Live TV",key="livetv"), sg.Button("Menu",key="menu")],
          [sg.Button("▲",key="up",size=(4,1)), sg.Button("▼",key="down",size=(4,1)), sg.Button("⌂",key="home",size=(4,1)), sg.Button("◀",key="left",size=(4,1)), sg.Button("▶",key="right",size=(4,1)), sg.Button("Select",key="select",size=(5,1)), sg.Button("Back",key="back",size=(4,1))],
          [sg.Button("⏮",key="prev",size=(4,1)), sg.Button("⏪",key="rewind",size=(4,1)), sg.Button("⏯︎", key="playpause",size=(4,1)), sg.Button("⏩",key="fastforward",size=(4,1)), sg.Button("⏭",key="next",size=(4,1))],
          [sg.Button("Vol+",key="volumeup",size=(4,1)), sg.Button("Mute",key="mute",size=(4,1)), sg.Button("Vol-",key="volumedown",size=(4,1))],
          [sg.Button("Keyboard",key='keyboard'), sg.Button("Numpad",key="numpad")],
          [sg.Button("Quit",size=(4,1))]]
# Create the window
window = sg.Window("Remote", layout)

#activity list
spotify = "adb shell monkey -p com.spotify.tv.android -c android.intent.category.LAUNCHER 1"
youtube = "adb shell monkey -p com.google.android.youtube.tv -c android.intent.category.LAUNCHER 1"
manager = "adb shell monkey -p com.xiaomi.mitv.tvmanager -c android.intent.category.LAUNCHER 1"
livetv = "adb shell monkey -p com.android.tv -c android.intent.category.LAUNCHER 1"
hotstar = "adb shell monkey -p in.startv.hotstar -c android.intent.category.LAUNCHER 1"
netflix = "adb shell monkey -p com.netflix.mediaclient -c android.intent.category.LAUNCHER 1"
#navigation
dpad_left = "adb shell input keyevent 21"
dpad_right = "adb shell input keyevent 22"
dpad_up = "adb shell input keyevent 19"
dpad_down = "adb shell input keyevent 20"
dpad_home = "adb shell input keyevent 3"
menu = "adb shell input keyevent 82"
select = "adb shell input keyevent 66"
back = "adb shell input keyevent 4"
#media controls
inputsource = "adb shell input keyevent 178"
media_playpause = "adb shell input keyevent 85"
media_fastforward = "adb shell input keyevent 90"
media_rewind = "adb shell input keyevent 89"
media_previous = "adb shell input keyevent 88"
media_next = "adb shell input keyevent 87"
volup = "adb shell input keyevent 24"
voldown = "adb shell input keyevent 25"
mute = "adb shell input keyevent 164"
# Create an event loop
while True:
    event, values = window.read()
    inputIP = values['-IP-']   
    connecttotv = "adb connect %s" % (inputIP)   
    disconnecttotv = "adb disconnect"                     
    if event == "Connect" and inputIP !=None:
        print("Connecting to IP address", inputIP)
        try:
            process = subprocess.Popen(connecttotv.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            adb_output = check_output(["adb", "devices"])
            if adb_output != None:
                state = 1
                print("Connected!")
        except CalledProcessError as e:
            print (e.returncode)
    
    if event == "Disconnect":
        state = 0
        print("Disconnected")
        try:
            process = subprocess.Popen(disconnecttotv.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong while disconnecting")
    
    if event in ('Disconnect', 'Connect'):
        value, text_color = status[state]
        window['INDICATOR'].update(value=value, text_color=text_color)
    
    if event == "inputsource":
        try:
            process = subprocess.Popen(inputsource.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("err_input")
            
    if event == "netflix":
        try:
            process = subprocess.Popen(netflix.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
        
    if event == "spotify":
        try:
            process = subprocess.Popen(spotify.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("err_spotify")
            
    if event == "youtube":
        try:
            process = subprocess.Popen(youtube.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("err_youtube")
            
    if event == "hotstar":
        try:
            process = subprocess.Popen(hotstar.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "manager":
        try:
            process = subprocess.Popen(manager.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
       
    if event == "livetv":
        try:
            process = subprocess.Popen(livetv.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "up":
        try:
            process = subprocess.Popen(dpad_up.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "down":
        try:
            process = subprocess.Popen(dpad_down.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "left":
        try:
            process = subprocess.Popen(dpad_left.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "right":
        try:
            process = subprocess.Popen(dpad_right.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "home":
        try:
            process = subprocess.Popen(dpad_home.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "select":
        try:
            process = subprocess.Popen(select.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "back":
        try:
            process = subprocess.Popen(back.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "rewind":
        try:
            process = subprocess.Popen(media_rewind.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "prev":
        try:
            process = subprocess.Popen(media_previous.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "playpause":
        try:
            process = subprocess.Popen(media_playpause.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "next":
        try:
            process = subprocess.Popen(media_next.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "fastforward":
        try:
            process = subprocess.Popen(media_fastforward.split(), stdout=subsubprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "volumeup":
        try:
            process = subprocess.Popen(volup.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "volumedown":
        try:
            process = subprocess.Popen(voldown.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "mute":
        try:
            process = subprocess.Popen(mute.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "keyboard":
        open_keyboard()
        
    if event == "numpad":
        open_numpad()
    
    if event == sg.WIN_CLOSED or event == "Quit":
        break


window.close()