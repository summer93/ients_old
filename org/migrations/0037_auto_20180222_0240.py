# Generated by Django 2.0 on 2018-02-22 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0036_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_type',
            name='NO',
            field=models.CharField(default='0', max_length=20, verbose_name='账户类型代码'),
        ),
        migrations.AlterField(
            model_name='account_type',
            name='Name',
            field=models.CharField(max_length=20, verbose_name='账户类型名称'),
        ),
    ]
