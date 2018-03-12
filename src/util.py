class Logger(object):
    def __init__(self, logfile, verbose):
       self.log = open(logfile,"w") 
       self.v =verbose

        
    def closeLog(self):
       self.log.write("Closing log."+"\n")
       self.log.close()

    def logAndPrint(self, s):
        print(s+"\n")
        self.log.write(s+"\n")
       
    def vLog(self, s):
        if v:
            log.write(s+"\n")

