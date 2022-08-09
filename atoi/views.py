from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from atoi.DTO import AtoiDTO

from atoi.interactor import AtoiInteractor

@csrf_exempt 
def atoi_post(request):
    if request.method == 'POST':
        atoi_interactor = AtoiInteractor()
        
        atoi_interactor.set_params(AtoiDTO.deserializer(data=request.POST))

        return HttpResponse(f'The result is {atoi_interactor.excute()}')
    else :
        return HttpResponse("Wrong method!")
