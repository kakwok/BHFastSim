from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

# To be set from make script

#config.General.requestName = 'Charybdis_BH$((BH))_CH_MD$((j))000_MBH$((i))000_n$((dim))'
#config.General.workArea = 'Charybdis_BH$((BH))_CH_MD$((j))000_MBH$((i))000_n$((dim))'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName  = 'PrivateMC'
#config.JobType.psetName   = 'Charybdis_BH$((BH))_CH_MD$((j))000_MBH$((i))000_n$((dim)).py'
#config.JobType.pyCfgParams =
config.JobType.generator   = 'lhe'
config.JobType.maxMemoryMB = 2500

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
config.Data.totalUnits  = 10000
#config.Data.outputPrimaryDataset = 'Charybdis_BH$((BH))_CH_MD$((j))000_MBH$((i))000_n$((dim))'
#config.Data.outputDatasetTag = 'Charybdis_BH$((BH))_CH_MD$((j))000_MBH$((i))000_n$((dim))'

config.Data.publication = True
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.ignoreLocality = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'

#config.section_("Site")
#config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.whitelist   = ['T2_CH_CERN']
