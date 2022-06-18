from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 科目
class Topic(models.Model):
    SUBJECT_CHOICES = (
      (0, "未選擇"),
      (1, "公立"),
      (2, "私立")
    )
    #班級選項
    CLASS_CHOICES = (
        (0, "未選擇"),
        (1, "高中"),
        (2, "高職"),
        (3, "五專"),
        (4, "綜高"),
    )

    subject = models.IntegerField('公/私立', default=0,choices=SUBJECT_CHOICES)
    classes = models.IntegerField('類別', default=0,choices=CLASS_CHOICES)
    content = models.CharField('學校名稱',max_length = 256)
    picture = models.ImageField('照片', blank=True, null=True)
    road = models.TextField('入學方法',blank=True, null=True,max_length = 1024)
    created = models.DateTimeField('上傳時間', auto_now_add=True)
    slink1 = models.URLField('學校官網', max_length=512, null=True, blank=True)
    slink2 = models.URLField('招生參考網址', max_length=512, null=True, blank=True)
    def __str__(self):
        return self.conetent

class Location(models.Model):
    good = models.CharField(max_length = 256)