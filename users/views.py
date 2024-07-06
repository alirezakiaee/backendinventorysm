#=====views.py=====
from django.shortcuts import render
from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from rest_framework import status, authentication, permissions, generics, parsers
from rest_framework.response import Response
from .serializers import UserSerializer
import pandas as pd
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view, parser_classes
from .dc import data_quality_report  # Import your data processing function
import numpy as np
from django.http import JsonResponse
import json
import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import boto3
from django.views.decorators.csrf import csrf_exempt
import environ
import csv
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.conf import settings
import boto3
import uuid
from rest_framework import status
from rest_framework import viewsets
from django.views import View
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Company, CompanyLocation ,Supplier ,ProductCategory ,ProductData
from .serializers import CompanySerializer, CompanyLocationSerializer ,SupplierSerializer ,ProductCategorySerializer,ProductDataSerializer




# Create your views here.
class UserActivationView(UserViewSet):
    def activate(self, request):
        uid = request.data.get('uid')
        token = request.data.get('token')
        if not uid or not token:
            return Response({'error': 'UID and token are required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = get_user_model().objects.get(pk=uid)
        except get_user_model().DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        if not user.is_active:
            user.is_active = True
            user.save()
            return Response({'success': 'User activated successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User is already active.'}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailsView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    authentication_classes = (authentication.BasicAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_file(request):
    try:
        file_obj = request.FILES['file']
        df = pd.read_csv(file_obj)  # Read the CSV file directly into a DataFrame
        report_results = data_quality_report(df)  # Get the data quality report

        # Convert report_results to a JSON-compatible dictionary
        json_compatible_report = {
            key: (float(val) if isinstance(val, np.int64) else val)
            for key, val in report_results.items()
        }

        return JsonResponse(json_compatible_report, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def upload_to_s3(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        s3_client = boto3.client('s3', region_name=os.environ.get('YOUR_REGION'), aws_access_key_id=os.environ.get('YOUR_ACCESS_KEY_ID'), aws_secret_access_key=os.environ.get('YOUR_SECRET_ACCESS_KEY'))

        try:
            s3_client.upload_fileobj(file, os.environ.get('YOUR_BUCKET_NAME'), file.name)
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

class RevenueCsvDataView(View):
    def get(self, request):
        # Configure AWS SDK
        aws_access_key_id = os.environ.get('YOUR_ACCESS_KEY_ID')
        aws_secret_access_key = os.environ.get('YOUR_SECRET_ACCESS_KEY')
        aws_region = os.environ.get('YOUR_REGION')

        s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region,
        )

        try:
            # Get CSV file from S3 bucket
            s3_object = s3_client.get_object(
                Bucket=os.environ.get('RESULTS_BUCKET_NAME'),
                Key='Total_Revenue.csv',
            )
            csv_string = s3_object['Body'].read().decode('utf-8')

            # Parse CSV string using csv module
            csv_data = list(csv.DictReader(csv_string.splitlines()))

            return JsonResponse(csv_data, safe=False)

        except Exception as e:
            print(f"Error fetching CSV data: {e}")
            return JsonResponse({'error': 'Failed to fetch CSV data'}, status=500)
class ProductsCategoriesCsvDataView(View):
    def get(self, request):
        # Configure AWS SDK
        aws_access_key_id = os.environ.get('YOUR_ACCESS_KEY_ID')
        aws_secret_access_key = os.environ.get('YOUR_SECRET_ACCESS_KEY')
        aws_region = os.environ.get('YOUR_REGION')

        s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region,
        )

        try:
            # Get CSV file from S3 bucket
            s3_object = s3_client.get_object(
                Bucket=os.environ.get('RESULTS_BUCKET_NAME'),
                Key='Product_Categories_ActualvsForecast.csv',
            )
            csv_string = s3_object['Body'].read().decode('utf-8')

            # Parse CSV string using csv module
            csv_data = list(csv.DictReader(csv_string.splitlines()))

            return JsonResponse(csv_data, safe=False)

        except Exception as e:
            print(f"Error fetching CSV data: {e}")
            return JsonResponse({'error': 'Failed to fetch CSV data'}, status=500)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        user = self.request.query_params.get('user')
        if user:
            return Company.objects.filter(user_id=user)
        else:
            return Company.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CompanyLocationViewSet(viewsets.ModelViewSet):
    queryset = CompanyLocation.objects.all()
    serializer_class = CompanyLocationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.query_params.get('user')
        if user:
            return CompanyLocation.objects.filter(user_id=user)
        else:
            return CompanyLocation.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    
class ProductDataViewSet(viewsets.ModelViewSet):
    queryset = ProductData.objects.all()
    serializer_class = ProductDataSerializer