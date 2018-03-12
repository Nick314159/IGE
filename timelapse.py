#Import
import argparse
import picamera
import time

#Parse Arguements
parser = argparse.ArgumentParser(description='Take timelapse images. Should be run as a background thread.')
parser.add_argument('integers', metavar='m', type=int, nargs='+', default=60,
                    help='Number of minutes between each snapshot')



#Camera Setup
camera = picamera.PiCamera()
camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50
camera.saturation = 0
camera.ISO = 0
camera.video_stabilization = False
camera.exposure_compensation = 0
camera.exposure_mode = 'auto'
camera.meter_mode = 'average'
camera.awb_mode = 'auto'
camera.image_effect = 'none'
camera.color_effects = None
camera.rotation = 0
camera.hflip = False
camera.vflip = False
camera.crop = (0.0, 0.0, 1.0, 1.0)

args = parser.parse_args()

#min = h*60
min = 1
i = 0
while True:
    i = i +1
    camera.capture('image'+str(i)+'.jpg')
    time.sleep(min)
