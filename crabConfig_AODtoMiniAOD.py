from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from sys import argv
config = config()

# usage: crab submit crabConfig_AODtoMiniAOD.py argv[3] argv[4]
# argv[3] = Charybdis_BH6_CH_MD2000_MBH6000_n6
# argv[4] = /Charybdis_BH6_CH_MD2000_MBH6000_n6/kakwok-Charybdis_BH6_CH_MD2000_MBH6000_n6-43efd47f54c11c6efdc1cb52f92c16e7/USER

#config.General.requestName = argv[3]
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'AODtoMiniAOD.py'

config.Data.inputDBS = 'phys03'
#config.Data.inputDataset = argv[4]
#config.Data.outputDatasetTag = argv[3]
#config.Data.inputDataset = '/Charybdis_BH6_CH_MD2000_MBH6000_n6/kakwok-Charybdis_BH6_CH_MD2000_MBH6000_n6-43efd47f54c11c6efdc1cb52f92c16e7/USER'
#config.Data.outputDatasetTag = 'Charybdis_BH6_CH_MD2000_MBH6000_n6_V2'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 100
config.Data.outLFNDirBase = '/store/user/%s/MiniAOD/' % (getUsernameFromSiteDB())
#config.Data.outLFNDirBase = '/mnt/hadoop/users/mkwok/MiniAOD/' 
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'

config.Site.storageSite = 'T3_US_Brown'
#config.Site.storageSite = 'T2_CH_CERN'
