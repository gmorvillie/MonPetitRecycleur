import json
import numpy as np


def toJson(boxes, classes, scores, name = 'plateau.json'):
	
	
	data = {}  
	data['plateau'] = []  
	
	for i, elem in enumerate(boxes):
		
		data['plateau'].append({  
			'idBoite': i, #int
			'typeDechet': classes[i], #int
			'score': scores[i] #int
	})

	with open(name, 'w') as outfile:  
		json.dump(data, outfile, indent = 0)
		
		
