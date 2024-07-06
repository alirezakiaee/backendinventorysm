from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
from .models import Company, CompanyLocation ,Supplier , ProductCategory, ProductData



# Register your models here.
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser','id']
    list_display_links = ['email', 'first_name', 'last_name']
    list_filter = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions and groups'), {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),  # Removed 'date_joined'
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'first_name', 'last_name','email', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'company_name', 'description', 'logo')
    list_filter = ('company_name',)
    search_fields = ('company_name', 'description')
class CompanyLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'description', 'logo')
    list_filter = ('company_name',)
    search_fields = ('company_name', 'description')
@admin.register(CompanyLocation)
class CompanyLocationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'location_name',
        'company',
        'country',
        'city',
        'state',
        'zip_code',
        'phone',
        'email',
        'website',
        'tax',
        'address',
    )
    list_filter = ('company',)
    search_fields = ('location_name', 'company__company_name')
admin.site.register(User, UserAdmin)
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'address', 'email', 'tax', 'description', 'phone')
    
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'percentage', 'user')
    
@admin.register(ProductData)
class ProductDataAdmin(admin.ModelAdmin):
    list_display = ('name',        'description',        'sku',        'manufacturer_name',        'cost',        'price',        'unit',        'size_quantity_per_carton',        'company',        'location',        'category',        'supplier',        'user',        'barcodeValue',    )
    list_filter = (
        'company',
        'location',
        'category',
        'supplier',
        'user',
    )
    search_fields = (
        'name',
        'description',
        'sku',
        'manufacturer_name',
        'barcodeValue',
    )