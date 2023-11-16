import PySimpleGUI as sg
import telnetlib, colorama, time, os

import ports
from ports import portlist # Importing the ports dictionary
plist = ports.portlist

def check_online(hostname, port):
    try:
        tn = telnetlib.Telnet(hostname, port, timeout=1)
        tn.close()
        return "[✓]"
    except (ConnectionRefusedError, OSError) as e:
        return "[×]"


def getport(port_num):
    description = plist.get(int(port_num))
    if description is not None:
        return description
    else:
        return str(port_num)



# Read the content of the "hosts" file
with open('../hosts', 'r') as file:
    host_lines = file.readlines()


# TABLE FOR HOSTS
headings = ['', 'Host', 'Address', 'Port', 'Port Type']

table = []
for line in host_lines:
    rawout = line.strip()
    splitraw = rawout.split(':')


    ip = splitraw[0]
    port = splitraw[1]
    name = splitraw[2]
    state = check_online(ip, port)
    porttype = getport(port)

    table.append([state, name, ip, port, porttype])



# Define the layout for the window
layout = [
    [sg.Text('Text Boxes from "hosts" File')],
    [sg.Table(values=table, headings=headings, auto_size_columns=False, justification='left', display_row_numbers=False, col_widths=[3, 15, 15, 5, 10])],
]

# Create a text box for each line in the "hosts" file


layout.append([sg.Button('Save')])

# Create the window
window = sg.Window('Text Boxes from "hosts" File', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()
