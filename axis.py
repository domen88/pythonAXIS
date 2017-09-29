#!/usr/bin/env python
#
# Axis camera driver.
#
# dscotece, msolimando
#

import wget

def video(hostname):
    #start record
    url = 'http://' + hostname + '/axis-cgi/mjpg/video.cgi?duration=60'
    path = '/mnt/'
    wget.download(url, path)

def main():
    hostname = '192.168.0.90'        # default IP address
    video(hostname)

if __name__ == "__main__":
    main()