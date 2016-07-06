# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions MCRUN2_74_V9 --fast -n 10 --eventcontent MINIAODSIM --runUnscheduled --filein file:fastsim.root -s PAT --datatier MINIAODSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --mc
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process('PAT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('FastSimulation.Configuration.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.MessageLogger = cms.Service("MessageLogger",
                            destinations   = cms.untracked.vstring('messages')
)
#------------------------------------------------------------------------------------
# Options
#------------------------------------------------------------------------------------

options = VarParsing.VarParsing()
options.register('InputFile',
		"file:input.lhe",
		VarParsing.VarParsing.multiplicity.singleton,
		VarParsing.VarParsing.varType.string,
		"filename of LHE")


options.parseArguments()

#fname = options.InputFile.split("/")
#OutputFile = fname[len(fname)-2]+"_miniAOD.root"

fname  = options.InputFile
OutputFile = fname.replace("_AOD.root","_miniAOD.root")
print "Input AOD =", options.InputFile
print "Onput MiniAOD =", OutputFile

#------------------------------------------------------------------------------------


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
#process.maxLuminosityBlocks = cms.untracked.PSet(
#    input = cms.untracked.int32(-1)
#)
# Input source
process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring('file:BlackMaxLHArecord_BH1_BM_MD4000_MBH5000_n2.root'),
#    fileNames = cms.untracked.vstring('file:/afs/cern.ch/work/t/tutanon/BH2015/CMSSW_7_4_4/src/SignalGeneration/FixedBlackMaxAOD/BlackMaxLHArecord_BH1_BM_MD4000_MBH5000_n2.root'),
#    fileNames = cms.untracked.vstring('/afs/cern.ch/user/k/kakwok/eos/cms/store/user/kakwok/CRAB_PrivateMC/crab_BHFastSim_LHEtoAOD_BH6_CH_MD3000_MBH6000_n2/160701_162952/0000/*.root')
#    fileNames = cms.untracked.vstring('root://eoscms//eos/cms/store/user/kakwok/CRAB_PrivateMC/crab_BHFastSim_LHEtoAOD_BH6_CH_MD3000_MBH6000_n2/160701_162952/0000/*.root')

    processingMode =cms.untracked.string("RunsLumisAndEvents"),
     fileNames = cms.untracked.vstring(
	 options.InputFile
    ),
    setRunNumber = cms.untracked.uint32(1),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string(': 1.19 $')
)

# Output definition

process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('BH6_CH_MD3000_MBH6000_n2_MiniAOD.root'),
#    fileName = cms.untracked.string(OutputFile),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.endjob_step,process.MINIAODSIMoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from FastSimulation.Configuration.MixingModule_Full2Fast
from FastSimulation.Configuration.MixingModule_Full2Fast import prepareDigiRecoMixing 

#call to customisation function prepareDigiRecoMixing imported from FastSimulation.Configuration.MixingModule_Full2Fast
process = prepareDigiRecoMixing(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
process.load('Configuration.StandardSequences.PATMC_cff')

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC 

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.metFilterPaths_cff
from PhysicsTools.PatAlgos.slimming.metFilterPaths_cff import miniAOD_customizeMETFiltersFastSim 

#call to customisation function miniAOD_customizeMETFiltersFastSim imported from PhysicsTools.PatAlgos.slimming.metFilterPaths_cff
process = miniAOD_customizeMETFiltersFastSim(process)

# End of customisation functions
