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
    )

    subject = models.IntegerField('公/私立', default=0,choices=SUBJECT_CHOICES)
    classes = models.IntegerField('類別', default=0,choices=CLASS_CHOICES)
    content = models.TextField('內容')
    created = models.DateTimeField('上傳時間', auto_now_add=True)

    def __str__(self):
        return "{}: {}".format(self.author, self.subject)