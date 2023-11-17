from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee

# Create your views here.
def employeeView(request):
    emp = {
        'id':123,
        'name':'Rahul',
        'sal':45000
    }

    data = Employee.objects.all();
    emp = list(data.values())
    response = {'employees' : emp}

    return JsonResponse(response)