#Import
from src import Timelapser
from src.configs import Conf
from src.util import Logger

import argparse
import time
import os
from datetime import datetime


#Parse Arguements
parser = argparse.ArgumentParser(description='Take timelapse images. Should be run as a background thread.')
parser.add_argument(
    "-m","--minutes", default=1,  required=False, help='Number of minutes between each snapshot')
parser.add_argument(
    "-v", "--verbose", action="store_true", required=False,  help="increase output verbosity",)
parser.add_argument(
    "-o", "--outputDirectory", default='timelapse_results', required=False, help="Directory in which to output files, photos, and videos")
parser.add_argument(
    "-l", "--logDirectory", default='logs', required=False, help="Directory in which to store log files")
parser.add_argument(
    "-x", "--maxIterations", default = -1, type=int, required=False, help="Max number of iterations of length [--minutes]")
args = parser.parse_args()



#Verbose set up
v = args.verbose
    
#Log Setup
logs= args.logDirectory+'/'
if not os.path.exists(logs):
    os.makedirs(logs)

logfile = logs + datetime.now().strftime("%m-%d-%Y_%H:%M:S")+".txt"

logger = Logger(logfile, v)
if v:
    logger.logAndPrint("Verbosity turned on") 

#Configurations
conf = Conf(logger)
camera = conf.camera
    
#Output Setup
output = args.outputDirectory+"/"
if not os.path.exists(output):
    os.makedirs(output)

#Iterations
it =  args.maxIterations
i = 0

#Arguement Conversion
minutes = args.minutes
seconds =float( minutes) * 60.0

#Primary code
predicate = True
while predicate:
    try:
        if it!=-1 or i >= it:
            predicate = False
            
        i = i + 1
        
        logger.logAndPrint("Iteration "+str(i))
        file = output + datetime.now().strftime("%m-%d_%H:%M:S")+'.jpg'
        logger.logAndPrint("Capturing Snapshot...")
        camera.capture(file)
        logger.logAndPrint("Snapshot Captured!")
        logger.logAndPrint("Sleeping for "+ str(minutes) + " Minutes...")
        time.sleep(seconds)
    except KeyboardInterrupt:
        logger.logAndPrint("Recived Abort Signal!")
        logger.logAndPrint("Closing log.")
        logger.closeLog()
        
    except Exception as e:
       logger. logAndPrint("Encountered unexpected excpetion:")
       logger.logAndPrint(str(e))
       logger.closeLog()
    
    logger.logAndPrint("Finished Iteration "+str(i))

        

