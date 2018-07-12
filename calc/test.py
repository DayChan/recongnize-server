#coding:utf-8
from __future__ import unicode_literals
import HyperLPRLite as pr
import cv2
import numpy as np


from django.shortcuts import render
from django.http import HttpResponse

#path = "images_rec/1.jpg"
model1 = 0


def recong(path):
	global model1
	grr = cv2.imread(str(path))
	if (model1 is 0):
		model1 = pr.LPR("model/cascade.xml","model/model12.h5","model/ocr_plate_all_gru.h5")
	result = model1.SimpleRecognizePlateByE2E(grr)
	#print result
	if result:
		best_result = result[0][0]
		for pstr,confidence,rect in result:
			if confidence>0.7:	    
				print("plate_str",pstr[-6:])
				print("plate_confidence",confidence)
				#cv2.waitKey(0)
		return best_result
	else:
		return "no plate"