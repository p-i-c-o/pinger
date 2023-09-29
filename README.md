# pinger
python based ping software using telnet to bypass ICMP restrictions

## Prerequisites
- Python 3.x
- `telnetlib`
- `colorama`

## Installation
```
git clone https://github.com/p-i-c-o/pinger
cd pinger
chmod +x ./run
nano hosts
```
Then simply add your hosts in this format: `ipaddress:port`

Example: `www.google.com:80`

## Usage
Simply run:
`./run`
or
`python3 ping.py`
