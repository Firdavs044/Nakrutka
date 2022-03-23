from statistics import quantiles
from django.contrib import admin
from . models import  Order, Website, Type, Price

admin.site.register(Website)
admin.site.register(Type)
admin.site.register(Price)
admin.site.register(Order)
