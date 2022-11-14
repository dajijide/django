# Generated by Django 3.2.15 on 2022-09-11 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_auto_20220911_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='book',
            name='market_price',
            field=models.DecimalField(decimal_places=2, default='9999', max_digits=7, verbose_name='市场价'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=8888, max_digits=7, verbose_name='定价'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub',
            field=models.CharField(max_length=50, null=True, verbose_name='出版社'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=30, unique=True, verbose_name='书名'),
        ),
    ]