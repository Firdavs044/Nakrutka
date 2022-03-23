
from payments.models import BasePayment
from django.db import models
from django.db.models.fields import DecimalField, related
from django.forms import IntegerField
from django.utils import timezone
from django.contrib.auth.models import User




class Website(models.Model):
    title = models.CharField('Загаловок', max_length=250, null=True)
    image = models.ImageField('Фото', upload_to='productColor gallery', blank=True)

    class Meta:
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'

    def __str__(self):
        return self.title


class Type(models.Model):
    title = models.CharField('Загаловок', max_length=250, null=True)
    website = models.ManyToManyField(Website, through="Price")
    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    def __str__(self):
        return self.title


class Price(models.Model):
    website = models.ForeignKey(Website, related_name='price_category', null=True, on_delete=models.CASCADE, verbose_name='Категоря')
    type = models.ForeignKey(Type,on_delete=models.CASCADE, null=True, related_name='price_main_category',verbose_name='Тип' )
    price = models.IntegerField('Цена',default=0)
    

    class Meta:
        verbose_name = 'price'
        verbose_name_plural = 'price'

    def __str__(self):
        return self.website.title   






class Order(models.Model):
    price = models.ForeignKey(Price,on_delete=models.SET_NULL, null=True, verbose_name='Корзина')
    quantity = models.IntegerField('Кол-во', default=0)
    total = models.IntegerField('Сумма заказа',default=0)
    link = models.TextField('Ссылка', null=True)
    status = models.BooleanField('Статус заказа', default=False)

    class Meta: 
        verbose_name = 'Заказа'
        verbose_name_plural = 'Заказы'


    def __str__(self):
        return str(self.status) 



