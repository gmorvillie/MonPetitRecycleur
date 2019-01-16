import json
import numpy as np



boxesEX = np.array([[1, 2, 1, 2],[1, 3, 1, 3],[2, 3, 2, 3]]) #boxes coordinates
classesEX = np.array([1, 2, 1]) #orga trash orga
scoresEX = np.array([0.9, 0.8, 0.9])


def toJson(boxes, classes, scores):
	
	
	data = {}  
	data['plateau'] = []  
	
	for i, elem in enumerate(boxes):
		
		data['plateau'].append({  
			'idBoite': i, #int
			'typeDechet': classes[i], #int
			'score': scores[i] #int
	})

	with open('plateau.json', 'w') as outfile:  
		json.dump(data, outfile, indent = 0)
		
toJson(boxesEX, classesEX, scoresEX)
		

