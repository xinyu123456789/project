# Generated by Django 3.1.4 on 2022-06-18 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0006_auto_20220618_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='照片'),
        ),
    ]
