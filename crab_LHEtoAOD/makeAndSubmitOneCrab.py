from sys import argv
from os import path, makedirs, system
import subprocess

# This script will run:
# cmsRun pSetName argv[1]

# Input should be the location of LHE
# LHEpath = /afs/cern.ch/user/k/kakwok/work/public/Blackhole/CMSSW_8_0_14/src/BH/BHFastSim/BH10_LHE/BH10_MD5_MBH7_n6_fixed.xml
LHEpath    = argv[1]
print "Going to use LHE:" + LHEpath
fname       = LHEpath.split("/")[len(LHEpath.split("/"))-1]
modelnumber = fname.split("_")[0]
MD          = fname.split("_")[1].replace("MD","")
MBH         = fname.split("_")[2].replace("MBH","")
nDim        = fname.split("_")[3]


SampleName ="Charybdis_%s_CH_MD%s000_MBH%s000_%s" % (modelnumber, MD, MBH, nDim)
pSetName   ="LHEtoAOD_80X.py"
print "The SampleName is " + SampleName

#####################################################################
# Print the static lines from template, make the script for submission
if not path.exists("CrabConfigs"):
  makedirs("CrabConfigs")

crabConfigFileName="CrabConfigs/CrabConfig_%s.py"%SampleName
tempCrabConfig = open(crabConfigFileName, "w")

template = open("template_LHEtoAOD.py", "r")
for line in template:
  tempCrabConfig.write(line)
template.close()
#####################################################################

tempCrabConfig.write("config.General.requestName = 'crab_job_%s'\n"%SampleName)
tempCrabConfig.write("config.General.workArea    = 'crab_job_%s'\n"%SampleName)
tempCrabConfig.write("config.JobType.psetName 	 = '%s'\n"%pSetName)
tempCrabConfig.write("config.JobType.pyCfgParams = ['InputFile=%s']\n"%fname)
tempCrabConfig.write("config.JobType.inputFiles  = ['%s']\n"%LHEpath)
tempCrabConfig.write("config.Data.outputDatasetTag     = '%s'\n"%SampleName)
tempCrabConfig.write("config.Data.outputPrimaryDataset = '%s'\n"%SampleName)
tempCrabConfig.close()

cmd ="crab submit %s"%crabConfigFileName
print cmd
system(cmd)
#subprocess.Popen(["crab", "submit", crabConfigFileName])
