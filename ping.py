# ┌──────────────────────────────────┐
# │ This code was created by p-i-c-o │
# │ GitHub:   www.github.com/p-i-c-o │
# │                                  │
# │ No referral is required!         │
# │ This was created for the world.  │
# └──────────────────────────────────┘

# pinger by p-i-c-o
# https://www.github.com/p-i-c-o/pinger
# pinger is an uptime tracker for the CLI that bypasses ICMP restrictions by using telnet

# PLANS:
# Neat names for hosts
# Logging
# GUI with PySimpleGUI




import telnetlib, colorama, time, os
from colorama import Fore, Style
from datetime import datetime

import ports # Custom port list "ports.py"
from ports import portlist # Importing the ports dictionary
plist = ports.portlist

# Defining the base vars
hosts = []
output = ""


# Uses the port lists to return the plain text port use (ex: 80 -> HTTP)
def getport(port_num):
    description = plist.get(int(port_num))
    if description is not None:
        return description
    else:
        return str(port_num)


# Uses telnetlib to check if a host is online an returns a concatenated message with colors
def check_online(hostname, port):
    try:
        tn = telnetlib.Telnet(hostname, port, timeout=1)
        tn.close()
        stat = Fore.GREEN + "[✓]" + Style.RESET_ALL
        return f"{stat} {hostname:<40} {port}: {getport(port)}"
    except (ConnectionRefusedError, OSError) as e:
        stat = Fore.RED + "[×]" + Style.RESET_ALL
        return f"{stat} {hostname:<40} {port}: {getport(port)}"

# Returns date and time in the "DD/MM/YYYY | HH:MM:SS"
def gettime():
    now = datetime.now()
    formatted_date = now.strftime("%d/%m/%Y")
    formatted_time = now.strftime("%H:%M:%S")
    return f"{formatted_date} | {formatted_time}"

# This reads the hosts file and removes any empty lines in order to prevent trying to ping ""
with open('hosts', 'r+') as f:
    temp = f.readlines()
for i in temp:
    hosts.append(i.replace('\n', ''))

# Start of loop
try:
  while True:
      # Defining header, shows date and time and prints table headers
      header = f"""Pinger
{gettime()}

    {Style.BRIGHT}[HOSTNAME/URL]{" "*27}[PORT]{Style.RESET_ALL}
"""
      output += header # Adding "header" to output first to put it at the top
      for i in hosts: # Iteratiing through the hosts to convert the raw text from the file into the "ip" and "port" vars
          host = i.split(':')
          ip = host[0]
          port = host[1]
          output = output + check_online(ip, port) + "\n" # Appends the result of "check_online" to the output var
      os.system('clear')
      print(output) # Print the header and the scanned hosts
      output = ""
      time.sleep(1)
except KeyboardInterrupt: # Catches the keyboard interrupt and neatly exits
  print('\nQuitting...')
