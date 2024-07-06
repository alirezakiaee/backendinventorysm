#=====models.py=====
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.contrib.auth.models import User

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email
    def id (self):
        return self.id

    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)

    def __str__(self):
        return self.company_name

class CompanyLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    location_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    tax = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.location_name} - {self.user}"
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        
class Supplier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    tax = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.user}" 


class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class ProductData(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.ForeignKey(CompanyLocation, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    sku = models.CharField(max_length=100)
    manufacturer_name = models.CharField(max_length=100)
    cost = models.FloatField()
    price = models.FloatField()
    unit = models.CharField(max_length=10)
    size_quantity_per_carton = models.IntegerField()
    image = models.ImageField(upload_to='product_images/' ,null=True, blank=True)
    user = models.CharField(max_length=100)
    barcodeValue = models.CharField(max_length=2000)