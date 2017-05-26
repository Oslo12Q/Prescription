from rest_framework import serializers
from .models import *


class MedicineSerializer(serializers.HyperlinkedModelSerializer):
   
    prescription_name = serializers.CharField(source='prescription_idx_id.prescription_name')
    class Meta:
	model = Medicine
	fields = ('prescription_name','medicine_name')


class PrescriptionSerializer(serializers.HyperlinkedModelSerializer):

    medicine = MedicineSerializer(source='medicine_set',many=True)
    
    class Meta:
	model = Prescription
	fields = ('prescription_idx_id','prescription_name','prescription_age','prescription_date','prescription_cost','prescription_sex','prescription_diagnose','prescription_hospital','prescription_department','medicine','prescription_doctor','prescription_img_path','prescription_docx_path')
    
