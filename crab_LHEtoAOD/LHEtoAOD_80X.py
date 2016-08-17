# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options:
#Configuration/GenProduction/python/JME-RunIISpring16FSPremix-00002-fragment.py 
#--fileout file:JME-RunIISpring16FSPremix-00002.root 
#--pileup_input dbs:/Neutrino_E-10_gun/RunIISpring16FSPremix-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/GEN-SIM-DIGI-RAW 
#--mc 
#--eventcontent AODSIM 
#--fast 
#--customise SimGeneral/DataMixingModule/customiseForPremixingInput.customiseForPreMixingInput 
#--datatier AODSIM 
#--conditions 80X_mcRun2_asymptotic_v12 
#--beamspot Realistic50ns13TeVCollision 
#--customise_commands process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200) 
#--step GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,L1Reco,RECO,HLT:@fake1 
#--datamix PreMix 
#--era Run2_25ns 
#--filein file:BH10_fixed.xml
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
from sys import argv

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_25ns,eras.fastSim)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeV2016Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('FastSimulation.Configuration.SimIdeal_cff')
process.load('FastSimulation.Configuration.Reconstruction_BefMix_cff')
process.load('Configuration.StandardSequences.DigiDMPreMix_cff')
process.load('SimGeneral.MixingModule.digi_MixPreMix_cfi')
process.load('Configuration.StandardSequences.DataMixerPreMix_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorDM_cff')
process.load('Configuration.StandardSequences.DigiToRawDM_cff')
process.load('FastSimulation.Configuration.L1Reco_cff')
process.load('FastSimulation.Configuration.Reconstruction_AftMix_cff')
process.load('HLTrigger.Configuration.HLT_Fake1_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

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

#PathAndName     = "./BH10_LHE/BH10_MD2_MBH6_n6_fixed.xml"
#InputFile       = "file:"+PathAndName
InputFile       = "file:"+options.InputFile
flist           = options.InputFile.split("/")
fname           = flist[len(flist)-1]

#------------------------------------------------------------------------------------

OutputFile = fname.replace(".xml","")+"_AOD.root"

print "Input LHE =", InputFile
print "Onput AOD =", OutputFile

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("LHESource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring(InputFile),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop LHEXMLStringProduct_*_*_*'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/JME-RunIISpring16FSPremix-00002-fragment.py nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AODSIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
#    fileName = cms.untracked.string('file:JME-RunIISpring16FSPremix-00002.root'),
    fileName = cms.untracked.string(OutputFile),
    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersMixPreMix)
process.mixData.input.fileNames = cms.untracked.vstring(
[
'root://eoscms.cern.ch//store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/007F9F8A-EB14-E611-9918-00259075D72C.root', 
'root://eoscms.cern.ch//store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/00A7A158-4E14-E611-A2E5-0025905B858E.root', 
'root://eoscms.cern.ch//store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/00B28D0D-A214-E611-A9FA-0025904C4E28.root', 
'root://eoscms.cern.ch//store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/00C7136F-8714-E611-9DD4-0025905B8564.root', 
'root://eoscms.cern.ch//store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/00ECAC4F-5714-E611-ACAC-0CC47A4D76D0.root', 
'root://eoscms.cern.ch//store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/02053F47-7B14-E611-904C-0025905C53D0.root', 
'root://eoscms.cern.ch//store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/020ACED3-8C14-E611-9F4D-0025905B85DC.root', 
'root://eoscms.cern.ch//store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0259F967-6915-E611-8908-00304867FE4B.root', 
'root://eoscms.cern.ch//store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/02600760-4E14-E611-B7D9-0025905B8592.root',
'root://eoscms.cern.ch//store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/027EC271-7714-E611-971C-0025905C5502.root'])
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 
#	'80X_mcRun2_asymptotic_v12',
	'80X_mcRun2_asymptotic_RealisticBS_25ns_13TeV2016_v1_mc',
	 '')
process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CUEP8M1Settings'),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'),
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
	    'Next:numberShowLHA = 10',
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on')
    ),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(10),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step 		= cms.Path(process.pgen)
process.simulation_step 		= cms.Path(process.psim)
process.reconstruction_befmix_step 	= cms.Path(process.reconstruction_befmix)
process.digitisation_step		= cms.Path(process.pdigi)
process.datamixing_step 		= cms.Path(process.pdatamix)
process.L1simulation_step 		= cms.Path(process.SimL1Emulator)
process.digi2raw_step 			= cms.Path(process.DigiToRaw)
process.L1Reco_step 			= cms.Path(process.L1Reco)
process.reconstruction_step		= cms.Path(process.reconstruction)
process.genfiltersummary_step 		= cms.EndPath(process.genFilterSummary)
process.endjob_step			= cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step 		= cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(
	process.generation_step,
	process.genfiltersummary_step,
	process.simulation_step,
	process.reconstruction_befmix_step,
	process.digitisation_step,
	process.datamixing_step,
	process.L1simulation_step,
	process.digi2raw_step,
	process.L1Reco_step,
	process.reconstruction_step
)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.AODSIMoutput_step])

# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 


# customisation of the process.

# Automatic addition of the customisation function from SimGeneral.DataMixingModule.customiseForPremixingInput
from SimGeneral.DataMixingModule.customiseForPremixingInput import customiseForPreMixingInput 

#call to customisation function customiseForPreMixingInput imported from SimGeneral.DataMixingModule.customiseForPremixingInput
process = customiseForPreMixingInput(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFastSim 

#call to customisation function customizeHLTforFastSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFastSim(process)

# End of customisation functions

# Customisation from command line
#process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)

# Customisation from command line
#process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)
