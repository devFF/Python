from django.contrib.auth.models import User
from django.db import models
from products.models import Product


class SalesOrder(models.Model):
    """Заказ"""
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    # Связь с пользователем: many to one, много заказов у одного пользователя ForeignKey
    # Параметр on_delete -  действие при удалении
    # SET_NULL - в заказах в поле User будет пусто
    # CASCADE - удалятся все заказы от этого пользователя при его удалении
    # PROTECT - нельзя удалять пользователя пока есть заказы
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product)
