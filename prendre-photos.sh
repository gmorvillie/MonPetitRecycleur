#!/bin/bash

NAME=cam
i=0
while : 
do
	raspistill -o /home/pi/MonPetitRecycleur/photosRI/$NAME$i.jpg
	i=$((i+1))
done

