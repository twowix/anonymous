##프로젝트 실행 방법

#### 1. 프로젝트 루트에 env.json 이라는 파일 생성 후 하단의 json 형식에 맞춰 작성!
```
{
  "SECRET_KEY": "django 비밀키!",
  "AWS_ACCESS_KEY_ID": "AWS 액세스키",  
  "AWS_SECRET_ACCESS_KEY": "AWS 비밀 키",    
  "S3_BUCKET_NAME": "AWS S3 버킷 이름",   
  "S3_ROOT_URL": "AWS S3 URL",  
  "DATABASE_NAME": "DATABASE 이름",    
  "DATABASE_HOST": "DATABASE End Point",  
  "DATABASE_USER": "Database User",  
  "DATABASE_PASSWORD": "Database 비밀번호"
}
 ```
#### 2. 가상환경 세팅
`python -m venv venv`
#### 3. 가상환경 패키지 설치
`pip install -r requirements.txt`
#### 4. 개발 서버 오픈
`python manage.py runserver 8000`
