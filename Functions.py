import json
import time

smart = False
rStage = 0
lStage = 0
rPrio = [0,0,0,0,0,0,0,0]
lPrio = [0,0,0,0,0,0,0,0]
recvData = ''
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
    #Clearing
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

	#Right 1
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
		data["V2-1"] = 1
		data["V2-2"] = 0
		data["V2-3"] = 0
		data["V2-4"] = 1
		data["A3-1"] = 1
		data["A3-2"] = 1
		data["A3-3"] = 0
		data["A3-4"] = 0

	#Right 2
	elif nr == 4:
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
		data["V2-1"] = 1
		data["V2-2"] = 1
		data["V2-3"] = 0
		data["V2-4"] = 0
		data["A3-1"] = 1
		data["A3-2"] = 1
		data["A3-3"] = 1
		data["A3-4"] = 1

	#Right 3
	elif nr == 6:	
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

	#Right 4
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
		data["V1-3"] = 1
		data["V1-4"] = 1
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

	#Right:5
	elif nr == 10:	
		data["A1-1"] = 1
		data["A1-2"] = 1
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

	#Right:6
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

	#Right:7
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
		data["V2-1"] = 1
		data["V2-2"] = 1
		data["V2-3"] = 0
		data["V2-4"] = 0
		data["A3-1"] = 0
		data["A3-2"] = 0
		data["A3-3"] = 0
		data["A3-4"] = 0
		
	#Right:8
	elif nr == 16:	
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
		data["A2-3"] = 0
		data["A2-4"] = 0
		data["F2-1"] = 1
		data["F2-2"] = 1
		data["V2-1"] = 0
		data["V2-2"] = 0
		data["V2-3"] = 0
		data["V2-4"] = 0
		data["A3-1"] = 0
		data["A3-2"] = 0
		data["A3-3"] = 0
		data["A3-4"] = 0

def updateLightL(nr):
	#Clearing
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

	#Left 1
	if nr == 2:		
		data["A4-1"] = 1
		data["A4-2"] = 1
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

	#Left 2
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
		data["V5-3"] = 1
		data["V5-4"] = 1
		data["A6-1"] = 1
		data["A6-2"] = 1
		data["A6-3"] = 1
		data["A6-4"] = 1

	#Left 3
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
		data["V4-3"] = 1
		data["V4-4"] = 1
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

	#Left 4
	elif nr == 8:
		data["A4-1"] = 0
		data["A4-2"] = 0
		data["A4-3"] = 0
		data["A4-4"] = 0
		data["B4-1"] = 0
		data["F4-1"] = 1
		data["F4-2"] = 1
		data["V4-1"] = 1
		data["V4-2"] = 1
		data["V4-3"] = 1
		data["V4-4"] = 1
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
	
	#Left:5
	elif nr == 10:
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
		data["V5-1"] = 1
		data["V5-2"] = 1
		data["V5-3"] = 1
		data["V5-4"] = 1
		data["A6-1"] = 0
		data["A6-2"] = 0
		data["A6-3"] = 1
		data["A6-4"] = 1
	
	#Left:6
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

	#Left:7
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
		data["V5-3"] = 1
		data["V5-4"] = 1
		data["A6-1"] = 0
		data["A6-2"] = 0
		data["A6-3"] = 0
		data["A6-4"] = 0
	
	#left 8
	if nr == 16:
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

def updateRecvData(data):
	global recvData
	recvData = data

def updatePrio(side ,stage, reset):
	if side == 'r': 
		if reset:
			rPrio[int(stage / 2 - 1)] += 1
		else:
			rPrio[int(stage / 2 - 1)] = 0
	else:
		if reset:
			lPrio[int(stage / 2 - 1)] += 1
		else:	
			lPrio[int(stage / 2 - 1)] = 0


def SmartLights():
	data = getRecvData()
	data = json.loads(data)
	listData = []
	for light, state in data.items():
		if state == 1:
			listData.append(light)
	listData = set(listData)

	right1 = ['A1-1','A1-2','A3-1','A3-2']
	right2 = ['A3-1','A3-2','A3-3','A3-4']
	right3 = ['A2-1','A2-2','A2-3','A2-4']
	right4 = ['A2-3','A2-4','A3-3','A3-4']
	right5 = ['A3-3','A3-4','A1-1','A1-2']
	right6 = ['B1-1','B1-2']
	right7 = ['A1-1','A1-2','A1-3']
	right8 = ['F1-1','F1-2','F2-1','F2-2']

	left1 = ['A4-3','A4-4','A5-3','A5-4']
	left2 = ['A6-1','A6-2','A6-3','A6-4']
	left3 = ['A5-1','A5-2','A5-3','A5-4']
	left4 = ['A5-1','A5-2','A6-1','A6-2']
	left5 = ['A6-3','A6-4','A4-3','A4-4']
	left6 = ['A4-2','B4-1','A5-3','A5-4'] 
	left7 = ['A4-1','A4-2','A4-3','A4-4']
	left8 = ['F4-1','F4-2','F5-1','F5-2']

	#Count waiting traffic for each set
	rSet1 = (len(listData.intersection(right1)))
	rSet2 = (len(listData.intersection(right2)))
	rSet3 = (len(listData.intersection(right3)))
	rSet4 = (len(listData.intersection(right4)))
	rSet5 = (len(listData.intersection(right5)))
	rSet6 = (len(listData.intersection(right6)))
	rSet7 = (len(listData.intersection(right7)))
	rSet8 = (len(listData.intersection(right8)))

	#extra prio for busses
	if rSet6 != 0: rSet6 = rSet6 + 3
	if rSet7 != 0: rSet7 = rSet7 + 1
	
	lSet1 = (len(listData.intersection(left1)))
	lSet2 = (len(listData.intersection(left2)))
	lSet3 = (len(listData.intersection(left3)))
	lSet4 = (len(listData.intersection(left4)))
	lSet5 = (len(listData.intersection(left5)))
	lSet6 = (len(listData.intersection(left6)))
	lSet7 = (len(listData.intersection(left7)))
	lSet8 = (len(listData.intersection(left8)))

	#order of values: stage, number of cars, prio.	
	rCompare = [(2,rSet1,1),(4,rSet2,rPrio[1]),(6,rSet3,rPrio[2]),(8,rSet4,1),(10,rSet5,1),(12,rSet6,rPrio[5]),(14,rSet7,rPrio[6]),(16,rSet8,rPrio[7])]
	lCompare = [(2,lSet1,1),(4,lSet2,lPrio[1]),(6,lSet3,lPrio[2]),(8,lSet4,1),(10,lSet5,1),(12,lSet6,lPrio[5]),(14,lSet7,lPrio[6]),(16,lSet8,lPrio[7])]

	#order first based on highest number of cars, then highest prio
	rs = sorted(rCompare, key=lambda x: (x[1],x[2]), reverse=True)
	ls = sorted(lCompare, key=lambda x: (x[1],x[2]), reverse=True)
	
	print("sort rs:", str(rs))
	print("sort ls:", str(ls))

	rs = rs[0][0]
	ls = ls[0][0]
	
	#dynamic prio for entrance routes
	if getStage('r') == 1:
		for r in rCompare:
			updatePrio('r' ,r[0], r[0] != rs)
	
	if getStage('l') == 1:
		for l in lCompare:
			updatePrio('l', l[0], l[0] != ls)
	
	
	#set next stage based on current stage. if current is even, next stage is a clearing stage
	setStage(
		getStage('r') % 2 == 1 and rs or 1,
		getStage('l') % 2 == 1 and ls or 1
	)

def update():
	print("rStage: ", str(rStage), " & lStage: ", str(lStage))
	rStage % 2 == 1 and updateLightR(1) or updateLightR(rStage)
	lStage % 2 == 1 and updateLightL(1) or updateLightL(lStage)