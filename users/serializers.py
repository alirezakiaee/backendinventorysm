#==== serializers.py ====
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import Document
from .models import Company, CompanyLocation ,ProductCategory ,Supplier ,ProductData

User = get_user_model()

class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "email", "first_name", "last_name" , "password"]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('file', 'uploaded_at')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'user', 'company_name', 'description', 'logo')

    def validate_user(self, value):
        # The user field should always be the currently logged-in user
        return self.context['request'].user
    
class CompanyLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyLocation
        fields = (
            'id',
            'user',
            'company',
            'location_name',
            'country',
            'city',
            'state',
            'zip_code',
            'phone',
            'email',
            'website',
            'tax',
            'address',
            'description',
        )

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'user', 'name', 'address', 'email', 'tax', 'description', 'phone')


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'value', 'percentage', 'user']
        
class ProductDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductData
        fields = '__all__'