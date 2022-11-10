from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def sendResponse(ssrequest):
    return HttpResponse('Hello, welcome to the index page.')
