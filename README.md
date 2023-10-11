# pinger
python based ping software using telnet to bypass ICMP restrictions

## Prerequisites
- Python 3.x
- `telnetlib` _May be deprecated on new python versions_
- `colorama`

## Installation
```
git clone https://github.com/p-i-c-o/pinger
cd pinger
nano hosts
```
Then simply add your hosts in this format: `ipaddress:port`

Example: `www.google.com:80`

## Usage
Simply run:
`python3 ping.py`

## Tested on
- macOS
- Ubuntu 22.04.3 LTS
