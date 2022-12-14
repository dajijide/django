# Generated by Django 3.2.15 on 2022-09-17 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_auto_20220911_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(default=1, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(default='xxx@yyy.zzz', max_length=254, null=True, verbose_name='邮箱'),
        ),
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bookstore.author')),
            ],
        ),
    ]
