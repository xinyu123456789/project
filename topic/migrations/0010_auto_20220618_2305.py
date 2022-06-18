# Generated by Django 3.1.4 on 2022-06-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0009_topic_road'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='classes',
            field=models.IntegerField(choices=[(0, '未選擇'), (1, '高中'), (2, '高職'), (3, '五專'), (3, '綜高')], default=0, verbose_name='類別'),
        ),
    ]
