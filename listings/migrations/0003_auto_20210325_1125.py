# Generated by Django 3.1 on 2021-03-25 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210325_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='D:\\youtku\\media'),
        ),
    ]
