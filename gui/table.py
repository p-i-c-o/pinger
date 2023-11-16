import PySimpleGUI as sg

# Define the data for the table
data = [
    ['John', 25, 'Engineer'],
    ['Alice', 30, 'Designer'],
    ['Bob', 28, 'Developer'],
]

# Define the column headings
headings = ['Name', 'Age', 'Occupation']

# Create the layout for the window
layout = [
    [sg.Table(values=data, headings=headings, auto_size_columns=False, justification='right', display_row_numbers=False, num_rows=5, col_widths=[15, 5, 15])],
    [sg.Button('Exit')],
]

# Create the window
window = sg.Window('Table Example', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
