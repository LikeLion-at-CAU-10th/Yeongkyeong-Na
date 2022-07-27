from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import *
import json

# Create your views here.
def create_category(request):
    if request.method == 'POST':
        
        body = json.loads(request.body.decode('UTF-8'))

        new_category = Category.objects.create(
            title = "할일",         # body['title']
            view_auth = 0,         # body['view_auth']
            color = "#111111"      # body['color']
        )

        new_category_json = {
            "id"        : new_category.id,
            "title"     : new_category.title,
            "view_auth" : new_category.view_auth,
            "color"     : new_category.color,
            "pup_date"  : new_category.pup_date,
        }

        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message": "생성 성공!",
            "data": new_category_json,
        })

    return JsonResponse({
            "status" : 405,
            "success" : False,
            "message": "method error",
            "data": None
            
    })


def get_category_all(requests):
    if requests.method == 'GET':
        category_all = Category.objects.all() # 쿼리셋 모양

        # 이쁘게 만들기
        category_json_all=[]
        for category in category_all:
            category_json={
                "id"        : category.id,
                "title"     : category.title,
                "view_auth" : category.view_auth,
                "color"     : category.color,
                "pup_date"  : category.pup_date,
            }
            category_json_all.append(category_json) # 나중에 serializer 배우면 생략 가능한 부분!!
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'category_all 수신 성공!',
                'data': category_json_all
            })

    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
            })

def create_todo(request,category_id):
    if request.method == "POST":

        body = request.POST
        img = request.FILES['thumb_nail']

        new_todo = Todo.objects.create(
            category = get_object_or_404(Category, pk=category_id),
            content = body['content'],
            thumb_nail = img 
        )

        new_todo_json={
            "id"         : new_todo.id,
            "title"      : new_todo.content,
            "thumb_nail" : "/media/" + str(new_todo.thumb_nail),
            "is_completed" : new_todo.is_completed,
            "pup_date"   : new_todo.pup_date
        }

        return JsonResponse({
            'status' : 200,
            'success' : True,
            "message" : "투두 생성 성공!",
            'data' : new_todo_json
        })

    return JsonResponse({
        'status' : 405,
        'success' : False,
        'message' : 'method error',
        'data' : None
    })
        

