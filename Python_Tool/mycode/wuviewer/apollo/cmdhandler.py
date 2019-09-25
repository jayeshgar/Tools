import io
import subprocess
import json

class cmdhandler:
	def executecmd(cmdlist):
		proc=subprocess.Popen(cmdlist,stdout=subprocess.PIPE,universal_newlines=True)
		output="{"
		for line in proc.stdout:
        		if ":" in str(line):
                		linelist=line.split(':')
                		output=output+"\""+linelist[0].strip()+"\":\""+linelist[1].strip()+"\","
        		else:
                		continue

		output=output[:-1]+"}"
		return json.dumps(output)
