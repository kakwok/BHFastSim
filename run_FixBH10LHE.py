import glob
import os

#InputDir="../charybdis2/"
#flist = glob.glob("%s/BH10*MBH10*.xml"%InputDir)
#InputDir="/afs/cern.ch/user/b/belotel/work/public/BH/BH6_CH_MD4000_MBH10000_n6/lhouches.xml"
InputDir="/afs/cern.ch/user/b/belotel/work/public/BH"
OutputDir="/afs/cern.ch/user/k/kakwok/work/public/Blackhole/LHE/charybdis/BH9_LHE/"
flist = glob.glob("%s/BH9_CH_MD*_MBH*_n*/lhouches.xml"%InputDir)

for fpath in flist:
	#cmd = "python FixBH10LHE.py %s"%fpath
	cmd = "python FixBH10LHE.py %s %s" % ( fpath, OutputDir+fpath.split("/")[-2]+"_fixed.xml")
	print cmd
	os.system(cmd)
