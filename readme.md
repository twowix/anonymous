가장 바깥 경로에 env.json 이라는 파일 생성 후  
내부에 하단의 json 형식에 맞춰 작성!

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