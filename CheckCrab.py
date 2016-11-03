import glob
import os

#~/eos/cms/store/user/kakwok/BH/AOD/StringBall_MD8750_MBH5000_MS1500_gs04_n6_blackmax_AOD/StringBall_MD8750_MBH5000_MS1500_gs04_n6_blackmax_AOD/161004_094650/0000/
TopDir ="/afs/cern.ch/user/k/kakwok/eos/cms/store/user/kakwok/BH/AOD"
#TopDir ="/afs/cern.ch/user/k/kakwok/eos/cms/store/user/kakwok/MiniAOD"

folderlist = glob.glob("%s/*StringBall*charybdis*"%TopDir)
#print folderlist
for folder in folderlist:
	flist  = glob.glob("%s/*/*/*/*.root"%(folder))
	Sample = folder.split("/")[-1]
	if len(flist)==10:
		print "%s  %s   completed!"%(Sample,len(flist))
	else:
		print "%s  %s"%(Sample,len(flist))
	
