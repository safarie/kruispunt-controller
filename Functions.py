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
	print("r" + str(nr))
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
		data["A1-3"] = 1
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

#Right-Red
	elif nr == 4:
		data["A1-1"] = 0
		data["A1-2"] = 0
		data["A1-3"] = 0
		data["B1-1"] = 0
		data["B1-2"] = 0
		data["F1-1"] = 1
		data["F1-2"] = 1
		data["V1-1"] = 1
		data["V1-2"] = 1
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

#Right-Green
	elif nr == 6:		
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
		data["V2-2"] = 1
		data["V2-3"] = 1
		data["V2-4"] = 0
		data["A3-1"] = 1
		data["A3-2"] = 1
		data["A3-3"] = 0
		data["A3-4"] = 0

#Right-Blue
	elif nr == 8:		
		data["A1-1"] = 1
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

def updateLightL(nr):
	print("l" + str(nr))
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

#Left-Red
	elif nr == 4:
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

#Left-Green
	elif nr == 6:
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

#Left-Blue
	elif nr == 8:
		data["A4-1"] = 0
		data["A4-2"] = 0
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
