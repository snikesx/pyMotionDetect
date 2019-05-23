import cv2
import time
import numpy as np


class Capture:
    def __init__(self, device, config):
	self.cam = cv2.VideoCapture(device)

	try:
	    self.cam.set(3,config['video']['width'])
	    self.cam.set(4,config['video']['height'])
	except:
	    self.cam.set(3,320)
	    self.cam.set(4,240)

	self.config = config
	self.fcc = cv2.VideoWriter_fourcc(*'XVID')
	self.max_frame = 5000
	self.frame_count = 0
	self.vid = None


    def getImage(self):
	ret, img = self.cam.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	return img, gray


    def compareImage(self, img1, img2):
	res = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
	return res[0][0]


    def fastCompare(self, img1, img2):
	img1_norm = img1 / np.sqrt(np.sum(img1**2))
	img2_norm = img2 / np.sqrt(np.sum(img2**2))
	return np.sum(img2_norm*img1_norm)


    def writeVideo(self, frame):
	try:
	    path = self.config['video_path']
	except:
	    path = ''

	if self.frame_count > self.max_frame or self.vid==None:
	    if self.vid!=None:
		self.vid.release()
	    self.frame_count = 0

	    filename = path + time.strftime('%Y-%m-%d_%X')+'.avi'
	    print(filename)
	    w,h = frame.shape[:2]
	    self.vid = cv2.VideoWriter(filename, self.fcc, 20.0, (w,h))
	
	self.frame_count+=1
	cv2.putText(frame, time.strftime('%d.%m.%Y %X'), (5,10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,255,255),1)
	self.vid.write(frame)


    def __del__(self):
	if self.cam:
	    self.cam.release();

	if self.vid:
	    self.vid.release();

