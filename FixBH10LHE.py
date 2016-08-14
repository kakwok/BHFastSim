import math
from sys import argv

def ReplacePid(pid):
	if pid=="50":
		return "1000022"
	if pid=="-51":
		return "1000015"
	if pid=="51":
		return "-1000015"
	print "Cannot find correct replacement, check the code!"
	return pid
def get4vector(line):
	FourVector = []
	FourVector.append(line[6])
	FourVector.append(line[7])
	FourVector.append(line[8])
	FourVector.append(line[9])
	return FourVector

def getNparticleLine(line):
	tmp = ""
	line = line.strip().split()
	line[0] = str(int(line[0])-1)
	for data in line:
		tmp += data + "     "
	tmp += "\n"
	return tmp
def getGravitonLine(line,p1p2):
	pSum = []
	tmp  = ""
	i    = 0
	if(len(p1p2)==2):
		#print p1p2
		p1 = p1p2[0]
		p2 = p1p2[1]
		pSum.insert(0,  float(p1[0]) + float(p2[0]))
		pSum.insert(1,  float(p1[1]) + float(p2[1]))
		pSum.insert(2,  float(p1[2]) + float(p2[2]))
		pSum.insert(3,  float(p1[3]) + float(p2[3]))
		mass = math.sqrt(pSum[3]*pSum[3]-pSum[0]*pSum[0]-pSum[1]*pSum[1]-pSum[2]*pSum[2])
		line[6]  =str( pSum[0])
		line[7]  =str( pSum[1])
		line[8]  =str( pSum[2])
		line[9]  =str( pSum[3])
		line[10] =str( mass   )
		for data in line:
			tmp += data + "    "
		tmp += "\n"
		return tmp
	else:
		print "did not get 2 graviton's 4vector"
		return tmp
		
StartReplace = False

nEvent     = 0
n39        = 0
nWarn      = 0
eventLines = []
gravitonline  = []
nParticleLine = ""
p1p2       = []

file = open(argv[1],"r")

ListOfInput = argv[1].split("/")
fname = ListOfInput[len(ListOfInput)-1].replace(".xml","_fixed.xml")
FixedLHE = open(fname,"w")

print "Going to replace pids in the following LHE: %s"%argv[1]
for line in file:
	if StartReplace:
		splitLine = line.strip().split()
		if(len(splitLine)>1):
			#Handle number of events
			if(len(splitLine)==6):
				nParticleLine = line
			#Handle replacement
			else:
				line = line.strip().split()
				replacedline =""
				if(line[0]=="50" or line[0]=="-51" or line[0]=="51"):
					line[0]=ReplacePid(line[0])
				if(line[0]=="39"):
					n39 +=1
					line[12]="9."
					p1p2.append(get4vector(line))
				if(n39==1):
					#keep first graviton's info except 4 momentum and mass
					gravitonline = line
				#Skip adding to buffer if it's a graviton line
				if(not(line[0]=="39")):
					for data in line:
						replacedline +=data +"     "
					replacedline+="\n"
					eventLines.append(replacedline)
		# Event header
		if(len(splitLine)==1):
			# if event buffers is empty, this is a new event
			if(len(eventLines)==0):
				eventLines.append(line)
			# if event buffers is not empty, wrtie the lines
			else:
				if(n39<2):
					n39=0				#reset ngraviton
					print "warning! found only 1 gravitons in an event!"
				elif(n39==2):
					# Found 2 gravitons, print an nParticleline with 1 less particle
					tmpline = getNparticleLine(nParticleLine)
					eventLines.insert(1,tmpline)
					# Append graviton line
					tmpline = getGravitonLine(gravitonline,p1p2)
					eventLines.append(tmpline)
					eventLines.append(line)			#append </event>
					for bufferlines in eventLines:
						FixedLHE.write(bufferlines)
						#print bufferlines
					eventLines = []				#reset buffer
					p1p2       = []				#reset buffer
					nParticleLine = ""			#reset buffer
					n39=0
				else:
					nWarn +=1
					print "warning! found more than 2 gravitons in an event!"
	else:
		if "event" in line:
			StartReplace=True
			eventLines.append(line)
		else:
			FixedLHE.write(line)
print "Found "+ str(nWarn)+" events with more then 2 gravitons"
print "Finished! Check the fixed LHE: %s"%fname
