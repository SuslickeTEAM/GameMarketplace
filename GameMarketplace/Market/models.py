from django.db import models
from django.contrib.auth.models import User


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = ("Пользователь"))
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = ("Корзину")
        verbose_name_plural = ("Корзины")


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name = ("Наименование продукта"))
    price = models.DecimalField(max_digits=30, decimal_places=2, verbose_name = ("Цена"))
    # rate = models.ForeignKey('Rating', on_delete=models.CASCADE, related_name='+')
    img = models.ImageField(verbose_name = ("Изображение"))
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name = ("Категория"))
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = ("Продукт")
        verbose_name_plural = ("Продукты")


class Basket_product(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, verbose_name = ("Корзина пользователя"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name = ("Наименование продукта"))
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.basket}'
    
    class Meta:
        verbose_name = ("Корзину продуктов")
        verbose_name_plural = ("Корзина продуктов")

   
class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name = ("Наименование категории"))
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = ("Категория")
        verbose_name_plural = ("Категории")


class Product_info(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name = ("Продукт"))
    title = models.CharField(max_length=128, verbose_name = ("Заголовок"))
    description = models.CharField(max_length=128, verbose_name = ("Описание"))

    def __str__(self):
        return f'{self.title}/{self.product}'
    
    class Meta:
        verbose_name = ("Информацию о продукте")
        verbose_name_plural = ("Информация о продуктах")