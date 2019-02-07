import json
import numpy as np
import datetime
from elasticsearch import Elasticsearch



boxesEX = np.array([[1, 2, 1, 2],[1, 3, 1, 3],[2, 3, 2, 3]]) #boxes coordinates
classesEX = np.array([1, 2, 1]) #orga trash orga
scoresEX = np.array([0.9, 0.8, 0.9])

def toJson(boxes, classes, score):
	es = Elasticsearch()
	with open('box.json', 'w') as outfile: 
			json.dump([], outfile, indent = 0) 
	
	time = str(datetime.datetime.now())
	
	for i, elem in enumerate(boxes):
		box = {
			'Type de dechet': int(classes[i]),
			'confidence': float(score[i]),
			'timestamp': datetime.now(),
		}
		#box = {}  
		#box['Type de dechet'] = int(classes[i])
		#box['confidence'] = float(score[i])
		#box['timestamp'] = time
		res = es.index(index="boites", doc_type='boite', id=1, body=doc)
		
		

	

		#ICI METTRE DICO.APPEND
	
	
	with open('box.json', 'w') as filefeed:
		json.dump(box, filefeed, indent = 0)	
		filefeed.write("\n")

toJson(boxesEX, classesEX, scoresEX)
