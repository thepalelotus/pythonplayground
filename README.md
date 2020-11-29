# Python Playground

This is just a little repo for sharing the python scripts I write while learning and hoping to get better at writing my own tools. 

---

1. **ssidSniffer.py** - This script will automatically set the inteface you choose to `monitor mode` and then run a daemon that will change the channel of the interface from 1-14, every .5 seconds. The script will also make sure to disregard duplicate entries to the output. The output will contain the SSID as well as the BSSID of the access point.
