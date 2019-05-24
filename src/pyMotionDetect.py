import time
import cv2
import os
import sys
import argparse


import config
import service

#Arguments of cmd
def argParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='pyMotionDetect.conf')
    parser.add_argument('-d', '--device', default='/dev/video0')
    return parser.parse_args(sys.argv[1:])



#main code here
if __name__ == "__main__":
    sys.dont_write_bytecode = True
    #try:
    params = argParser()
    conf = config.load_config(params.config);
    print('try using '+params.device)
    print('try using '+params.config)
    service.Service(params.device, conf)
    #except Exception:
	#print(Exception)

    