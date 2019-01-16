import json
import numpy as np
import datetime


def toJson(boxes, classes, scores, name = 'plateau.json'):
	d = []
	plateau = {}  
	
	plateau['date'] = str(datetime.datetime.now()) 
	
	for i, elem in enumerate(boxes):
		
		d.append({  
			'idBoite': i, #int
			'typeDechet': classes[i], #int
			'score': scores[i] #float
	})
	
	plateau['boxes'] = d
	plateau.tolist()
	with open('plateau.json', 'w') as outfile:  
		json.dump(plateau, outfile, indent = 0)	
		outfile.write("\n")

		
		
