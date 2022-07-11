# BE-Assingment02: CRUD(1)

## 과제
1. 지난 주 진행했던 과제 레포에 새로운 앱 profiles 추가  
2. 세션 내용을 되짚으며 profile 데이터에 관한 create&read 코드 완성(update,delete는 선택)  
3. README.md에 get 요청과 post 요청 결과 2장 이미지 첨부하여 마무리  
4. 필드(name,age 등등) 종류는 자유  
  
## 결과
### Create
데이터 3개를 생성했다.  
<img width="622" alt="create-profile" src="https://user-images.githubusercontent.com/102007066/178310007-23974396-43b5-4b05-9e5d-829e92d0e469.PNG">
<img width="622" alt="create-profile2" src="https://user-images.githubusercontent.com/102007066/178310025-104ae207-9234-427e-b007-24d882257dd8.PNG">

### Read-all
생성된 3개의 데이터를 확인할 수 있다.  
<img width="622" alt="get-profile-all" src="https://user-images.githubusercontent.com/102007066/178310055-ec04f18a-0a04-4625-ab84-79215ae0952b.PNG">

### Read-one
id가 2인 데이터를 읽어온다.  
<img width="622" alt="get-profile" src="https://user-images.githubusercontent.com/102007066/178310083-3673e417-9afc-46ee-862b-6e08dd953609.PNG">  

### Update
id가 2인 데이터의 name과 age 값을 수정했다.  
<img width="622" alt="update-profile1" src="https://user-images.githubusercontent.com/102007066/178310127-f2b1009e-5adf-4a1c-9006-572ea750b9d7.PNG">  
  
get-profile-all을 실행하면 id가 2인 데이터만 값이 변경된 것을 확인할 수 있다.  
<img width="622" alt="update-profile2" src="https://user-images.githubusercontent.com/102007066/178310134-ee0fa86d-525a-4acf-b896-bbf08de67202.PNG">  

### Delete
id가 2인 데이터만 삭제한다.  
<img width="622" alt="delete-profile1" src="https://user-images.githubusercontent.com/102007066/178310155-22220463-fe8d-4606-9093-c96cadf8f6d3.PNG">  
  
id가 2인 데이터만 삭제된 것을 확인할 수 있다.  
<img width="622" alt="delete-profile2" src="https://user-images.githubusercontent.com/102007066/178310181-dca71456-2317-4b9c-a906-e2dec249674b.PNG">
  
## 💡 과제 중 알게 된 것!
### `get_object_or_404`
1. 모델의 예외 대신 발생    
2. 만약 객체가 존재하지 않는다면, get()을 사용하여 HTTP404 예외를 발생시킴    
3. Django 모델을 첫 번째 인자로 받고, 몇 개의 키워드 인수를 모델 관리자의 get() 함수에 넘긴다.  