from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 科目
class Topic(models.Model):
    # 支出類別選項
    SUBJECT_CHOICES = (
      (0, "未選擇"),
      (1, "數學"),
      (2, "國文"),
      (3, "英文"),
      (4, "歷史"),
      (5, "地理"),
      (6, "公民"),
      (7, "物理"),
      (8, "化學"),
      (9, "生物"),
      (10, "音樂"),
      (11, "美術"),
      (12, "國防教育"),
      (13, "健護"),
      (14, "體育"),
    )
    #班級選項
    CLASS_CHOICES = (
        (0, "未選擇"),
        (1, "101"),
        (2, "102"),
        (3, "103"),
        (4, "104"),
        (5, "105"),
        (6, "106"),
        (7, "107"),
        (8, "108"),
        (9, "109"),
        (10, "110"),
        (11, "201"),
        (12, "202"),
        (13, "203"),
        (14, "204"),
        (15, "205"),
        (16, "206"),
        (17, "207"),
        (18, "208"),
        (19, "209"),
        (20, "210"),
        (21, "301"),
        (22, "302"),
        (23, "303"),
        (24, "304"),
        (25, "305"),
        (26, "306"),
        (27, "307"),
        (28, "308"),
        (29, "309"),
        (30, "310"),
    )

    subject = models.IntegerField('科目', default=0,choices=SUBJECT_CHOICES)
    classes = models.IntegerField('班級', default=0,choices=CLASS_CHOICES)
    content = models.TextField('教學計劃')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField('上傳時間', auto_now_add=True)

    def __str__(self):
        return "{}: {}".format(self.author, self.subject)