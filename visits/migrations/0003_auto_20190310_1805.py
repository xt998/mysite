# Generated by Django 2.0 on 2019-03-10 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0002_auto_20190310_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userip',
            name='address',
            field=models.CharField(blank=True, max_length=500, verbose_name='地址'),
        ),
    ]
