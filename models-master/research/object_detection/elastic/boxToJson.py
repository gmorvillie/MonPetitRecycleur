import json
import numpy as np
import datetime


boxesEX = np.array([[1, 2, 1, 2],[1, 3, 1, 3],[2, 3, 2, 3]]) #boxes coordinates
classesEX = np.array([1, 2, 1]) #orga trash orga
scoresEX = np.array([0.9, 0.8, 0.9])

def toJson(boxes, classes, score):
	
	with open('box.json', 'w') as outfile: 
			json.dump([], outfile, indent = 0) 
	
	time = str(datetime.datetime.now())
	
	for i, elem in enumerate(boxes):
		
		box = {}  
		box['Type de dechet'] = int(classes[i])
		box['confidence'] = float(score[i])
		box['timestamp'] = time
		
		#ICI METTRE DICO.APPEND
	
	
	with open('box.json', 'w') as filefeed:
		json.dump(box, filefeed, indent = 0)	
		filefeed.write("\n")

toJson(boxesEX, classesEX, scoresEX)
