import time
import capture
import sys

def Service(device, config):
    cap = capture.Capture(device, config)
    run = True
    img1, gray1 = cap.getImage()
    
    time.sleep(0.1)
    try:
	sensor = config['sensetive']
    except:
	sensor = 0.997

    writeCount = 0
    slp = 0.33
    print ('\033[92m'+'webcam is running'+'\033[0m')
    while run:
	try:
	    img, gray2 = cap.getImage()
	    imgDiff = cap.compareImage(gray1, gray2)
	    frmNum = cap.getFrame()
	    print "\033[K",'cmp:',imgDiff, '\ttm:', slp, '\tsens:', sensor, '\tfrm:',frmNum,"\r",
	    sys.stdout.flush()

	    if imgDiff < sensor or writeCount>0:
		slp = 0.07
		if writeCount ==0:
		    writeCount = 50

		cap.writeVideo(img)
		writeCount-=1
	    else:
		slp = 0.33


	    gray1 = gray2
	    time.sleep(slp)
	except KeyboardInterrupt:
	    print('\033[93m'+'\nwebcam is stoped\n'+'\033[0m')
	    run = False
	    break
    
    del cap