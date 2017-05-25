# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicine_id', models.AutoField(serialize=False, primary_key=True)),
                ('medicine_idx_id', models.IntegerField(verbose_name='\u836f\u7269\u4fe1\u606f\u7f16\u53f7')),
                ('medicine_name', models.CharField(max_length=255, null=True, verbose_name='\u836f\u54c1', blank=True)),
                ('medicine_component', models.TextField(null=True, verbose_name='\u836f\u54c1\u6210\u5206', blank=True)),
                ('medicine_indication', models.TextField(null=True, verbose_name='\u9002\u5e94\u75c7\u72b6', blank=True)),
                ('medicine_dosage', models.TextField(null=True, verbose_name='\u670d\u7528\u65b9\u6cd5', blank=True)),
                ('medicine_test_1', models.CharField(max_length=255, null=True, blank=True)),
                ('medicine_test_2', models.CharField(max_length=255, null=True, blank=True)),
                ('medicine_test_3', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u836f\u54c1',
                'verbose_name_plural': '\u836f\u54c1',
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prescription_id', models.AutoField(serialize=False, primary_key=True)),
                ('prescription_idx_id', models.IntegerField(unique=True, verbose_name='\u5316\u9a8c\u5355\u7f16\u53f7')),
                ('prescription_name', models.CharField(max_length=200, verbose_name='\u59d3\u540d')),
                ('prescription_age', models.IntegerField(verbose_name='\u5e74\u9f84')),
                ('prescription_date', models.CharField(max_length=255, null=True, verbose_name='\u5904\u65b9\u5355\u65f6\u95f4', blank=True)),
                ('prescription_cost', models.DecimalField(null=True, verbose_name='\u8d39\u7528', max_digits=10, decimal_places=2, blank=True)),
                ('prescription_sex', models.CharField(max_length=255, null=True, verbose_name='\u6027\u522b', blank=True)),
                ('prescription_diagnose', models.CharField(max_length=255, null=True, verbose_name='\u8bca\u65ad\u63cf\u8ff0\u4fe1\u606f', blank=True)),
                ('prescription_hospital', models.CharField(max_length=255, null=True, verbose_name='\u533b\u9662', blank=True)),
                ('prescription_department', models.CharField(max_length=255, null=True, verbose_name='\u79d1\u5ba4', blank=True)),
                ('prescription_doctor', models.CharField(max_length=255, null=True, verbose_name='\u533b\u751f', blank=True)),
                ('prescription_img_path', models.ImageField(upload_to='exhibited_picture/%Y/%m/%d', verbose_name='\u5904\u65b9\u5355\u56fe\u7247\u5b58\u653e\u4f4d\u7f6e')),
                ('prescription_docx_path', models.ImageField(upload_to='ocr_file/%Y/%m/%d', verbose_name='ocr\u6587\u4ef6\u5b58\u653e\u4f4d\u7f6e')),
                ('prescription_crate_date', models.DateTimeField(null=True, verbose_name='\u521b\u5efa\u65f6\u95f4', blank=True)),
                ('prescription_update_date', models.DateTimeField(null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', blank=True)),
                ('prescription_test_1', models.CharField(max_length=255, null=True, blank=True)),
                ('prescription_test_2', models.CharField(max_length=255, null=True, blank=True)),
                ('prescription_test_3', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u5904\u65b9\u5355',
                'verbose_name_plural': '\u5904\u65b9\u5355',
            },
        ),
        migrations.AddField(
            model_name='medicine',
            name='prescription_idx_id',
            field=models.ForeignKey(verbose_name='\u5904\u65b9\u5355\u540d\u5b57', to_field='prescription_idx_id', blank=True, to='P.Prescription', null=True),
        ),
    ]
