import imghdr
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import *
import json

# Create your views here.
def create_profile(request,family_id):
    if request.method == 'POST':
        body = json.loads(request.body.decode('UTF-8'))

        new_profile = Profile.objects.create(
            family = get_object_or_404(Family, pk=family_id),
            name = body['name'],
            age = body['age'],
            phone = body['phone']
        )

        new_profile_json = {
            "id"   : new_profile.id,
            "family" : new_profile.family.name,
            "name" : new_profile.name,
            "age" : new_profile.age,
            "phone" : new_profile.phone,
            "pup_date" : new_profile.pup_date
        }

        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message" : "생성 성공!",
            "data" : new_profile_json
        })


    else:
        return JsonResponse({
            "status" : 405,
            "success" : False,
            'message' : 'method error',
            'data' : None
        })



def get_profile_all(request):
    if request.method == "GET":
        profile_all = Profile.objects.all()

        profile_json_all = []

        for profile in profile_all:
            profile_json = {
                "id"   : profile.id,
                "name" : profile.name,
                "age" : profile.age,
                "phone" : profile.phone,
                "pup_date" : profile.pup_date
            }
            profile_json_all.append(profile_json)

        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message" : "모든 프로필 수신 성공!",
            "data" : profile_json_all
        })

    else:
        return JsonResponse({
            "status" : 405,
            "success" : False,
            'message' : 'method error',
            'data' : None
        })


def get_profile(request, id):
    if request.method == "GET":
        get_profile = get_object_or_404(Profile, pk=id)
        
        profile_json = {
                "id"   : get_profile.id,
                "name" : get_profile.name,
                "age" : get_profile.age,
                "phone" : get_profile.phone,
                "pup_date" : get_profile.pup_date
        }

        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message" : "프로필 수신 성공!",
            "data" : profile_json
        })

    else:
        return JsonResponse({
            "status" : 405,
            "success" : False,
            'message' : 'method error',
            'data' : None
        })



def update_profile(request, id):
    if request.method == "PATCH":
        body = json.loads(request.body.decode('utf-8'))

        
        update_profile = get_object_or_404(Profile, pk=id)
        update_profile.name = body['name']
        update_profile.age = body['age']
        update_profile.phone = body['phone']
        update_profile.save()

        update_profile_json={
            "id"       : update_profile.id,
            "name"     : update_profile.name,
            "age"      : update_profile.age,
            "phone"    : update_profile.phone,
            "pup_date" : update_profile.pup_date
        }

        return JsonResponse({
            'status' : 200,
            'success' : True,
            'message' : '업데이트 성공!',
            'data' : update_profile_json
        })
    
    else:
        return JsonResponse({
            'status' : 405,
            'success' : False,
            'message' : 'method error',
            'data' : None
        })



def delete_profile(request, id):
    if request.method == 'DELETE':
        delete_profile = get_object_or_404(Profile,pk=id)
        delete_profile.delete()
        
        return JsonResponse({
            'status':200,
            'success':True,
            'message':'삭제 성공!',
            'data':None
        })
    
    else:
        return JsonResponse({
            'status' : 405,
            'success' : False,
            'message' : 'method error',
            'data' : None
        })

def create_family(request):
    if request.method == "POST":

        body = request.POST
        img = request.FILES['thumbnail']

        new_family = Family.objects.create(
            name = body['name'],
            message = body['message'],
            thumbnail = img
        )

        new_family_json={
            "id"       : new_family.id,
            "name"     : new_family.name,
            "message"  : new_family.message,
            "thumbnail": "/medila/" + str(new_family.thumbnail)
        }

        return JsonResponse({
            'status' : 200,
            'success' : True,
            "message" : '가족 그룹 생성 성공!',
            "data" : new_family_json
        })

    else:
        return JsonResponse({
            'status' : 405,
            'success' : False,
            "message" : 'method error',
            "data" : None
        })

def get_family_all(request):
    if request.method == "GET":
        family_all = Family.objects.all()

        family_json_all = []

        for family in family_all:
            family_json = {
                "id"   : family.id,
                "name" : family.name,
                "message" : family.message,
                "thumbnail" : "/medila/" + str(family.thumbnail),
            }
            family_json_all.append(family_json)

        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message" : "모든 가족 그룹 수신 성공!",
            "data" : family_json_all
        })

    else:
        return JsonResponse({
            "status" : 405,
            "success" : False,
            'message' : 'method error',
            'data' : None
        })

def delete_family(request, id):
    if request.method == 'DELETE':
        delete_profile = get_object_or_404(Family,pk=id)
        delete_profile.delete()
        
        return JsonResponse({
            'status':200,
            'success':True,
            'message':'가족 그룹 삭제 성공!',
            'data':None
        })
    
    else:
        return JsonResponse({
            'status' : 405,
            'success' : False,
            'message' : 'method error',
            'data' : None
        })