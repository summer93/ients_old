# Generated by Django 2.0 on 2018-01-04 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20180104_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeform',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建日期'),
        ),
    ]
