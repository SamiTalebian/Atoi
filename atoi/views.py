from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def atoi_post(request):
    if request.method == 'POST':
        
        return HttpResponse(request.POST)
    else :
        return HttpResponse("Wrong method!")
