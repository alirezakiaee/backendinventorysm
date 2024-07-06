#=====urls.py=====
from django.contrib import admin
from django.urls import path, include
from users.views import UserActivationView
from users.views import UserDetailsView
from users.views import upload_file
from users.views import upload_to_s3
from django.conf import settings
from django.conf.urls.static import static
from users.views import RevenueCsvDataView ,ProductsCategoriesCsvDataView ,CompanyViewSet, CompanyLocationViewSet,SupplierViewSet,ProductCategoryViewSet,ProductDataViewSet
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register(r'company-details', CompanyViewSet, basename='company-details')
router.register(r'locations', CompanyLocationViewSet, basename='company-locations')
router.register(r'suppliers', SupplierViewSet, basename='suppliers')
router.register(r'product-categories', ProductCategoryViewSet)
router.register(r'products', ProductDataViewSet, basename='product')





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('activation/', UserActivationView.as_view({'post': 'activate'}), name='activation'),
    path('api/v1/auth/user/', UserDetailsView.as_view(), name='user-details'),
    path('upload/', upload_file, name='file-upload'),
    path('upload-to-s3/', upload_to_s3, name='upload_to_s3'),
    path('api/csv-data/', RevenueCsvDataView.as_view(), name='csv_data'),
    path('api/csv-product-categories/', ProductsCategoriesCsvDataView.as_view(), name='csv_data'),

    
    path('api/v1/auth/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
