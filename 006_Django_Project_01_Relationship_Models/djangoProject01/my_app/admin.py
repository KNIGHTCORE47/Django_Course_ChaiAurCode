from django.contrib import admin
from .models import Different_Chais, Product_Review, Product_Certificate, Store

# Register your models here.

class Product_ReviewInline(admin.TabularInline):
    model = Product_Review
    extra = 2

class Different_ChaisAdmin(admin.ModelAdmin):
    list_display = ('name', 'chai_type', 'current_time')
    inlines = [Product_ReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('product_varieties',)


class Product_CertificateAdmin(admin.ModelAdmin):
    list_display = ('product', 'certificate_number', 'issued_date', 'expiration_date')

admin.site.register(Different_Chais, Different_ChaisAdmin)
admin.site.register(Product_Certificate, Product_CertificateAdmin)
admin.site.register(Store, StoreAdmin)

