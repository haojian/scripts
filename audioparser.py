import scipy
import time

def parseHeader(line):
	parts = line.strip().split("\t")
	return {'time_sec':long(parts[1]), 'time_mill':int(parts[2]), "frame": long(parts[3]) }
	
	
def convertToMatlabCSV(input, output):
	with open(output, "w") as out:
		out.write("")
	with open(output, "a") as out:
		with open(input) as f:
			for line in f:
				if not line.strip().startswith('#'):
					out.write(line.strip())

			
headers = []
with open("audiorecording.txt") as f:
	for line in f:
		if line.strip().startswith('#'):
			headers.append(line.strip())
			# pass
			print line
	res1 =  parseHeader(headers[0]) 
	res2 =  parseHeader(headers[-1])
	print "sampling rate: ", (res2['frame']-res1['frame'])/( (res2['time_sec']-res1['time_sec']) + (res2['time_mill'] - res1['time_mill']) / 1000)
	
convertToMatlabCSV("audiorecording.txt", "/Users/haojian/Documents/MATLAB/signalprocessing/matlabfile.txt")

millis = int(round(time.time() * 1000))
print millis