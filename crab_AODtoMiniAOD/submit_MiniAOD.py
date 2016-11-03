import os

#file = open("dasoutput.txt","r")
#file = open("dasoutput_n6.txt","r")
#file = open("SBAOD.txt","r")
#file = open("charybdis_tosubmit.txt","r")
file = open("BH6_MD2000_fixed.txt","r")

for line in file:
	if(not(line[0]=="#")):
		line = line.strip()
		#key  = line.split("/")[1]+"_MINIAOD"
		key  = line.split("/")[1].replace("AOD","MINIAOD")
		requestName = "miniAOD_"+key
		cmd="crab submit crabConfig_AODtoMiniAOD.py General.requestName=%s Data.inputDataset=%s Data.outputDatasetTag=%s"%(requestName,line,key)
		print cmd
		os.system(cmd)
