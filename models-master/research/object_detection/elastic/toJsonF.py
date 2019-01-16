import json
import numpy as np
import datetime


def toJson(boxes, classes, scores, name = 'plateau.json'):
	
	plateau = {}  
	plateau['boxes'] = []
	plateau['date'] = str(datetime.datetime.now()) 
	
	for i, elem in enumerate(boxes):
		
		plateau['boxes'].append({  
			'idBoite': i, #int
			'typeDechet': classes[i], #int
			'score': scores[i] #float
	})

	with open('plateau.json', 'w') as outfile:  
		json.dump(plateau, outfile, indent = 0)	
		outfile.write("\n")

		
		
