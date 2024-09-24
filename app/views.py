from django.shortcuts import render
from .models import ProductType,Product,Purchase,Department,Vendor,Sales,Customer
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductTypeSerializer,ProductSerializer,PurchaseSerializer,VendorSerializer,DepartmentSerializer,SalesSerializer,CustomerSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# Create your views here.
class ProductTypeApiView(ModelViewSet):
    queryset=ProductType.objects.all()
    serializer_class=ProductTypeSerializer
    
class ProductApiView(GenericAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    
    def get(self,request):
        product_objs=self.get_queryset()
        serializer = ProductSerializer(product_objs,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data created.')
        else:
            return Response(serializer.errors)
        
class PurchaseApiView(ModelViewSet):
    queryset=Purchase.objects.all()
    serializer_class=PurchaseSerializer
    
class DepartmentApiView(ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    
class VendorApiView(ModelViewSet):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer
    
class SalesApiView(ModelViewSet):
    queryset=Sales.objects.all()
    serializer_class=SalesSerializer
    
class CustomerApiView(ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer