from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def http_response(request):
    if request.method == "GET":
        return HttpResponse("응답했어요")

def json_response(request):
    if request.method == "GET":
        data = {
            'name' : 'Yeongkyeong',
            'school' : "CAU"
        }

        return JsonResponse(data=data)

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        data = {
            'name' : name
        }

        return render(request, 'index.html', context=data)
    
    else:
        return render(request, 'index.html')