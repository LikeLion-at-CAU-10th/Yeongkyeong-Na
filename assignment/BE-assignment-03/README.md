# BE-Assingment03: CRUD(2)

## 과제
해커톤과 관련하여 자유롭게 model을 만들고 1:N 관계를 이해한다!  
  
## 과정
### <오순도순>의 1:N 관계
1. <오순도순> 서비스의 각 이용자는 한 가족 그룹에만 속할 수 있다.  
2. 한 가족 그룹은 여러 명의 이용자를 가질 수 있지만 한 이용자는 여러 가족 그룹에 속할 수 없으므로 가족 그룹(Family)와 이용자 프로필(Profile)은 1:N 관계이다. 
### Model
1. Family 모델을 생성한다. <오순도순>의 가족 그룹은 이름, 상태메시지, 대표 사진으로 이루어져있다.  
```python
class Family(models.Model):
    name = models.CharField(max_length=40,null=True,blank=True)
    message = models.CharField(max_length=90,null=True,blank=True)
    thumbnail = models.ImageField(upload_to="family/",null=True,blank=True)
```  
2. Profile이 Family를 fk로 할 수 있도록 Profile 모델을 수정한다.  
```python
class Profile(models.Model):
    family = models.ForeignKey('Family',on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20,null=True,blank=True)
    age = models.IntegerField(default=0,null=True,blank=True)
    phone = models.CharField(max_length=11,null=True,blank=True)
    pup_date = models.DateTimeField(auto_now_add=True)
```  
3. profile/urls.py에서 `create-profile`도 다음과 같이 수정했다.  
`path('create-profile/<int:family_id>', create_profile, name="create-profile"),`

  
## 결과
### Create
가족 그룹을 2개 생성했다.  
<img width="610" alt="가족 그룹 생성" src="https://user-images.githubusercontent.com/102007066/179561031-0b19ba62-be62-46f7-bedf-1b8876bdd189.PNG">  
<img width="610" alt="가족 그룹 생성 성공" src="https://user-images.githubusercontent.com/102007066/179561075-e0526730-e70e-4008-a9d2-55c40664e54c.PNG">  
<img width="610" alt="가족그룹 또 생성함" src="https://user-images.githubusercontent.com/102007066/179561094-0e3332f9-b102-4d96-b753-8b3affa7f09e.PNG">  

### Read-all
생성된 2개의 가족 그룹을 확인할 수 있다.  
<img width="610" alt="가족 불러오기 성공" src="https://user-images.githubusercontent.com/102007066/179561364-7f28c17a-6d7c-4120-96d6-f70a9a1bd9f9.PNG">  

  
## 🤔 바뀐 Profile은 어떻게 되었을까?
### Create
가족 그룹 '오순도순'에 속하도록 나의 프로필을 생성했다.
<img width="610" alt="프로필 생성" src="https://user-images.githubusercontent.com/102007066/179561845-5d45fd37-01ad-409c-8551-3a6666829024.PNG">
가족 그룹 '오순도순'에 성공적으로 들어간 것을 확인할 수 있다!😆
<img width="610" alt="프로필 생성 성공" src="https://user-images.githubusercontent.com/102007066/179562508-6d9fc0d0-7a6e-4723-9230-61bad4dc1df2.PNG">