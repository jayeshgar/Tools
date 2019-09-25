import threading
import schedule
import time
from channels import Group
from subprocess import call,getoutput
from datetime import datetime
from apollo.cmdhandler import cmdhandler
def job():
	output=cmdhandler.executecmd(["administrator","adminport=2010","display","node"])
	Group("apollo").send({"text":output})

class handleSchedules(threading.Thread):
        def __init__(self,threadID,name):
                threading.Thread.__init__(self)
                self.threadID=threadID
                self.name=name

        def run(self):
                print("starting schdeduler")
                schedule.every(1).minutes.do(job)
                while True:
                        schedule.run_pending()
                        time.sleep(1)

#myscheduler=scheduler(1,"myscheduler")
#myscheduler.start()                                             
