from django.contrib import admin
from .models import Product,Product_Image


#modifying the site admin page

admin.site.site_header='Genesis Gear Online Shop'
admin.site.site_title='Genesis Gear'
admin.site.index_title='Welcome to Genesis Gear'
# Register your models here.

class ProductImageAdmin(admin.TabularInline):
    model=Product_Image
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Produt Type',{'fields': ['Product_Type']}),
        ('Product Name',{'fields':['Product_Name']}),
        ('Product Size',{'fields':['Product_Size']}),
        ('Product Price',{'fields':['Product_Price'],'classes':'collapse'}),
    ]

    inlines=[ProductImageAdmin]

    list_display=('Product_Type','Product_Name','Product_Size','Product_Price')

admin.site.register(Product,ProductAdmin)
#admin.site.register(Product_Image)
