from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=20)
    PWQuestList = {
        'elemenSchool':'다녔던 초등학교 이름', ''
    }
    findPWQuest = models.TextField(choices=)
'''