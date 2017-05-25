#!/usr/bin/python
#-*- coding: UTF-8 -*- 
#coding=utf-8
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.db import connection

from django.conf import settings
from datetime import datetime 
import json
import time


def get_json_response(request, json_rsp):
    return HttpResponse(json.dumps(json_rsp), content_type='application/json')


def list_prescription(request):

    url_path = request.get_host()
    images_path = settings.MEDIA_URL

    ption_list = []

    sql ='SELECT test_prescription.prescription_id,test_prescription.prescription_idx_id,test_prescription.prescription_name,test_prescription.prescription_age,test_prescription.prescription_date,test_prescription.prescription_cost,test_prescription.prescription_sex,test_prescription.prescription_diagnose,test_prescription.prescription_hospital,test_prescription.prescription_department,test_prescription.prescription_doctor,test_prescription.prescription_img_path,test_prescription.prescription_docx_path,group_concat(concat(test_medicine.medicine_name)SEPARATOR ',') as medicine_name FROM test_prescription LEFT JOIN test_medicine ON test_medicine.prescription_idx_id = test_prescription.prescription_idx_id GROUP BY prescription_idx_id' 
    cursor=connection.cursor()
    row = cursor.execute(sql)
    print row 
    line = cursor.fetchall()
    print line
    cursor.close()
    connection.close()

    exihibitpic = url_path + images_path
    exihibitpic = exihibitpic.decode('utf-8')
    for i in line:
	lines = {}
	lines['prescription_id'] = i[0]
	lines['prescription_idx_id'] = i[1]	
	lines['prescription_name'] = i[2]
	lines['prescription_age'] = i[3]
        lines['prescription_date'] = i[4]
	lines['prescription_cost'] = str(i[5])
        lines['prescription_sex'] = i[6]
	lines['prescription_diagnose'] = i[7]
	lines['prescription_hospital'] = i[8]
	lines['prescription_department'] = i[9]
	lines['prescription_doctor'] = i[10]
	lines['prescription_img_path'] = exihibitpic + i[11]
	lines['prescription_docx_path'] = i[12]
	lines['medicine_name'] = i[13]
	ption_list.append(lines)
	
    rst_data = {
	"data":ption_list
    }
    return get_json_response(request, dict(data=rst_data))


def list_only(request):
   
    if request.method != 'POST':
        return get_json_response(request, dict(status='error', message='only POST method supported.', data=None))

    ption_id = reuqest.POST.get('id',None)
    if ption_id is None:
        return get_json_response(request, dict(status='error', message='id is None', data=None))

    prescription = Prescription.objects.filter(id = ption_id)
    if prescription is []:
        return get_json_response(request, dict(status='error', message='prescription is None', data=None))

    ption_list = []   
    url_path = request.get_host()
    images_path = settings.MEDIA_URL
 
    exihibitpic = url_path + images_path
 
    for i in prescription:
	image = i.image
        image_json = i.image_json
        ption_data = {
            'id':id,
            'image':exihibitpic + str(image),
            'image_json':image_json.replace("\r\n"," ")
        }
	ption_list.append(ption_data)

    rst_data = {
        "data":ption_list
    }
    return get_json_response(request, dict(status='1', message='1', data=rst_data))

def update_ption(request):

   if request.method != 'POST':
        return get_json_response(request, dict(status='error', message='only POST method supported.', data=None))

   ption_id = request.POST.get('id',None)
   if ption_id is None:
        return get_json_response(request, dict(status='error', message='id is None', data=None))

   ption_json = request.POST.get('image_json',None)
   if ption_json is None:
        return get_json_response(request, dict(status='error', message='ption_json is None', data=None))

   prescription = Prescription.objects.filter(id = ption_id)
   if prescription:
        for _ in prescription:
            _.image_json = ption_json
	    _.save()
        return get_json_response(request, dict(status='1', message='Success'))

   else:
	return get_json_response(request, dict(status='error', message='prescription is None', data=None))


#def increase_ption(request):
#
#    if request.method != 'POST':
#        return get_json_response(request, dict(status='error', message='only POST method supported.', data=None))
#
#    file_obj = request.FILES.get('image', None)
#    if not file_obj:
#	return get_json_response(request, dict(status='error', message='Image is None', data=None))
#
#    image_json = request.POST.get('image_json',None)
#    if not image_json:
#        return get_json_response(request, dict(status='error', message='Image_json is None',data=None))
#      
#    file_name = 'ption_{}_{}.jpg'.format(datetime.now().strftime("%Y%m%d%H%M%S"),random.randint(1000, 9999))
#    file_dest = '/home/lzq/Prescription/images/exhibited_picture/2017/05/23/{}'.format(file_name)
#    writer = open(file_dest, 'wb+')
#    writer.write(file_obj)
#    writer.close()
#    file_objs = '/exhibited_picture/2017/05/23/' + file_name
#    
#    prescription = Prescription.objects(image = file_objs,image_json = image_json)
#    prescription.save()
#
#    return get_json_response(request, dict(status='1', message='Success'))

#def def_ption(request):
#    if request.method != 'POST':
#        return get_json_response(request, dict(status='error', message='only POST method supported.', data=None))
#    ption_id = request.POST.get('id',None)
#    if ption_id is None:
#        return get_json_response(request, dict(status='error', message='id is None', data=None))
#    prescription = Prescription.objects.filter(id = ption_id)
#    if prescription:
#    	prescription.delete()
#
#    	return get_json_response(request, dict(status='1', message='Success'))
#    else:
#	return get_json_response(request, dict(status='error', message='prescription is None', data=None))

def dev(request):
    data_list = []
    prescription = Prescription.objects.all()
    for _ in prescription:
	id = _.prescription_id
	prescription_name = _.prescription_name

	
	mes ={
	    'id':id,
	    'prescription_name':prescription_name
	}
	data_list.append(mes)
    rst_data = {
        "data":data_list
    }
	  

    return get_json_response(request, dict(status='error', message='prescription is None', data=rst_data))
 
