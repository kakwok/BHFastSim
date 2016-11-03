# This script screens the files in input list that are un-finished


Alldataset = open("SBAOD_charybdis.txt","r")
completed  = open("charybdis_completed.txt","r")
submitted  = open("charybdis_submitted.txt","r+")
Tosubmit   = open("charybdis_tosubmit.txt","w")

submitted_list=[]
for SampleName in submitted:
	SampleName = SampleName.strip()
	submitted_list.append(SampleName)
print "These samples have been submitted:",submitted_list
print "Going to generate submit file"
for line in Alldataset:
	dataset = line.strip()
	for line in completed:
		SampleName = line.strip().split()[0]
		if SampleName in dataset:
			if SampleName in submitted_list:
				print "%s has already been submitted. skipping" % SampleName 
			else:
				print "%s is completed but not submitted! Adding to submit list" % SampleName
				submitted.write("%s\n"%SampleName)
				Tosubmit.write("%s\n"%dataset)
	completed.seek(0)
print "Please submit %s " % Tosubmit.name
