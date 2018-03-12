#Import
from src import Timelapser
import argparse
import picamera
import time
from datetime import datetime
import os

#Parse Arguements
parser = argparse.ArgumentParser(description='Take timelapse images. Should be run as a background thread.')
parser.add_argument('integers', metavar='m', type=int, nargs='+', default=1,
                    help='Number of minutes between each snapshot')



args = parser.parse_args()


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


dir='timelapse_results'

if not os.path.exists(dir):
    os.makedirs(dir)

min=m*60

while True:
    file = datetime.now().strftime("%m-%d_%H:%M:S")+'.jpg'
    camera.capture(file)
    time.sleep(min)


