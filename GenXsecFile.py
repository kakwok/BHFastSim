from sys import argv
import os
import glob

Topdir="./BH10_LHE"
fname ="Charybdis_BH10_xsection.txt"
file_list= glob.glob("%s/*.xml"%Topdir)
Xsec = open(fname,"w")

#lhe = BH10_MD2_MBH7_n6_fixed.xml
#Output format = BlackHole_BH10_MD2000_MBH11000_n4
for fpath in file_list:
	fname = fpath.split("/")[len(fpath.split("/"))-1]
	BH   = fname.split("_")[0]
	MD   = fname.split("_")[1]
	MBH  = fname.split("_")[2]
	n    = fname.split("_")[3]	
	key = "Charybdis_"+BH+"_"+MD+"000_"+MBH+"000_"+n
	#print key
	FoundInit = False
	LHE = open("%s/%s"%(Topdir,fname))
	#look for the 2nd line in the init 
	for line in LHE:
		line = line.strip().split()
		if(len(line)>0):
			if("init" in line[0]):
				FoundInit = True
			if(FoundInit and len(line)==4):
				print "%s     %s" % (key, line[0])
				Xsec.write("%s     %s\n"%(key,line[0]))
				break
Xsec.close()	
