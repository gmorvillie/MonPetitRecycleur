import json
import numpy as np
import datetime
from elasticsearch import Elasticsearch

default_address = '18.185.48.125:9200'
index = {1 : 'grise', 2 : 'verte'}

boxesEX = np.array([[1, 1, 30, 30],[1, 1, 20, 20],[2,1, 20, 20]]) #boxes coordinates
classesEX = np.array([1, 2, 1]) #orga trash orga
scoresEX = np.array([0.9, 0.8, 0.9])


def toElastic(boxes, classes, score, category_index =  index, address = default_address):
	es = Elasticsearch([address])
	with open('box.json', 'w') as outfile: 
			json.dump([], outfile, indent = 0) 
	
	time = datetime.datetime.now()
	
	for i, elem in enumerate(boxes):
		if( float(score[i]) > 0.5):
			
			box = {
				'Restaurant' : 'RI',
				'Type de dechet': str(category_index[1]['name']),
				'confidence': float(score[i]),
				'timestamp': time,
				'Surface': float((boxes[i][2]-boxes[i][0])*(boxes[i][3]-boxes[i][1]))
			}
			print(box)
			res = es.index(index="surface", doc_type='boite',  body=box)
		
		
	
	

