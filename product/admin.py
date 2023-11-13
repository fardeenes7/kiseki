from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html



class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SubcategoryInline]


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductInline]


class SpecificationInline(admin.TabularInline):
    model = Specification
    extra = 0


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class StockInline(admin.TabularInline):
    model = Stock
    extra = 0



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'subcategory', 'price', 'stock_count', 'created_at', 'updated_at', 'sn_starting', 'new_stock')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'sn_starting', 'new_stock')
    inlines = [SpecificationInline, ProductImageInline, StockInline]

    def stock_count(self, obj):
        return obj.stocks.filter(sold=False).count()
    
from customer.models import OrderItem
class InvoiceInline(admin.StackedInline):
    model = OrderItem
    extra = 0
    can_delete = False
    readonly_fields = ('order', 'product', 'warranty',)
    # set title
    verbose_name = "Invoice"
    verbose_name_plural = "Invoice"
    
class WarrantyInline(admin.StackedInline):
    model = Warranty
    extra = 0
    can_delete = False
    readonly_fields = ( 'sn', 'created_at', 'updated_at', 'warranty_link')
    # set title
    verbose_name = "Warranty"
    verbose_name_plural = "Warranty"

    #add link to warranty

    def warranty_link(self, obj):
        url = (
            reverse("admin:product_warranty_changelist")
            + str(obj.id)
        )
        return format_html('<a href="{}">View Warranty</a>', url) 

class StockAdmin(admin.ModelAdmin):
    list_display = ('sn', 'view_product_link', 'sold')
    list_filter = ('sold', )
    fields = ('sn', 'product', 'sold')
    search_fields = ('sn', 'product__name')
    inlines = [InvoiceInline, WarrantyInline]

    def invoice_link(self, obj):
        url = (
            reverse("admin:customer_order_changelist")
            + str(obj.order_item.order.id)
        )
        return format_html('<a href="{}">{}</a>', url, obj.order_item.order.id)

    def view_product_link(self, obj):
        url = (
            reverse("admin:product_product_changelist")
            + str(obj.product.id)
        )
        return format_html('<a href="{}">{}</a>', url, obj.product.name)

    view_product_link.short_description = "Product"

    

from customer.models import Order, OrderItem
class WarrantyLogInline(admin.TabularInline):
    model = WarrantyLog
    extra = 1


class WarrantyAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'customer', 'product', 'sn', 'created_at', 'updated_at')
    list_filter = ('status','created_at', 'updated_at')
    search_fields = ('id','user__username', 'product__name', 'sn')
    inlines = [WarrantyLogInline]

    def product(self, obj):
        return obj.sn.product.name
    
    def customer(self, obj):
        return Order.objects.get(items__stock__sn=obj.sn)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Warranty, WarrantyAdmin)
admin.site.register(Stock, StockAdmin)