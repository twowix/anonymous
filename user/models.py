from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser

# 필수! 커스텀 유저 생성시 settings 에 사용 유저 모델을 정의

# AbstractUser
# - django 기본 유저 모델 (이것저것 많이 포함되어있음, 각종 필드, 각종 함수(유저생성, 유저인증 등등))
class User(AbstractUser):
    nickname = models.CharField(max_length=30, null=True)

    class Meta:
        db_table='user'


# AbstractBaseUser 
# - django 최소 유저 모델 (필드:비밀번호, 마지막로그인, 활성여부 3가지만 존재, 최소한의 함수만 존재)
# - 따라서, 로그인시 필요한 필드 등 많은 부분이 커스텀가능
# class User(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     nickname = models.CharField(max_length=30, null=True)

#     USERNAME_FIELD = 'email' # 로그인시 사용할 필드
#     REQUIRED_FIELDS = []

#     class Meta:
#         db_table='user'

