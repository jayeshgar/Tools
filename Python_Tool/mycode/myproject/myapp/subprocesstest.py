import io
import subprocess
import json

proc=subprocess.Popen(["administrator","adminport=2010","display","node"],stdout=subprocess.PIPE,universal_newlines=True)
#outs=proc.communicate(timeout=15)
#print(len(outs))

output="{"
for line in proc.stdout:
	if ":" in str(line):
		linelist=line.split(':')
		output=output+"\""+linelist[0].strip()+"\":\""+linelist[1].strip()+"\","
	else:
		continue
	
output=output[:-1]+"}"
parsed_json=json.loads(output)
print(output)
