from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

import uuid

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = ("Пользователь"))
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = ("Корзину")
        verbose_name_plural = ("Корзины")


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name = ("Наименование продукта"))
    price = models.DecimalField(max_digits=30, decimal_places=2, verbose_name = ("Цена"))
    img = models.ImageField(verbose_name = ("Изображение"), upload_to='products/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name = ("Категория"))
    is_sold = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)
    
    
    # def save(self, *args, **kwargs):
    #     related_objects = ProductDetail.objects.filter(product=self)
    #     self.quantity = related_objects.count()
    #     super().save(*args, **kwargs)

        
    def __str__(self):
        return f'{self.name}'
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.img.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
    
    class Meta:
        verbose_name = ("Продукт")
        verbose_name_plural = ("Продукты")


class Basket_product(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, verbose_name = ("Корзина пользователя"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name = ("Наименование продукта"))
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.basket} {self.product}'
    
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


class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name = ("Продукт"))
    login = models.CharField(max_length=128, verbose_name = ("Логин"))
    password = models.CharField(max_length=128, verbose_name = ("Пароль"))
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = ("Информацию о продукте")
        verbose_name_plural = ("Информация о продуктах")
        
        
class Order(models.Model):
    STATUS_CHOICES = [
        ('created', 'Created'),
        ('processing', 'Processing'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
        ('error', 'Error'),
    ]
    
    order_number = models.UUIDField(default = uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=128, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created')


    def __str__(self):
        return str(self.order_number)


class PurchaseHistory(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    details = models.ManyToManyField(ProductDetail)

    
class SpecialOffer(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256, blank=True)
    img = models.ImageField(verbose_name = ("Изображение"))
    
    def __str__(self):
        return self.title
    
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(verbose_name = ("Изображение"))
    bio = models.TextField()
    
    def __str__(self) -> str:
        return self.user.username