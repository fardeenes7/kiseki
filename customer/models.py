from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from product.models import *
from datetime import timedelta

class Cart(models.Model):
    user = models.ForeignKey(User, related_name='carts', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='carts', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.name
    
    def get_total(self):
        return self.product.price * self.quantity
    

class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    )
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cod = models.BooleanField(default=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pending')
    total= models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.id and self.items.all().count()>0 :
            self.total = self.get_total()
        super().save(*args, **kwargs)

    def get_total(self):
        total = 0
        for item in self.items.all():
            total += item.product.price
        return total
    
    def set_warranty(self):
        for item in self.items.all():
            try:
                item.warranty = self.logs.get(status='Delivered').created_at + timedelta(days=item.product.warranty*365)
                item.save()
            except Exception as e:
                print(e)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, related_name='order_item', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    warranty = models.DateField(blank=True, null=True)
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    )
    def __str__(self):
        return self.product.name
    
    def save(self, *args, **kwargs):
        # if self.order.status == 'Delivered':
        #     self.warranty = self.logs.filter(status='Delivered').created_at + timedelta(days=self.product.warranty*365)
        # else:
        #     self.warranty = None
        super().save(*args, **kwargs)
        if self.stock and self.stock.sold:
            if self.stock.order_item != self:
                raise Exception('Stock already sold')
        else:
            if self.stock:
                self.stock.sold = True
                self.stock.save()
        self.product.save()

class OrderLog(models.Model):
    MSG_TEMPLATE = {
        'Pending': 'Order placed successfully',
        'Processing': 'Order is being processed',
        'Shipped': 'Order has been shipped',
        'Delivered': 'Order has been delivered',
        'Cancelled': 'Order has been cancelled'
    }
    order = models.ForeignKey(Order, related_name='logs', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=Order.STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.order.name

    def save(self, *args, **kwargs):
        if not self.message:
            self.message = self.MSG_TEMPLATE[self.status]
        super().save(*args, **kwargs)
        if self.status == 'Delivered':
            self.order.set_warranty()
        self.order.status = self.status
        self.order.save()    


def get_cart_total(user):
    total = 0
    for cart in user.carts.all():
        total += cart.get_total()
    return total


User.add_to_class('get_cart_total', get_cart_total)