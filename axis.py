#!/usr/bin/env python
#
# Axis camera driver.
#
# dscotece, msolimando
#

import urllib2
import time
import datetime


def image():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S')
    url = 'https://b.thumbs.redditmedia.com/0jcpyxFCewwL8R611kJgoCUxXxqGtDow56YlsO8lAxY.png'
    imgfile = urllib2.urlopen(url)
    name = 'test' + st + '.png'
    output = open(name, 'wb')
    output.write(imgfile.read())
    output.close()

def video():
    #start record
    time.sleep(61)
    #stop record


def main():
    arg_defaults = {
        'hostname': '192.168.0.90',       # default IP address
        'username': 'root',               # default login name
        'password': ''
    }

    image()

if __name__ == "__main__":
    main()