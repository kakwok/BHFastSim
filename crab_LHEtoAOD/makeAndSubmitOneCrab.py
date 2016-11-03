from sys import argv
from os import path, makedirs, system
from GetSB import *
import subprocess

# This script will run:
# cmsRun pSetName argv[1]

# Input should be the location of LHE
# LHEpath = /afs/cern.ch/user/k/kakwok/work/public/Blackhole/CMSSW_8_0_14/src/BH/BHFastSim/BH10_LHE/BH10_MD5_MBH7_n6_fixed.xml
# LHEpath = /afs/cern.ch/user/k/kakwok/work/public/Blackhole/LHE/charybdis/BH6_LHE/BH6_CH_MD2000_MBH9000_n6_fixed.xml
# LHEpath = /afs/cern.ch/user/k/kakwok/work/public/Blackhole/LHE/SB_LHE
LHEpath    = argv[1]
print "Going to use LHE:" + LHEpath
fname       = LHEpath.split("/")[-1]
#SBkey       = getSBkey_CYBD(fname)
#SBkey       = getSBkey_BM(fname)
modelnumber = fname.split("_")[0]
MD          = fname.split("_")[1].replace("MD","")
MBH         = fname.split("_")[2].replace("MBH","")
nDim        = fname.split("_")[3]

SampleName ="Charybdis_%s_CH_MD%s_MBH%s_%s" % (modelnumber, MD, MBH, nDim)
#SampleName ="Charybdis_%s_CH_MD%s000_MBH%s000_%s" % (modelnumber, MD, MBH, nDim)
#SampleName =SBkey["DBkey"]
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
tempCrabConfig.write("config.Data.outputDatasetTag     = '%s_AOD'\n"%SampleName)
tempCrabConfig.write("config.Data.outputPrimaryDataset = '%s_AOD'\n"%SampleName)
tempCrabConfig.close()

cmd ="crab submit %s"%crabConfigFileName
print cmd
#system(cmd)
#subprocess.Popen(["crab", "submit", crabConfigFileName])
