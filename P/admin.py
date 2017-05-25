from django.contrib import admin
from .models import *

# Register your models here.

class MedicineInline(admin.TabularInline):
	model = Medicine
	extra = 1


class PrescriptionAdmin(admin.ModelAdmin):

    inlines = [
	MedicineInline,
    ]
    list_display = ('prescription_idx_id','prescription_name','prescription_age','prescription_date','prescription_cost','prescription_sex','prescription_diagnose')
    search_fields = ['prescription_name']

class MedicineAdmin(admin.ModelAdmin):
    search_fields = ['medicine_name']
    list_display = ('prescription_idx_id_id','medicine_name','medicine_component','medicine_indication','medicine_dosage')

admin.site.register(Prescription,PrescriptionAdmin)
admin.site.register(Medicine,MedicineAdmin)
