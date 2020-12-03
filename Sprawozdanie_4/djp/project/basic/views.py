from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import CaseSerializer
from .models import Case
# Create your views here.
def case_list(request):
    if request.method=='GET':
        cases= Case.object.all()
        serializer= CaseSerializer(cases, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer = CaseSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)