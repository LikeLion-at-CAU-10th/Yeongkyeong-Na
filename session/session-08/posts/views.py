from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render

# Create your views here.
def http_response(request):
    if request.method == 'GET':
        return HttpResponse("응답")

def json_response(request):

    if request.method == "GET":
        data = {
            'name' : 'unan',
            'school' : 'CAU'
        }

        return JsonResponse(data=data)

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name') # name은 html파일의 name

        data = {
            'name' : name
        }
        
        return render(request,'index.html',context=data)

    else:
        return render(request, 'index.html')
