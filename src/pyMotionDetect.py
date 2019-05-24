import time
import cv2
import os
import sys
import argparse


import config
import service

#Arguments of cmd
def argParser():
    islinux = sys.platform.find('nux')
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='pyMotionDetect.conf', help='you can use any configuration')
    parser.add_argument('-i', '--input', default='/dev/video0', help='your device for capture, 0 or /dev/video0 - default')
    if islinux > 0:
	parser.add_argument('-d', '--deamon', action='store_const', const=True, help='run as service')

    return parser.parse_args(sys.argv[1:])


def run_deamon():
    pid = os.fork()

    if pid is 0:
	print('\033[93m'+'runinig as deamon'+'\033[0m')
    else:
	exit(0)


#main code here
if __name__ == "__main__":
    try:
	params = argParser()
	if params.deamon:
	    run_deamon()
	    sys.stdout = open(os.devnull,'w')

	conf = config.load_config(params.config);
	print('try using '+ params.input)
	print('try using '+ params.config)
	service.Service(params.input, conf)
    except Exception:
	print('\033[93m pyMotionDetect - fatal error, serivce is down \033[0m')

    