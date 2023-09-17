from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .models import Doctor, Department
from .serializers import DoctorSerializer
from django.contrib.auth.models import User

# Create your views here.

@api_view(['GET'])
def doctor_lists(request): 
    """ Doctors List API

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        query = Doctor.objects.all()
        serializer = DoctorSerializer(query, many=True)
        return JsonResponse({'res':'success', 'data': serializer.data})
    
    except:
        return JsonResponse({'res': 'fail'})
    
@api_view(['GET'])
def doctor_details(request, id):
    """ Detailed View of Doctor

    Args:
        request (_type_): _description_
        id (INT): Doctor ID

    Returns:
        _type_: _description_
    """
    try:
        query = Doctor.objects.get(id=id)
        serializer = DoctorSerializer(query)
        return JsonResponse({'res':'success', 'data': serializer.data})
    
    except:
        return JsonResponse({'res': 'fail'})
    
@api_view(['POST'])
def add_doctor(request):
    """_summary_

    Args:
        request (_type_): _description_
    """
    #try:
    user = User.objects.create_user(
        username = request.data['email'],
        password = 'Doctor@123'
    )
    request.data['user'] = user
    request.data['department'] = Department.objects.get(id=request.data['department'])
    serializer = DoctorSerializer(data=request.data)
    # print(serializer.is_valid())
    # if serializer.is_valid():
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return JsonResponse({'res':'success', 'data': serializer.data})
    # else:
    #     print(user.id)
    #     user.delete()
    #     return JsonResponse({'res': 'fail', 'errors': serializer.errors})
    # except:
    #     return JsonResponse({'res': 'fail'})