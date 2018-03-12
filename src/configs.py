import configparser
import picamera
from util import Logger

class Conf():
     
    def __init__(self, logger):
        self.logger = logger
        self.camera = picamera.PiCamera()
    
    def configure():
       
        #Config Set up
        config = configparser.ConfigParser()
        config.read('config.ini')
        config.sections()

        #self.camera Setup
        sec = 'Camera'

        sharpness = config[sec]['sharpness']
        logger.logAndPrint(sharpness) 
        self.camera.sharpness = sharpness

        contrast = config[sec]['contrast']
        logger.logAndPrint(contrast) 
        self.camera.contrast = contrast

        brightness = config[sec]['brightness']
        logger.logAndPrint(brightness) 
        self.camera.brightness = brightness

        saturation = config[sec]['saturation']
        logger.logAndPrint(saturation)
        self.camera.saturation = saturation

        ISO = config[sec]['ISO']
        logger.logAndPrint(ISO)
        self.camera.ISO = ISO


        video_stablization = config[sec]['video_stabilization']
        logAndPring(video_stablization)
        self.camera.video_stabilization = video_stablization

        exposure_compensation= config[sec]['exposure_compensation']
        logger.logAndPrint(exposure_compensation) 
        self.camera.exposure_compensation = exposure_compensation

        exposure_mode = config[sec]['exposure_mode']
        logger.logAndPrint(exposure_mode) 
        self.camera.exposure_mode = exposure_mode

        meter_mode = config[sec]['meter_mode']
        logger.logAndPrint(meter_mode)
        self.camera.meter_mode = meter_mode

        awb_mode = config[sec]['awb_mode']
        logger.logAndPrint(awb_mode) 
        self.camera.awb_mode = awb_mode

        image_effect = config[sec]['image_effect'] 
        logger.logAndPrint(image_effect) 
        self.camera.image_effect = image_effect

        color_effects = config[sec]['color_effects']
        logger.logAndPrint(color_effects) 
        self.camera.color_effects = color_effects

        rotation = config[sec]['rotation']
        logger.logAndPrint(rotation)
        self.camera.rotation = rotation

        onfig[sec]['hflip']
        logger.logAndPrint(hflip) 
        self.camera.hflip = hflip

        vflip = config[sec]['vflip']
        logger.logAndPrint(vflip) 
        self.camera.vflip = vflip

        crop = config[sec]['crop']
        logger.logAndPrint(crop) 
        self.camera.crop = crop


