# Generated by Django 3.2.5 on 2021-07-31 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealers', '0004_auto_20210731_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
