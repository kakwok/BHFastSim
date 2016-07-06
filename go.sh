#!/bin/bash

#Modify the LHE file input!
#echo "BH1, BH2, or BH5? (type 1,2, or 5)
#read BH
#echo "Enter number of dimensions (2,4,6)"
#read dim

dim=6
BH=6

#for j in $(seq 2 9)  
#for j in $(seq 2 4) 
for j in $(seq 3 7) 
do

#for i in $(seq  9)
for i in $(seq $((j+1)) 9)
#for i in $(seq $((j+1)) 11)

do

echo "from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'Charybdis_BH$((BH))_CH_MD$((j))000_MBH$((i))000_n$((dim))'
config.General.workArea = 'Charybdis_BH$((BH))_CH_MD$((j))000_MBH$((i))000_n$((dim))'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'Charybdis_BH$((BH))_CH_MD$((j))000_MBH$((i))000_n$((dim)).py'
config.JobType.generator = 'lhe'
config.JobType.maxMemoryMB = 2500

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 400
NJOBS = 50
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outputPrimaryDataset = 'Charybdis_BH$((BH))_CH_MD$((j))000_MBH$((i))000_n$((dim))'

config.Data.publication = True
#config.Data.outLFNDirBase = '/store/group/lpctthrun2/UVaSync/FixedBlackMaxAOD/'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())


config.Data.ignoreLocality = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.outputDatasetTag = 'Charybdis_BH$((BH))_CH_MD$((j))000_MBH$((i))000_n$((dim))'

config.section_(\"Site\")
#config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.storageSite = 'T2_CH_CERN'
config.Site.whitelist = ['T2_CH_CERN']" > crabConfig_Charybdis_BH$BH\_CH_MD$j\000_MBH$i\000_n$((dim)).py


echo "# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/Generator/python/Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff.py --filein file:BlackMaxLHArecord.lhe --datamix PreMix --conditions MCRUN2_74_V9 --pileup_input dbs:/Neutrino_E-10_gun/RunIISpring15PrePremix-MCRUN2_74_V9-v1/GEN-SIM-DIGI-RAW --fast -n -1 --eventcontent AODSIM -s GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2,DATAMIX,L1,L1Reco,RECO,HLT:@relval25ns --datatier AODSIM --beamspot NominalCollision2015 --customise SLHCUpgradeSimulations/Configuration/postLS1CustomsPreMixing.customisePostLS1 --magField 38T_PostLS1 --fileout MLM_BlackMax.root
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('FastSimulation.Configuration.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedNominalCollision2015_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('FastSimulation.Configuration.SimIdeal_cff')
process.load('FastSimulation.Configuration.Reconstruction_BefMix_cff')
process.load('FastSimulation.Configuration.DigiDMPreMix_cff')
process.load('SimGeneral.MixingModule.digi_MixPreMix_cfi')
process.load('FastSimulation.Configuration.DataMixerPreMix_cff')
process.load('FastSimulation.Configuration.SimL1Emulator_cff')
process.load('FastSimulation.Configuration.L1Reco_cff')
process.load('FastSimulation.Configuration.Reconstruction_AftMix_cff')
process.load('HLTrigger.Configuration.HLT_25ns14e33_v1_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source(\"LHESource\",
    fileNames = cms.untracked.vstring('file:/afs/cern.ch/user/b/belotel/work/public/BH/BH$((BH))_CH_MD$((j))000_MBH$((i))000_n$((dim))/lhouches.xml') 
#   fileNames = cms.untracked.vstring('root://eoscms.cern.ch//eos/cms/store/group/phys_exotica/BH_RunII/BlackMax_n2/BH$((BH))_CH_MD$((j))000_MBH$((i))000_n$((dim))/BlackMaxLHArecord.lhe')
#   fileNames = cms.untracked.vstring('file:/eos/uscms/store/user/zcarson/BH$((BH))_CH_MD$((j))000_MBH$((i))000_n$((dim))/BlackMaxLHArecord.lhe')
#   fileNames = cms.untracked.vstring('file:/afs/cern.ch/user/b/belotel/work/public/BH/BH$((BH))_CH_MD$((j))000_MBH$((i))000_n$((dim))/BlackMaxLHArecord.lhe')
#   fileNames = cms.untracked.vstring('/store/group/phys_exotica/QBH_LHE_John/MD_4_MQBH_4_n_1/LHEFfile.lhe')
#   fileNames = cms.untracked.vstring('root://eoscms.cern.ch//eos/cms/store/user/tutanon/BH2015/LHE/BlackMaxLHArecord_BH1_CH_MD2000_MBH10000_n6.lhe') 
#   fileNames = cms.untracked.vstring('root://eoscms.cern.ch//eos/cms/store/user/tutanon/BH2015/LHE/BlackMaxLHArecord_BH1_CH_MD3000_MBH7000_n6.lhe') 
#   fileNames = cms.untracked.vstring('root://eoscms.cern.ch//eos/cms/store/group/phys_exotica/QBH_LHE_John/MD_4_MQBH_4_n_1/LHEFfile.lhe')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/Generator/python/Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff.py nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODSIMoutput = cms.OutputModule(\"PoolOutputModule\",
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
    #fileName = cms.untracked.string('BH1_CH_MD4000_MBH5000_n2.root'),
    #fileName = cms.untracked.string('BH1_CH_MD4000_MBH5000_n4.root'),
    #fileName = cms.untracked.string('BH1_CH_MD4000_MBH5000_n6.root'),
    #fileName = cms.untracked.string('BH1_CH_MD6000_MBH7000_n2.root'),
    #fileName = cms.untracked.string('BH1_BM_MD6000_MBH7000_n4.root'),
    #fileName = cms.untracked.string('BH1_BM_MD6000_MBH7000_n6.root'),
    #fileName = cms.untracked.string('BH1_BM_MD8000_MBH9000_n2.root'),
    #fileName = cms.untracked.string('BH1_BM_MD8000_MBH9000_n4.root'),
    #fileName = cms.untracked.string('BH1_BM_MD8000_MBH9000_n6.root'),
    #fileName = cms.untracked.string('QBH_MD_6_MQBH_7_n_2.root'),
    fileName = cms.untracked.string('Charybdis_BH$((BH))_CH_MD$((j))000_MBH$((i))000_n$((dim)).root'),
    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring(\"generation_step\")
process.mix.digitizers = cms.PSet(process.theDigitizersMixPreMix)
#process.mixData.input.fileNames = cms.untracked.vstring(['/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/0021F46D-ED25-E511-9376-0025905B8576.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/0040E519-2226-E511-A1C9-002618FDA277.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00458809-B226-E511-952B-002354EF3BE0.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00946A66-4726-E511-BA1E-0025905A60F2.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/009FA86E-5F26-E511-A542-003048FFD732.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00AE3880-B826-E511-9B01-00261894394F.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00AF43F2-2B26-E511-BC56-0025905A6088.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00B5E935-3C26-E511-A7DF-0025905B85D6.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00CC8235-3C26-E511-8D60-0025905A60F4.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00D70232-4126-E511-B79A-0025905938A4.root'])
process.mixData.input.fileNames = cms.untracked.vstring(['/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/40001/0A977B86-9026-E511-8B64-0025905AA9CC.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/40001/0C815C87-AE26-E511-BEB5-0025905A48C0.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/40001/144FF8B9-8726-E511-AF47-0025905938D4.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/40001/149937C9-8526-E511-A6B7-0025905B85EE.root','/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/40001/1EB85210-8726-E511-A139-0025905A607E.root','/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/40001/1EB85210-8726-E511-A139-0025905A607E.root','/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/40001/28B6D74F-9226-E511-9B3E-0025905964C4.root','/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/40001/2AF81D4F-A926-E511-BAFF-0025905A48FC.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/40001/34DBF3EB-A326-E511-80F1-0025905A60B2.root','/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/40001/36B97117-9326-E511-A9D3-002354EF3BDB.root'])
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')

process.generator = cms.EDFilter(\"Pythia8HadronizerFilter\",
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
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.reconstruction_befmix_step = cms.Path(process.reconstruction_befmix)
process.digitisation_step = cms.Path(process.pdigi)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.reconstruction_befmix_step,process.digitisation_step,process.datamixing_step,process.L1simulation_step,process.L1Reco_step,process.reconstruction_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.AODSIMoutput_step])
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from FastSimulation.Configuration.MixingModule_Full2Fast
from FastSimulation.Configuration.MixingModule_Full2Fast import prepareDigiRecoMixing 

#call to customisation function prepareDigiRecoMixing imported from FastSimulation.Configuration.MixingModule_Full2Fast
process = prepareDigiRecoMixing(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1CustomsPreMixing
from SLHCUpgradeSimulations.Configuration.postLS1CustomsPreMixing import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1CustomsPreMixing
process = customisePostLS1(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFastSim 

#call to customisation function customizeHLTforFastSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFastSim(process)

# End of customisation functions" > Charybdis_BH$BH\_CH_MD$j\000_MBH$i\000_n$((dim)).py

crab submit -c crabConfig_Charybdis_BH$BH\_CH_MD$j\000_MBH$i\000_n$((dim)).py

done

done

ls
