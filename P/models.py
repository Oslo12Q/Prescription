#!/usr/bin/python
#-*- coding: UTF-8 -*- 
#coding=utf-8
from __future__ import unicode_literals

from django.db import models


class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    prescription_idx_id = models.IntegerField(unique = True,verbose_name = '化验单编号')
    prescription_name = models.CharField(max_length=200,verbose_name = '姓名')
    prescription_age = models.IntegerField(verbose_name = '年龄')
    prescription_date = models.CharField(max_length=255, blank=True, null=True,verbose_name = '处方单时间')
    prescription_cost = models.CharField(max_length=255, blank=True, null=True,verbose_name = '费用')
    prescription_sex = models.CharField(max_length=255, blank=True, null=True,verbose_name = '性别')
    prescription_diagnose = models.CharField(max_length=255, blank=True, null=True,verbose_name = '诊断描述信息')
    prescription_hospital = models.CharField(max_length=255, blank=True, null=True,verbose_name = '医院')
    prescription_department = models.CharField(max_length=255, blank=True, null=True,verbose_name = '科室')
    prescription_doctor = models.CharField(max_length=255, blank=True, null=True,verbose_name = '医生')
    prescription_img_path = models.ImageField(upload_to='exhibited_picture/%Y/%m/%d', blank=False,verbose_name = '处方单图片存放位置')
    prescription_docx_path = models.ImageField(upload_to='ocr_file/%Y/%m/%d', blank=False,verbose_name = 'ocr文件存放位置')
    prescription_crate_date = models.DateTimeField(blank=True, null=True,verbose_name = '创建时间')
    prescription_update_date = models.DateTimeField(blank=True, null=True,verbose_name = '更新时间')
    prescription_test_1 = models.CharField(max_length=255, blank=True, null=True)
    prescription_test_2 = models.CharField(max_length=255, blank=True, null=True)
    prescription_test_3 = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
	return self.prescription_name

    class Meta:
	verbose_name = '处方单'
	verbose_name_plural = '处方单'

class Medicine(models.Model):
    prescription_idx_id = models.ForeignKey(Prescription,blank=True, null=True,to_field = 'prescription_idx_id',verbose_name = '处方单名字')
    medicine_id = models.AutoField(primary_key=True)
    medicine_idx_id = models.IntegerField(verbose_name = '药物信息编号')
    medicine_name = models.CharField(max_length=255, blank=True, null=True,verbose_name = '药品')
    medicine_component = models.TextField(blank=True, null=True,verbose_name = '药品成分')
    medicine_indication = models.TextField(blank=True, null=True,verbose_name = '适应症状')
    medicine_dosage = models.TextField(blank=True, null=True,verbose_name = '服用方法')
    medicine_test_1 = models.CharField(max_length=255, blank=True, null=True)
    medicine_test_2 = models.CharField(max_length=255, blank=True, null=True)
    medicine_test_3 = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = '药品'
        verbose_name_plural = '药品'

    def __unicode__(self):
        return self.medicine_name
    
