# Generated by Django 3.1.4 on 2022-06-18 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0010_auto_20220618_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='classes',
            field=models.IntegerField(choices=[(0, '未選擇'), (1, '高中'), (2, '高職'), (3, '五專'), (4, '綜高')], default=0, verbose_name='類別'),
        ),
    ]
