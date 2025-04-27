from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def Index(request):
    return HttpResponse("Welcome To My Class")


def JSON(requsest):
    return JsonResponse({"Name":"Trilo"}, safe = False)


