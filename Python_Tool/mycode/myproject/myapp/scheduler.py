import threading
import schedule
import time

def job():
	print("I am working...")

class scheduler(threading.Thread):
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

myscheduler=scheduler(1,"myscheduler")
myscheduler.start()                                             
