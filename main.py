import PySimpleGUI as sg

text_font = ("Arial", 20)
button_font = ("Arial", 16)
bg_color = "#dba5e6"
convert_bg_color = "#22b50d"
cancel_bg_color = "#f01818"
layout = [[sg.Text("Welcome to My TTS Assistant", font=text_font, background_color=bg_color)],[sg.InputText(size=(80, 2), expand_y = True, default_text="Type text here", background_color="#f6cafb")], [sg.Button("Convert", font=button_font), sg.Button("Cancel", font=button_font)]]
window = sg.Window(title="My TTS Assistant", layout=layout, size=(600, 600), margins=(40,40), background_color=bg_color, element_justification="c")


while True:
    event, values = window.read()
    if event == "Convert" or event == sg.WIN_CLOSED:
        sg.popup("Saved to 'hello.mp3' file!")
        break;

window.close()


