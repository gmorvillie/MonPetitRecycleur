import json
import numpy as np
import datetime



boxesEX = np.array([[1, 2, 1, 2],[1, 3, 1, 3],[2, 3, 2, 3]]) #boxes coordinates
classesEX = np.array([1, 2, 1]) #orga trash orga
scoresEX = np.array([0.9, 0.8, 0.9])


def toJson(boxes, classes, scores):
	
	
	plateau = {}  
	plateau['boxes'] = []
	plateau['date'] = str(datetime.datetime.now()) 
	
	for i, elem in enumerate(boxes):
		
		plateau['boxes'].append({  
			'idBoite': i, #int
			'typeDechet': classes[i], #int
			'score': scores[i] #int
	})

	with open('plateau.json', 'w') as outfile:  
		json.dump(plateau, outfile, indent = 0)	
		outfile.write("\n")
		
toJson(boxesEX, classesEX, scoresEX)
		

