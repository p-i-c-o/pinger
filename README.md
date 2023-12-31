![Banner](.banner.png)
python based ping software using telnet to bypass ICMP restrictions

## Prerequisites
- Python 3.x
  - `telnetlib` _May be deprecated on newer python versions_
  - `colorama`

## Installation
```
git clone https://github.com/p-i-c-o/pinger
cd pinger
nano hosts
```

Then simply add your hosts in this format: `ipaddress:port:neatname`
- **IPADDRESS**: This can be an IPV4, IPV6 or HOSTNAME IP address.
- **PORT**: This can be any port you want TELNET to scan
- **NEATNAME**: This can be anything, it will be shown at the front so the user can quickly identify the host

Example: `www.google.com:80:Google`


## Usage
Simply run:
`python3 ping.py`

## Tested on
- [~] macOS
- [✓] Ubuntu 22.04.3 LTS

## Screenshots
![Preview of pinger when run in the terminal](.screen.png)
