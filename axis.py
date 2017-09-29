#!/usr/bin/env python
#
# Axis camera driver.
#
# dscotece, msolimando
#

import wget
import time
import datetime

def video(hostname):
    #start record
    url = 'http://' + hostname + '/axis-cgi/mjpg/video.cgi?duration=60'
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H:%M:%S')
    file_name = 'video-' + st + '.mjpg'
    path = '/mnt/' + file_name
    wget.download(url, path)

def main():
    hostname = '192.168.0.90'        # default IP address
    video(hostname)

if __name__ == "__main__":
    main()