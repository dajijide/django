# Generated by Django 3.2.15 on 2022-09-17 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_auto_20220917_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='wife',
            name='age',
            field=models.IntegerField(null=True, verbose_name='年龄'),
        ),
    ]
