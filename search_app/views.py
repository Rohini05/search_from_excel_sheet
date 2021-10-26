from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import csv
import json
import re

@api_view(['GET'])
def exceltoJsonData(request):
    data={}
    with open('search_app/python_assesment.csv') as csv_file:
        csvReader= csv.DictReader(csv_file)
        for rows in csvReader:
            name = rows['name']
            data[name]=rows
    with open('python_list.json', 'w') as json_file:
        json.dump(list(data), json_file)
    return Response("done")
 
@api_view(['GET'])
def searchJsonData(request):
    word =  request.GET.get('word')
    f = open('search_app/python_list.json',)
    data = json.load(f)
    result=[]
    for i in data:
        if re.search(word, i,flags=re.IGNORECASE):
            result.append(i)
    return Response(result)
 


 
@api_view(['GET'])
def searchExcelSheetData(request):
    word =  request.GET.get('word')
    result=[]
    with open('search_app/python_assesment.csv') as csv_file:
        csvReader= csv.DictReader(csv_file)
        for rows in csvReader:
            if re.search(word,  rows['name'],flags=re.IGNORECASE):
                result.append(rows['name'])
    return Response(result)
 