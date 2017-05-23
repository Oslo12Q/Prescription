#!/usr/bin/python
#-*- coding: UTF-8 -*- 
#coding=utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('1234')
