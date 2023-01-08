from django.db import models
from django.contrib.auth.models import User


class Basket(models.Model):
    basket_product = models.ForeignKey('Basket_product', on_delete=models.CASCADE, related_name='+', verbose_name = ("Наименование продукта"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = ("Пользователь"))

    def __str__(self):
        return f'{self.name}'
    
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
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name = ("Наименование продукта"))
    basket = models.OneToOneField(Basket, on_delete=models.CASCADE, related_name='+', verbose_name = ("Корзина пользователя"))
    def __str__(self):
        return f'{self.name}'
    
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
        return f'{self.name}'
    
    class Meta:
        verbose_name = ("Информацию о продукте")
        verbose_name_plural = ("Информация о продуктах")


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = ("Пользователь"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name = ("Продукт"))
    rate = models.PositiveIntegerField(verbose_name = ("Рейтинг"))

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = ("Рейтинг")
        verbose_name_plural = ("Рейтинги")