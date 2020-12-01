import json
import time

smart = False
rStage = 0
lStage = 0
recvData = ''
rSetPrio = [0,0,0,0,0,0,0]
lSetPrio = [0,0,0,0,0,0,0]
data = {
	"A1-1": 0,
	"A1-2": 0,
	"A1-3": 0,
	"B1-1": 0,
	"B1-2": 0,
	"F1-1": 0,
	"F1-2": 0,
	"V1-1": 0,
	"V1-2": 0,
	"V1-3": 0,
	"V1-4": 0,
	"A2-1": 0,
	"A2-2": 0,
	"A2-3": 0,
	"A2-4": 0,
	"F2-1": 0,
	"F2-2": 0,
	"V2-1": 0,
	"V2-2": 0,
	"V2-3": 0,
	"V2-4": 0,
	"A3-1": 0,
	"A3-2": 0,
	"A3-3": 0,
	"A3-4": 0,
	"A4-1": 0,
	"A4-2": 0,
	"A4-3": 0,
	"A4-4": 0,
	"B4-1": 0,
	"F4-1": 0,
	"F4-2": 0,
	"V4-1": 0,
	"V4-2": 0,
	"V4-3": 0,
	"V4-4": 0,
	"A5-1": 0,
	"A5-2": 0,
	"A5-3": 0,
	"A5-4": 0,
	"F5-1": 0,
	"F5-2": 0,
	"V5-1": 0,
	"V5-2": 0,
	"V5-3": 0,
	"V5-4": 0,
	"A6-1": 0,
	"A6-2": 0,
	"A6-3": 0,
	"A6-4": 0
}

def updateLightR(nr):
    #Set light to Red
	if nr == 1:
		data["A1-1"] = 0
		data["A1-2"] = 0
		data["A1-3"] = 0
		data["B1-1"] = 0
		data["B1-2"] = 0
		data["F1-1"] = 0
		data["F1-2"] = 0
		data["V1-1"] = 0
		data["V1-2"] = 0
		data["V1-3"] = 0
		data["V1-4"] = 0
		data["A2-1"] = 0
		data["A2-2"] = 0
		data["A2-3"] = 0
		data["A2-4"] = 0
		data["F2-1"] = 0
		data["F2-2"] = 0
		data["V2-1"] = 0
		data["V2-2"] = 0
		data["V2-3"] = 0
		data["V2-4"] = 0
		data["A3-1"] = 0
		data["A3-2"] = 0
		data["A3-3"] = 0
		data["A3-4"] = 0

#Right-purple
	elif nr == 2:		
		data["A1-1"] = 1
		data["A1-2"] = 1
		data["A1-3"] = 0
		data["B1-1"] = 0
		data["B1-2"] = 0
		data["F1-1"] = 0
		data["F1-2"] = 0
		data["V1-1"] = 0
		data["V1-2"] = 0
		data["V1-3"] = 0
		data["V1-4"] = 0
		data["A2-1"] = 0
		data["A2-2"] = 0
		data["A2-3"] = 0
		data["A2-4"] = 0
		data["F2-1"] = 1
		data["F2-2"] = 1
		data["V2-1"] = 0
		data["V2-2"] = 0
		data["V2-3"] = 0
		data["V2-4"] = 0
		data["A3-1"] = 1
		data["A3-2"] = 1
		data["A3-3"] = 0
		data["A3-4"] = 0

#Right-Red
	elif nr == 4:
		data["A1-1"] = 0
		data["A1-2"] = 0
		data["A1-3"] = 0
		data["B1-1"] = 0
		data["B1-2"] = 0
		data["F1-1"] = 0
		data["F1-2"] = 0
		data["V1-1"] = 0
		data["V1-2"] = 0
		data["V1-3"] = 0
		data["V1-4"] = 0
		data["A2-1"] = 0
		data["A2-2"] = 0
		data["A2-3"] = 0
		data["A2-4"] = 0
		data["F2-1"] = 0
		data["F2-2"] = 0
		data["V2-1"] = 1
		data["V2-2"] = 1
		data["V2-3"] = 0
		data["V2-4"] = 0
		data["A3-1"] = 1
		data["A3-2"] = 1
		data["A3-3"] = 1
		data["A3-4"] = 1

#Right-Green
	elif nr == 6:		
		data["A1-1"] = 0
		data["A1-2"] = 0
		data["A1-3"] = 0
		data["B1-1"] = 0
		data["B1-2"] = 0
		data["F1-1"] = 0
		data["F1-2"] = 0
		data["V1-1"] = 0
		data["V1-2"] = 0
		data["V1-3"] = 0
		data["V1-4"] = 0
		data["A2-1"] = 1
		data["A2-2"] = 1
		data["A2-3"] = 1
		data["A2-4"] = 1
		data["F2-1"] = 0
		data["F2-2"] = 0
		data["V2-1"] = 0
		data["V2-2"] = 0
		data["V2-3"] = 1
		data["V2-4"] = 1
		data["A3-1"] = 0
		data["A3-2"] = 0
		data["A3-3"] = 0
		data["A3-4"] = 0

#Right-Blue
	elif nr == 8:		
		data["A1-1"] = 0
		data["A1-2"] = 0
		data["A1-3"] = 0
		data["B1-1"] = 0
		data["B1-2"] = 0
		data["F1-1"] = 1
		data["F1-2"] = 1
		data["V1-1"] = 0
		data["V1-2"] = 0
		data["V1-3"] = 0
		data["V1-4"] = 0
		data["A2-1"] = 0
		data["A2-2"] = 0
		data["A2-3"] = 1
		data["A2-4"] = 1
		data["F2-1"] = 0
		data["F2-2"] = 0
		data["V2-1"] = 0
		data["V2-2"] = 0
		data["V2-3"] = 0
		data["V2-4"] = 0
		data["A3-1"] = 0
		data["A3-2"] = 0
		data["A3-3"] = 1
		data["A3-4"] = 1
		
	elif nr == 10:
		data["A1-1"] = 0
		data["A1-2"] = 0
		data["A1-3"] = 0
		data["B1-1"] = 0
		data["B1-2"] = 0
		data["F1-1"] = 0
		data["F1-2"] = 0
		data["V1-1"] = 1
		data["V1-2"] = 1
		data["V1-3"] = 0
		data["V1-4"] = 0
		data["A2-1"] = 0
		data["A2-2"] = 0
		data["A2-3"] = 0
		data["A2-4"] = 0
		data["F2-1"] = 0
		data["F2-2"] = 0
		data["V2-1"] = 0
		data["V2-2"] = 0
		data["V2-3"] = 0
		data["V2-4"] = 0
		data["A3-1"] = 1
		data["A3-2"] = 1
		data["A3-3"] = 1
		data["A3-4"] = 1
		
	elif nr == 12:
		data["A1-1"] = 0
		data["A1-2"] = 0
		data["A1-3"] = 0
		data["B1-1"] = 1
		data["B1-2"] = 1
		data["F1-1"] = 0
		data["F1-2"] = 0
		data["V1-1"] = 0
		data["V1-2"] = 0
		data["V1-3"] = 0
		data["V1-4"] = 0
		data["A2-1"] = 1
		data["A2-2"] = 1
		data["A2-3"] = 0
		data["A2-4"] = 0
		data["F2-1"] = 0
		data["F2-2"] = 0
		data["V2-1"] = 0
		data["V2-2"] = 0
		data["V2-3"] = 0
		data["V2-4"] = 0
		data["A3-1"] = 0
		data["A3-2"] = 0
		data["A3-3"] = 0
		data["A3-4"] = 0
		
	elif nr == 14:
		data["A1-1"] = 1
		data["A1-2"] = 1
		data["A1-3"] = 1
		data["B1-1"] = 0
		data["B1-2"] = 0
		data["F1-1"] = 0
		data["F1-2"] = 0
		data["V1-1"] = 0
		data["V1-2"] = 0
		data["V1-3"] = 1
		data["V1-4"] = 1
		data["A2-1"] = 0
		data["A2-2"] = 0
		data["A2-3"] = 0
		data["A2-4"] = 0
		data["F2-1"] = 0
		data["F2-2"] = 0
		data["V2-1"] = 0
		data["V2-2"] = 0
		data["V2-3"] = 0
		data["V2-4"] = 0
		data["A3-1"] = 0
		data["A3-2"] = 0
		data["A3-3"] = 0
		data["A3-4"] = 0

def updateLightL(nr):
	#Set everything to Red
	if nr == 1:
		data["A4-1"] = 0
		data["A4-2"] = 0
		data["A4-3"] = 0
		data["A4-4"] = 0
		data["B4-1"] = 0
		data["F4-1"] = 0
		data["F4-2"] = 0
		data["V4-1"] = 0
		data["V4-2"] = 0
		data["V4-3"] = 0
		data["V4-4"] = 0
		data["A5-1"] = 0
		data["A5-2"] = 0
		data["A5-3"] = 0
		data["A5-4"] = 0
		data["F5-1"] = 0
		data["F5-2"] = 0
		data["V5-1"] = 0
		data["V5-2"] = 0
		data["V5-3"] = 0
		data["V5-4"] = 0
		data["A6-1"] = 0
		data["A6-2"] = 0
		data["A6-3"] = 0
		data["A6-4"] = 0

#Left-Purple
	if nr == 2:		
		data["A4-1"] = 0
		data["A4-2"] = 0
		data["A4-3"] = 1
		data["A4-4"] = 1
		data["B4-1"] = 0
		data["F4-1"] = 0
		data["F4-2"] = 0
		data["V4-1"] = 0
		data["V4-2"] = 0
		data["V4-3"] = 0
		data["V4-4"] = 0
		data["A5-1"] = 0
		data["A5-2"] = 0
		data["A5-3"] = 0
		data["A5-4"] = 0
		data["F5-1"] = 1
		data["F5-2"] = 1
		data["V5-1"] = 0
		data["V5-2"] = 0
		data["V5-3"] = 0
		data["V5-4"] = 0
		data["A6-1"] = 0
		data["A6-2"] = 0
		data["A6-3"] = 1
		data["A6-4"] = 1

#Left-Red
	elif nr == 4:
		data["A4-1"] = 0
		data["A4-2"] = 0
		data["A4-3"] = 0
		data["A4-4"] = 0
		data["B4-1"] = 0
		data["F4-1"] = 0
		data["F4-2"] = 0
		data["V4-1"] = 0
		data["V4-2"] = 0
		data["V4-3"] = 0
		data["V4-4"] = 0
		data["A5-1"] = 0
		data["A5-2"] = 0
		data["A5-3"] = 0
		data["A5-4"] = 0
		data["F5-1"] = 0
		data["F5-2"] = 0
		data["V5-1"] = 0
		data["V5-2"] = 0
		data["V5-3"] = 1
		data["V5-4"] = 1
		data["A6-1"] = 1
		data["A6-2"] = 1
		data["A6-3"] = 1
		data["A6-4"] = 1

#Left-Green
	elif nr == 6:
		data["A4-1"] = 0
		data["A4-2"] = 0
		data["A4-3"] = 0
		data["A4-4"] = 0
		data["B4-1"] = 0
		data["F4-1"] = 0
		data["F4-2"] = 0
		data["V4-1"] = 0
		data["V4-2"] = 0
		data["V4-3"] = 0
		data["V4-4"] = 0
		data["A5-1"] = 1
		data["A5-2"] = 1
		data["A5-3"] = 1
		data["A5-4"] = 1
		data["F5-1"] = 0
		data["F5-2"] = 0
		data["V5-1"] = 1
		data["V5-2"] = 1
		data["V5-3"] = 0
		data["V5-4"] = 0
		data["A6-1"] = 0
		data["A6-2"] = 0
		data["A6-3"] = 0
		data["A6-4"] = 0

#Left-Blue
	elif nr == 8:
		data["A4-1"] = 0
		data["A4-2"] = 0
		data["A4-3"] = 0
		data["A4-4"] = 0
		data["B4-1"] = 0
		data["F4-1"] = 1
		data["F4-2"] = 1
		data["V4-1"] = 0
		data["V4-2"] = 0
		data["V4-3"] = 0
		data["V4-4"] = 0
		data["A5-1"] = 1
		data["A5-2"] = 1
		data["A5-3"] = 0
		data["A5-4"] = 0
		data["F5-1"] = 0
		data["F5-2"] = 0
		data["V5-1"] = 0
		data["V5-2"] = 0
		data["V5-3"] = 0
		data["V5-4"] = 0
		data["A6-1"] = 1
		data["A6-2"] = 1
		data["A6-3"] = 0
		data["A6-4"] = 0
		
	elif nr == 10:
		data["A4-1"] = 0
		data["A4-2"] = 0
		data["A4-3"] = 0
		data["A4-4"] = 0
		data["B4-1"] = 0
		data["F4-1"] = 0
		data["F4-2"] = 0
		data["V4-1"] = 0
		data["V4-2"] = 0
		data["V4-3"] = 1
		data["V4-4"] = 1
		data["A5-1"] = 0
		data["A5-2"] = 0
		data["A5-3"] = 0
		data["A5-4"] = 0
		data["F5-1"] = 0
		data["F5-2"] = 0
		data["V5-1"] = 0
		data["V5-2"] = 0
		data["V5-3"] = 0
		data["V5-4"] = 0
		data["A6-1"] = 1
		data["A6-2"] = 1
		data["A6-3"] = 1
		data["A6-4"] = 1
		
	elif nr == 12:
		data["A4-1"] = 1
		data["A4-2"] = 1
		data["A4-3"] = 0
		data["A4-4"] = 0
		data["B4-1"] = 1
		data["F4-1"] = 0
		data["F4-2"] = 0
		data["V4-1"] = 0
		data["V4-2"] = 0
		data["V4-3"] = 0
		data["V4-4"] = 0
		data["A5-1"] = 0
		data["A5-2"] = 0
		data["A5-3"] = 1
		data["A5-4"] = 1
		data["F5-1"] = 0
		data["F5-2"] = 0
		data["V5-1"] = 0
		data["V5-2"] = 0
		data["V5-3"] = 0
		data["V5-4"] = 0
		data["A6-1"] = 0
		data["A6-2"] = 0
		data["A6-3"] = 0
		data["A6-4"] = 0
		
	elif nr == 14:
		data["A4-1"] = 1
		data["A4-2"] = 1
		data["A4-3"] = 1
		data["A4-4"] = 1
		data["B4-1"] = 0
		data["F4-1"] = 0
		data["F4-2"] = 0
		data["V4-1"] = 1
		data["V4-2"] = 1
		data["V4-3"] = 0
		data["V4-4"] = 0
		data["A5-1"] = 0
		data["A5-2"] = 0
		data["A5-3"] = 0
		data["A5-4"] = 0
		data["F5-1"] = 0
		data["F5-2"] = 0
		data["V5-1"] = 0
		data["V5-2"] = 0
		data["V5-3"] = 0
		data["V5-4"] = 0
		data["A6-1"] = 0
		data["A6-2"] = 0
		data["A6-3"] = 0
		data["A6-4"] = 0


def getTime():
	if getStage('r') % 2 == 1:
		return 5
	else:
		return 10

def getStage(side):
	if side == 'r':
		return rStage
	else:
		return lStage

def setStage(r, l):
	global rStage, lStage
	rStage = r
	lStage = l

def getSmart():
	print("smart: ", str(smart))
	return smart

def isSmart(bool):
	global smart
	smart = bool

def receiving(c):
	while True:
		data = ''
		data = c.recv(1024).decode("utf-8")
		
		length = int(data[:3])
		data = data[4:]
		data = data[:length]
		
		if not data:
			isSmart(False)
		else:
			isSmart(True)
			updateRecvData(data)

def getRecvData():
	return recvData

def updatePrio(list, pos, val):
	if list == 'r':
		if val == 1:
			rSetPrio[pos] = rSetPrio[pos] + val
		else:
			rSetPrio[pos] = val

	else:
		if val == 1:
			lSetPrio[pos] = lSetPrio[pos] + val
		else:
			lSetPrio[pos] = val

	
def updateRecvData(data):
	global recvData
	recvData = data
	
def SmartLights():
	data = getRecvData()
	data = json.loads(data)
	listData = []
	for light, state in data.items():
		if state == 1:
			listData.append(light)
	listData = set(listData)

	#Sets of traffic lights
	right1 = ['A1-1','A1-2','A3-1','A3-2','F2-1','F2-2']
	right2 = ['A3-1','A3-2','A3-3','A3-4','V2-1','V2-2']
	right3 = ['A2-1','A2-2','A2-3','A2-4','V2-3','V2-4']
	right4 = ['A2-3','A2-4','A3-3','A3-4','F1-1','F1-2']
	right5 = ['A3-1','A3-2','A3-3','A3-4','V1-1','V1-2']
	right6 = ['B1-1','B1-2','A2-1','A2-2']
	right7 = ['A1-1','A1-2','A1-3','V1-3','V1-4']
	
	left1 = ['A4-3','A4-4','A6-3','A6-4','F5-1','F5-2']
	left2 = ['A6-1','A6-2','A6-3','A6-4','V5-3','V5-4']
	left3 = ['A5-1','A5-2','A5-3','A5-4','V5-1','V5-2']
	left4 = ['A5-1','A5-2','A6-1','A6-2','F4-1','F4-2']
	left5 = ['A6-1','A6-2','A6-3','A6-4','V4-3','V4-4']
	left6 = ['A4-1','A4-2','B4-1','A5-3','A5-4']
	left7 = ['A4-1','A4-2','A4-3','A4-4','V4-1','V4-2']


	#Count waiting traffic for each set
	rSet1 = (len(listData.intersection(right1))) + rSetPrio[0]
	rSet2 = (len(listData.intersection(right2))) + rSetPrio[1]
	rSet3 = (len(listData.intersection(right3))) + rSetPrio[2]
	rSet4 = (len(listData.intersection(right4))) + rSetPrio[3]
	rSet5 = (len(listData.intersection(right5))) + rSetPrio[4]
	rSet6 = (len(listData.intersection(right6))) + rSetPrio[5] + 3 #bus prio
	rSet7 = (len(listData.intersection(right7))) + rSetPrio[6]
	
	lSet1 = (len(listData.intersection(left1))) + lSetPrio[0]
	lSet2 = (len(listData.intersection(left2))) + lSetPrio[1]
	lSet3 = (len(listData.intersection(left3))) + lSetPrio[2]
	lSet4 = (len(listData.intersection(left4))) + lSetPrio[3]
	lSet5 = (len(listData.intersection(left5))) + lSetPrio[4]
	lSet6 = (len(listData.intersection(left6))) + lSetPrio[5] + 2 #bus prio
	lSet7 = (len(listData.intersection(left7))) + lSetPrio[6]
	
	#Compare sets and return the one with the most waiting traffic
	CompareRight = {2: rSet1, 4: rSet2, 6: rSet3, 8: rSet4, 10: rSet5, 12: rSet6, 14: rSet7}
	CompareLeft = {2: lSet1, 4: lSet2, 6: lSet3, 8: lSet4, 10: lSet5, 12: lSet6, 14: lSet7}
	
	rs = max(CompareRight, key=CompareRight.get)
	ls = max(CompareLeft, key=CompareLeft.get)
	
	print("prio r: ", str(rSetPrio))
	print("prio l: ", str(lSetPrio))
	
	for x in range(0,7):
		if not rs / 2 - 1 == x:
			updatePrio('r', x, 1)
		else:
			updatePrio('r', x, 0)
		
		
		if not ls / 2 - 1 == x:
			updatePrio('l', x, 1)
		else:
			updatePrio('l', x, 0)

	setStage(
		getStage('r') % 2 == 1 and rs or 1,
		getStage('l') % 2 == 1 and ls or 1
	)


def update():
	print("rStage: ", str(rStage), " & lStage: ", str(lStage))
	rStage % 2 == 1 and updateLightR(1) or updateLightR(rStage)
	lStage % 2 == 1 and updateLightL(1) or updateLightL(lStage)