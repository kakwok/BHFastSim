from os import system 
import subprocess

inputlist=open("LHElist.txt","r")

for line in inputlist:
  if(not line[0]=="#"):
	cmd = "python makeAndSubmitOneCrab.py %s"%line
	print cmd
	system(cmd)
	#subprocess.Popen(["python", "makeAndSubmitOneCrab.py", line]) 
