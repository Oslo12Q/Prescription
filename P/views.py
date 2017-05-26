#!/usr/bin/python
#-*- coding: UTF-8 -*- 
#coding=utf-8
from django.shortcuts import render
from .models import *
from django.http import HttpResponse

from django.conf import settings
from datetime import datetime 
import json
import time
from rest_framework import mixins,generics
from P.serializers import *


class PrescriptionList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class prescriptionDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


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


def dev(request):
    data_list = []
    prescription = Prescription.objects.all()
    for _ in prescription:
	id = _.prescription_idx_id
	prescription_name = _.prescription_name
	
	medicine = Medicine.objects.filter(prescription_idx_id = id)
	for i in medicine:
	    medicine_name = i.medicine_name
	    
	    mes ={
	        'id':id,
	        'prescription_name':prescription_name,
	        'medicine_name':medicine_name
	    }
	    data_list.append(mes)
    rst_data = {
        "data":data_list
    }
	  

    return get_json_response(request, dict(status='1', message='Success', data=rst_data))

