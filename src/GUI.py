import PySimpleGUI as sg
from graph import generate_button
# Define the window's contents
# layout = [[sg.Text("Enter the number of nodes")],
#           [sg.Input(key='nodes')],
#           [sg.Text("Enter the number of edges")],
#           [sg.Input(key='edges')],
#   [sg.Button('Generate', key='generate_button')]]
layout = [[sg.Column(
    [[sg.Text("Enter the number of nodes")],
     [sg.Input(key='nodes', size=(25, 10))]]),
    sg.Column(
    [[sg.Text("Enter the number of edges")],
     [sg.Input(key='edges', size=(25, 10))]])
],
    [sg.Button('Generate', key='generate_button',
               pad=((0, 0), (200, 0)))]
]
# Create the window
sg.theme('DarkGrey12')
window = sg.Window('Generate random graph', layout,
                   size=(500, 500), element_justification='c')

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    window['generate_button'].update("regenerate graph")

    if event == 'generate_button':
        generate_button(values)

window.close()
