import PySimpleGUI as sg
import subprocess as sp
import src.intents_keyevents as ik
from subprocess import check_output, CalledProcessError

sg.theme('DarkBlack')

status = [('\u2B24'+' Disconnected', 'red'), ('\u2B24'+' Connected', 'green')]
state = 0

def open_keyboard():
    layout = [[sg.Text(size=(40,1), key='-OUTPUT-')],
             [sg.Button("Q",key="q",size=(4,1)), sg.Button("W",key="w",size=(4,1)), sg.Button("E",key="e",size=(4,1)), sg.Button("R",key="r",size=(4,1)), sg.Button("T",key="t",size=(4,1)), sg.Button("Y",key="y",size=(4,1)), sg.Button("U",key="u",size=(4,1)), sg.Button("I",key="i",size=(4,1)), sg.Button("O",key="o",size=(4,1)), sg.Button("P",key="p",size=(4,1))],
             [sg.Button("A",key="a",size=(4,1)), sg.Button("S",key="s",size=(4,1)), sg.Button("D",key="d",size=(4,1)), sg.Button("F",key="f",size=(4,1)), sg.Button("G",key="g",size=(4,1)), sg.Button("H",key="h",size=(4,1)), sg.Button("J",key="j",size=(4,1)), sg.Button("K",key="k",size=(4,1)), sg.Button("L",key="l",size=(4,1))],
             [sg.Button("Z",key="z",size=(4,1)), sg.Button("X",key="x",size=(4,1)), sg.Button("C",key="c",size=(4,1)), sg.Button("V",key="v",size=(4,1)), sg.Button("B",key="b",size=(4,1)), sg.Button("N",key="n",size=(4,1)), sg.Button("M",key="m",size=(4,1))],
             [sg.Button("Backspace",key="backspace"), sg.Button("Quit",key="quit",size=(4,1))]]
    window = sg.Window("Keyboard", layout, modal=True, element_justification='c')
    while True:
        event, values = window.read()
        
        if event == "a":
            try:
                process = sp.Popen(ik.a.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
            
        if event == "b":
            try:
                process = sp.Popen(ik.b.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "c":
            try:
                process = sp.Popen(ik.c.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "d":
            try:
                process = sp.Popen(ik.d.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
        
        if event == "e":
            try:
                process = sp.Popen(ik.e.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "f":
            try:
                process = sp.Popen(ik.f.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "g":
            try:
                process = sp.Popen(ik.g.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "h":
            try:
                process = sp.Popen(ik.h.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "i":
            try:
                process = sp.Popen(ik.i.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "j":
            try:
                process = sp.Popen(ik.j.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "k":
            try:
                process = sp.Popen(ik.k.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
            
        if event == "l":
            try:
                process = sp.Popen(ik.l.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "m":
            try:
                process = sp.Popen(ik.m.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "n":
            try:
                process = sp.Popen(ik.n.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
        
        if event == "o":
            try:
                process = sp.Popen(ik.o.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "p":
            try:
                process = sp.Popen(ik.p.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "q":
            try:
                process = sp.Popen(ik.q.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "r":
            try:
                process = sp.Popen(ik.r.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "s":
            try:
                process = sp.Popen(ik.s.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "t":
            try:
                process = sp.Popen(ik.t.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "u":
            try:
                process = sp.Popen(ik.u.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "v":
            try:
                process = sp.Popen(ik.v.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "w":
            try:
                process = sp.Popen(ik.w.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "x":
            try:
                process = sp.Popen(ik.x.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "y":
            try:
                process = sp.Popen(ik.y.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "z":
            try:
                process = sp.Popen(ik.z.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "backspace":
            try:
                process = sp.Popen(ik.backspace.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
            
        if event == "quit" or event == sg.WIN_CLOSED:
            break
    window.close()
    
def open_numpad():
    layout = [[sg.Text(size=(40,1), key='-OUTPUT-')],
             [sg.Button("7",key="7",size=(4,1)), sg.Button("8",key="8",size=(4,1)), sg.Button("9",key="9",size=(4,1))],
             [sg.Button("4",key="4",size=(4,1)), sg.Button("5",key="5",size=(4,1)), sg.Button("6",key="6",size=(4,1))],
             [sg.Button("1",key="1",size=(4,1)), sg.Button("2",key="2",size=(4,1)), sg.Button("3",key="3",size=(4,1))],
             [sg.Button("0",key="0",size=(4,1))],
             [sg.Button("Quit",key="quit",size=(4,1))]]
    window = sg.Window("Numpad", layout, modal=True, element_justification='c')
    while True:
        event, values = window.read()
        
        if event == "1":
            try:
                process = sp.Popen(ik.num1.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
            
        if event == "2":
            try:
                process = sp.Popen(ik.num2.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "3":
            try:
                process = sp.Popen(ik.num3.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "4":
            try:
                process = sp.Popen(ik.num4.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
        
        if event == "5":
            try:
                process = sp.Popen(ik.num5.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "6":
            try:
                process = sp.Popen(ik.num6.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "7":
            try:
                process = sp.Popen(ik.num7.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "8":
            try:
                process = sp.Popen(ik.num8.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "9":
            try:
                process = sp.Popen(ik.num9.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
                
        if event == "0":
            try:
                process = sp.Popen(ik.num0.split(), stdout=sp.PIPE)
                output, error = process.communicate()
            except:
                window['-OUTPUT-'].update("Something went wrong")
        
        if event == "quit" or event == sg.WIN_CLOSED:
            break
    window.close()

layout = [[sg.Button("Sleep",key="sleep"), sg.Text("Input IP address to connect via ADB", justification='c'), sg.Text(text=status[state][0], text_color=status[state][1], size=(20, 1),
          justification='right', key='INDICATOR')], [sg.InputText(key='-IP-')], [sg.Button("Connect"), sg.Button("Disconnect")], [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button("Netflix",key='netflix', button_color=('black', 'red')), sg.Button("Spotify",key='spotify', button_color=('white', 'green')), sg.Button("Youtube",key="youtube", button_color=('white', 'red')), sg.Button("Hotstar", key="hotstar", button_color=('white', 'blue')), sg.Button("TV Manager",key="manager"), sg.Button("Live TV",key="livetv"), sg.Button("Menu",key="menu")],
          [sg.Button("▲",key="up",size=(4,1)), sg.Button("▼",key="down",size=(4,1)), sg.Button("⌂",key="home",size=(4,1)), sg.Button("◀",key="left",size=(4,1)), sg.Button("▶",key="right",size=(4,1)), sg.Button("Select/Enter",key="select"), sg.Button("Back",key="back",size=(4,1))],
          [sg.Button("⏮",key="prev",size=(4,1)), sg.Button("⏪",key="rewind",size=(4,1)), sg.Button("⏯︎", key="playpause",size=(4,1)), sg.Button("⏩",key="fastforward",size=(4,1)), sg.Button("⏭",key="next",size=(4,1))],
          [sg.Button("Vol+",key="volumeup",size=(4,1)), sg.Button("Mute",key="mute",size=(4,1)), sg.Button("Vol-",key="volumedown",size=(4,1))],
          [sg.Button("Keyboard",key='keyboard'), sg.Button("Numpad",key="numpad")],
          [sg.Button("Quit",size=(4,1))]]
# Create the window
window = sg.Window("Remote", layout)

# Create an event loop
while True:
    event, values = window.read()
    inputIP = values['-IP-']   
    connecttotv = "adb connect %s" % (inputIP)   
    disconnecttotv = "adb disconnect"                     
    if event == "Connect" and inputIP !=None:
        print("Connecting to IP address", inputIP)
        try:
            process = sp.Popen(connecttotv.split(), stdout=sp.PIPE)
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
            process = sp.Popen(disconnecttotv.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong while disconnecting")
    
    if event in ('Disconnect', 'Connect'):
        value, text_color = status[state]
        window['INDICATOR'].update(value=value, text_color=text_color)
    
    if event == "inputsource":
        try:
            process = sp.Popen(ik.inputsource.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("err_input")
            
    if event == "netflix":
        try:
            process = sp.Popen(ik.netflix.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
        
    if event == "spotify":
        try:
            process = sp.Popen(ik.spotify.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("err_spotify")
            
    if event == "youtube":
        try:
            process = sp.Popen(ik.youtube.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("err_youtube")
            
    if event == "hotstar":
        try:
            process = sp.Popen(ik.hotstar.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "manager":
        try:
            process = sp.Popen(ik.manager.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
       
    if event == "livetv":
        try:
            process = sp.Popen(ik.livetv.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "up":
        try:
            process = sp.Popen(ik.dpad_up.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "down":
        try:
            process = sp.Popen(ik.dpad_down.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "left":
        try:
            process = sp.Popen(ik.dpad_left.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "right":
        try:
            process = sp.Popen(ik.dpad_right.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "home":
        try:
            process = sp.Popen(ik.dpad_home.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "select":
        try:
            process = sp.Popen(ik.select.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "back":
        try:
            process = sp.Popen(ik.back.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "rewind":
        try:
            process = sp.Popen(ik.media_rewind.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "prev":
        try:
            process = sp.Popen(ik.media_previous.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "playpause":
        try:
            process = sp.Popen(ik.media_playpause.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "next":
        try:
            process = sp.Popen(ik.media_next.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "fastforward":
        try:
            process = sp.Popen(ik.media_fastforward.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "volumeup":
        try:
            process = sp.Popen(ik.volup.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "volumedown":
        try:
            process = sp.Popen(ik.voldown.split(), stdout=sp.PIPE)
            output, error = process.communicate()
        except:
            window['-OUTPUT-'].update("Something went wrong")
            
    if event == "mute":
        try:
            process = sp.Popen(ik.mute.split(), stdout=sp.PIPE)
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