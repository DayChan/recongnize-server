# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import HyperLPRLite as pr
import cv2
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from test import recong

from forms import CureDataImageForm

# Create your views here.

def add(request):
	if request.method == 'POST':

		form = CureDataImageForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			image = form.save()
			#image = form.cleaned_data['file']
			#image1 = request.FILES.get('file')
			#print(image1)
			print(image.file)
			#print(image1.name)
			#print(form.cleaned_data['file'].name)
			path = 'Data/media/' + str(image.file)
			print (path)
			#path1 = default_storage.save(path,ContentFile(image1))
			#print(path1)
			#print(request)
			return HttpResponse(recong(path))
		else: return HttpResponse("form error")
	else:
		return HttpResponse("request error")

def add2(request):
    path = "images_rec/2.jpg"
    str = recong(path)
    return HttpResponse(str)

def index(request):
	return render(request, 'home.html')
