from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100) 

# 修正: Djangoのmake_passwordを使って暗号化
# from django.contrib.auth.hashers import make_password

# class User(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)

#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)
