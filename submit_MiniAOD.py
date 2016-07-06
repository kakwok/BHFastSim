import os

file = open("dasoutput.txt","r")

for line in file:
	line = line.strip()
	key  = line.split("/")[1]
	cmd="crab submit crabConfig_AODtoMiniAOD.py Data.inputDataset=%s Data.outputDatasetTag=%s"%(line,key)
	print cmd
	os.system(cmd)
