from django.db import models
from django.db.models.fields import SlugField
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User
from django.db import transaction

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    

class Subcategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to="subcategory/", blank=True, null=True)

    def __str__(self):
        return self.name
    

from django.core.validators import RegexValidator

hexadecimal_validator = RegexValidator(
    regex='^[0-9a-fA-F]*$',
    message='Enter a valid hexadecimal number.',
    code='invalid_hexadecimal'
)

class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to="product/", blank=True, null=True)
    description = CKEditor5Field('Text', config_name='extends')
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sn_starting = models.CharField(max_length=16, validators=[hexadecimal_validator], blank=True, null=True)
    new_stock = models.IntegerField()
    warranty = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    
    def get_all_image(self):
        images = [self.image]
        for image in self.images.all():
            images.append(image.image)
        print(images)
        return images

    def stock(self):
        return self.stocks.filter(sold=False).count()
    
    def save(self, *args, **kwargs):
        if self.new_stock > 0 and self.sn_starting:
            super().save(*args, **kwargs)
            self.generate_stock(self.sn_starting, self.new_stock)
            self.new_stock = 0
            self.sn_starting = None
            self.save()
        else:
            super().save(*args, **kwargs)

    def generate_stock(self, current_hexadecimal, stock):
        print("Generating stock")
        try:
            # Convert the current_hexadecimal to an integer, increment it, and convert it back to hexadecimal
            current_integer = int(current_hexadecimal, 16)
            next_hexadecimal_numbers = []
            for _ in range(stock):
                print("Generating sn ")
                next_integer = current_integer + 1
                if next_integer > 0xFFFFFFFFFFFFFFFF:  # Handle overflow
                    break
                next_hexadecimal = format(next_integer, 'x')
                next_hexadecimal_numbers.append(next_hexadecimal)
                # create stock
                current_integer = next_integer
            print(next_hexadecimal_numbers, len(next_hexadecimal_numbers))
            with transaction.atomic():
                for hexa in next_hexadecimal_numbers:
                    print(f'SN: {hexa}')
                    Stock.objects.create(product=self, sn=hexa)
        except Exception as e:
            print(e)
        return
    
class Stock(models.Model):
    product = models.ForeignKey(Product, related_name='stocks', on_delete=models.CASCADE)
    sn = models.CharField(max_length=16, validators=[hexadecimal_validator])
    sold = models.BooleanField(default=False)
    verify_count = models.IntegerField(default=0)

    def __str__(self):
        return f'#{self.sn}- {self.product.name}'
    

class Specification(models.Model):
    product = models.ForeignKey(Product, related_name='specifications', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}: {self.value}'
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product/", blank=True, null=True)

    def __str__(self):
        return self.product.name
    

class ProductReview(models.Model):
    user  = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.product.name
    

class Warranty(models.Model):
    STATUS_CHOICES = (
        ('Received', 'Received'),
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Ready for Delivery', 'Ready for Delivery'),
    )
    sn = models.ForeignKey(Stock, related_name='warranties', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Select')

    def __str__(self):
        return f'#{self.id}- {self.sn.product.name}'

class WarrantyLog(models.Model):
    STATUS_CHOICES = (
        ('Received', 'Received'),
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Ready for Delivery', 'Ready for Delivery'),
        ('Delivered', 'Delivered'),
    )
    MSG_TEMPLATE = {
        'Received': 'Product received.',
        'Processing': 'Product warranty in the process.',
        'Ready for Delivery': 'Product is ready for delivery.',
        'Shipped': 'Order has been shipped',
        'Delivered': 'Product has been delivered',
    }
    warranty = models.ForeignKey(Warranty, related_name='logs', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pending')
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.message:
            self.message = self.MSG_TEMPLATE[self.status]
        super().save(*args, **kwargs)

        self.warranty.status = self.status
        self.warranty.save()