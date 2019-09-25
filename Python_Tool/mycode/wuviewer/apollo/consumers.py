from channels import Group
from subprocess import call,getoutput
from datetime import datetime
import logging
from apollo.cmdhandler import cmdhandler
def ws_message(message):
    mylogger=logging.getLogger("wuviewer")
    #execute command to check the status of the node
    #responsecode=call(["administrator","adminport=2001","display","node"])
    output=cmdhandler.executecmd(["administrator","adminport=2010","display","node"])
    mylogger.info("from websocket connection of Consumer..")
    mylogger.info(output)
    Group("apollo").send({"text":output})

# Connected to websocket.connect
def ws_add(message):
    mylogger=logging.getLogger("wuviewer")
    mylogger.info("New connection added.")
    Group("apollo").add(message.reply_channel)

# Connected to websocket.disconnect
def ws_remove(message):
    Group("apollo").discard(message.reply_channel)

