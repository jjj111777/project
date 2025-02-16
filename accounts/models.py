from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#회원가입 api
class User(AbstractUser):  # 🔥 AbstractUser를 상속하는 경우
    nickname = models.CharField(max_length=30, unique=True)
    
    # 🔥 related_name 충돌 해결
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # 충돌 방지
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # 충돌 방지
        blank=True
    )

    def __str__(self):
        return self.username