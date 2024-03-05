from django.contrib import admin

# Register your models here.

from .models import *

class OrderitemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    editable_fields = []

class OrderLogInline(admin.TabularInline):
    model = OrderLog
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'phone', 'address','division', 'district', 'area', 'total', 'created_at', 'updated_at', 'cod', 'status']
    list_filter = ['status', 'created_at', 'updated_at']
    search_fields = ['user__username', 'name', 'phone', 'address', 'division', 'district', 'total']
    inlines = [OrderitemInline, OrderLogInline]

admin.site.register(Order, OrderAdmin)