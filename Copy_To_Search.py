import PySimpleGUI as sg
import time
import pyperclip
import webbrowser

def check_clipboard():
    # Get current clipboard content
    clipboard_content = pyperclip.paste()

    # Check if the content is different from the previous check
    if clipboard_content != check_clipboard.last_clipboard_content:
        # Perform a Google search
        search_query = f"https://www.google.com/search?q={clipboard_content}"
        webbrowser.open_new_tab(search_query)

        # Update last clipboard content
        check_clipboard.last_clipboard_content = clipboard_content

# Initialize the variable, which will store the last clipboard content
check_clipboard.last_clipboard_content = ""

layout = [[sg.Text("Clipboard Searcher")],[sg.Button("Turn ON", key="button")]]

window = sg.Window("CS", layout,margins=(50, 20))

# Create an event loop
flag = False

while True:
    event, values = window.read(timeout=0)
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break

    elif event == "button":
        button_text = window["button"].Widget.cget("text")

        if button_text == "Turn OFF":
            window["button"].update(text="Turn ON")
            flag = False
        else:
            window["button"].update(text="Turn OFF")
            flag = True
    
    if flag:
        check_clipboard()
        time.sleep(1)
        
window.close()