def getSBkey_BM(fname):
        key={}
        #StringBall_MD1640_MBH9000_MS1100_gs02_n4_1
        if ("EX1" in fname):
                #MD="1640"
                MD="7630"
                MS="1100"
                gs="02"
        if ("EX2" in fname):
                #MD="1490"
                MD="6890"
                MS="1100"
                gs="03"
        if ("EX3" in fname):
                #MD="1890"
                MD="8750"
                MS="1500"
                gs="04"
        if ("EX4" in fname):
                #MD="2380"
                MD="11030"
                MS="2000"
                gs="05"
        #MBH= fname.split("_")[2].replace(".xml","")+"000"
        MBH= fname.split("_")[3].replace(".lhe","").replace("MBH","")
        key['DBkey']="StringBall_MD%s_MBH%s_MS%s_gs%s_n6_blackmax" % (MD,MBH,MS,gs)
        key['MBH'] = MBH
        key['MD'] = MD
        key['MS'] = MS
        key['gs'] = gs
        return key
def getSBkey_CYBD(fname):
	key={}
	#StringBall_MD1640_MBH9000_MS1100_gs02_n4_1
	if ("EX1" in fname):
		#MD="1640"
		MD="5930"
		MS="1100"
		gs="02"
	if ("EX2" in fname):
		#MD="1490"
		MD="5360"
		MS="1100"
		gs="03"
	if ("EX3" in fname):
		#MD="1890"
		MD="6800"
		MS="1500"
		gs="04"
	if ("EX4" in fname):
		#MD="2380"
		MD="8570"
		MS="2000"
		gs="05"
	#MBH= fname.split("_")[2].replace(".xml","")+"000"
	MBH= fname.split("_")[2].replace(".xml","")
	key['DBkey']="StringBall_MD%s_MBH%s_MS%s_gs%s_n6_charybdis" % (MD,MBH,MS,gs)
	key['MBH'] = MBH
	key['MD'] = MD
	key['MS'] = MS
	key['gs'] = gs
	return key

