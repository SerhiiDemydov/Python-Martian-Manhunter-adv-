# Generated by Django 3.2.5 on 2021-07-31 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20210731_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='pictures_brand_logo'),
        ),
    ]
