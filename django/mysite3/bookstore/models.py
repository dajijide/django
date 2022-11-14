from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30,unique=True,verbose_name='书名')  # varchar(30)
    price = models.DecimalField(decimal_places=2,max_digits=7,verbose_name='定价',default=8888)  # Decimal(7,2)
    pub = models.CharField(max_length=50,verbose_name='出版社',null=True)
    market_price = models.DecimalField(decimal_places=2,max_digits=7,default='9999',verbose_name='市场价')

    def __str__(self):
        return "书名:" + self.title

class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(verbose_name='年龄',default=1)
    email = models.EmailField(verbose_name='邮箱',null=True,default='xxx@yyy.zzz')

    def __str__(self):
        return "作者: " + self.name

class Wife(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄',null=True)
    author = models.OneToOneField(Author,on_delete=models.CASCADE)
