from rest_framework.decorators import api_view
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.shortcuts import render
from .apps import AppConfig

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json


#Filter Function takes json file and outputs specefied information
@csrf_exempt
@api_view(['POST'])
def get(request):
        if request.method == 'POST':
            #Checking for wrong json input
            try:
                params = json.loads(request.body.decode("utf-8"))
            except Exception as e:
                return JsonResponse({"Status code": 401, "Status message": "Invalid JSON data"},safe=False)

            # filter from the file
            with open('/home/ubuntu/new/Django_user_management/apiTest/deploy/fb/user_data.json', 'r') as myfile:
                data=myfile.read()

            # parse file
            obj = json.loads(data)

            #checking if all fields are empty
            bool_val = all(value == "empty" for value in params.values())

            #Retuening all the records if its all empty
            if bool_val:
                response = obj

            #Returning JSON response
                return JsonResponse(response,safe=False)
            #Filtering based on recieved data
            else:
                params_updated = dict((k, v) for k, v in params.items() if v=="empty")
                list_return = []
                for individual_dict in obj:
                    if all(individual_dict.get(key, None) == val for key, val in params.items()):
                        list_return.append(individual_dict)

                return JsonResponse( {"Match Found List":list_return},safe=False)
@csrf_exempt
@api_view(['POST'])
def upload(request):
        if request.method == 'POST':
            #Checking for wrong json input
            try:
                params = json.loads(request.body.decode("utf-8"))
            except Exception as e:
                return JsonResponse({"Status code": 401, "Status message": "Invalid JSON data"},safe=False)

            # filter from the file
            with open('/home/ubuntu/new/Django_user_management/apiTest/deploy/fb/user_data.json', 'r') as myfile:
                data=myfile.read()

            # parse file
            obj = json.loads(data)

            #checking if all fields are empty
            bool_val = all(value == "empty" for value in params.values())

            #Retuening all the records if its all empty
            if bool_val:
                response = obj

            #Returning JSON response
                return JsonResponse(response,safe=False)
            #Filtering based on recieved data
            else:
                params_updated = dict((k, v) for k, v in params.items() if v=="empty")
                list_return = []
                for individual_dict in obj:
                    if all(individual_dict.get(key, None) == val for key, val in params.items()):
                        list_return.append(individual_dict)

                return JsonResponse( {"Match Found List":list_return},safe=False)