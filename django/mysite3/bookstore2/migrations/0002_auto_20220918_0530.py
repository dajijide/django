# Generated by Django 3.2.15 on 2022-09-18 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book2',
            name='title',
            field=models.CharField(max_length=30, verbose_name='书名:'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=50, verbose_name='出版社:'),
        ),
    ]