from django.db import models
from django.contrib.auth.models import User


class Basket(models.Model):
    basket_product = models.ForeignKey('Basket_product', on_delete=models.CASCADE, related_name='+')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name = ("Наименование продукта"))
    price = models.DecimalField(max_digits=30, decimal_places=2, verbose_name = ("Цена"))
    # rate = models.ForeignKey('Rating', on_delete=models.CASCADE, related_name='+')
    img = models.ImageField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name = ("Категория"))
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = ("Продукт")
        verbose_name_plural = ("Продукты")


class Basket_product(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    basket = models.OneToOneField(Basket, on_delete=models.CASCADE, related_name='+')


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name = ("Наименование категории"))
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = ("Категория")
        verbose_name_plural = ("Категории")


class Product_info(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()