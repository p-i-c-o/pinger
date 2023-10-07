
import telnetlib, colorama, time, os
from colorama import Fore, Style
from datetime import datetime

import ports
from ports import portlist
plist = ports.portlist

hosts = []
output = ""

def getport(port_num):
    description = plist.get(int(port_num))
    if description is not None:
        return description
    else:
        return str(port_num)


def check_online(hostname, port):
    try:
        tn = telnetlib.Telnet(hostname, port, timeout=1)
        tn.close()
        stat = Fore.GREEN + "[✓]" + Style.RESET_ALL
        return f"{stat} {hostname:<40} {port}: {getport(port)}"
    except (ConnectionRefusedError, OSError) as e:
        stat = Fore.RED + "[×]" + Style.RESET_ALL
        return f"{stat} {hostname:<40} {port}: {getport(port)}"

def gettime():
    now = datetime.now()
    formatted_date = now.strftime("%d/%m/%Y")
    formatted_time = now.strftime("%H:%M:%S")
    return f"{formatted_date} | {formatted_time}"


with open('hosts', 'r+') as f:
    temp = f.readlines()




for i in temp:
    hosts.append(i.replace('\n', ''))
try:
  while True:
      header = f"""Pinger
{gettime()}

    {Style.BRIGHT}[HOSTNAME/URL]{" "*27}[PORT]{Style.RESET_ALL}
"""
      output += header
      for i in hosts:
          host = i.split(':')
          ip = host[0]
          port = host[1]
          output = output + check_online(ip, port) + "\n"
      os.system('clear')
      print(output)
      output = ""
      time.sleep(1)
except KeyboardInterrupt:
  print('\nQuitting...')
