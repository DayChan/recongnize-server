#coding:utf-8
from __future__ import unicode_literals
import HyperLPRLite as pr
import cv2
import numpy as np


from django.shortcuts import render
from django.http import HttpResponse

def recong(path):
	grr = cv2.imread(str(path))
	model1 = pr.LPR("model/cascade.xml","model/model12.h5","model/ocr_plate_all_gru.h5")

	for pstr,confidence,rect in model1.SimpleRecognizePlateByE2E(grr):
		if confidence>0.7:
		    
		    print("plate_str",pstr[-6:])
		    print("plate_confidence",confidence)



	cv2.waitKey(0)
	return pstr
