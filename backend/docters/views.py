from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .models import Docter
from .serializers import DocterSerializer
# Create your views here.

@api_view(['GET'])
def docter_lists(request): 
    """ Docters List API

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        query = Docter.objects.all()
        serializer = DocterSerializer(query, many=True)
        return JsonResponse({'res':'success', 'data': serializer.data})
    
    except:
        return JsonResponse({'res': 'fail'})
    
@api_view(['GET'])
def docter_details(request, id):
    """ Detailed View of Docter

    Args:
        request (_type_): _description_
        id (INT): Docter ID

    Returns:
        _type_: _description_
    """
    try:
        query = Docter.objects.get(id=id)
        serializer = DocterSerializer(query)
        return JsonResponse({'res':'success', 'data': serializer.data})
    
    except:
        return JsonResponse({'res': 'fail'})
    
@api_view(['POST'])
def add_docter(request):
    """_summary_

    Args:
        request (_type_): _description_
    """
    pass