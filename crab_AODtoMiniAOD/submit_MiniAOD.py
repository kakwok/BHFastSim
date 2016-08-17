import os

file = open("dasoutput.txt","r")

for line in file:
	if(not(line[0]=="#")):
		line = line.strip()
		key  = line.split("/")[1]
		requestName = "miniAOD_"+key
		cmd="crab submit crabConfig_AODtoMiniAOD.py General.requestName=%s Data.inputDataset=%s Data.outputDatasetTag=%s"%(requestName,line,key)
		print cmd
		os.system(cmd)
