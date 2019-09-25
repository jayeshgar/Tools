from django.shortcuts import render
from subprocess import call,getoutput
from django.http import HttpResponse
from django.template import loader
from apollo.scheduler import handleSchedules
from django.views import generic
import logging
from apollo.cmdhandler import cmdhandler
#logger=logging.getLogger(__name__)
# Create your views here.
def index(request):
	#output=cmdhandler.executecmd(["administrator","adminport=2010","display", "node"])
	logger=logging.getLogger("wuviewer")
	#logger.info(output)
	template=loader.get_template('apollo/general/General.html')
	context={

        # 'cmdresult' : output,
	}

	#Startup code to start the scheduler
	logger.info("Setting scheduler")
	myscheduler=handleSchedules(1,"myscheduler")
	myscheduler.start()

	return HttpResponse(template.render(context,request))
