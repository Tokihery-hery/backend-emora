from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import UsersEmora, ProductsEmora, SaleOrderEmora

#just commnet
@api_view(['GET', 'POST', 'DELETE'])
def getListUsers(request, pk):
    
    if request.method is 'POST':
        users = UsersEmora.objects.get(id=pk)
        serializer = UsersSerializer(users, many=False)
    else:
        users = UsersEmora.objects.all()
        serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)


class UsersList(generics.ListCreateAPIView):
        serializer_class = UsersSerializer
        queryset = UsersEmora.objects.all()


class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = UsersSerializer
        def get_queryset(self):
                queryset = UsersEmora.objects.filter(id=1)
                return queryset

#All product non filter
class ProductsList(generics.ListCreateAPIView):
        serializer_class = ProductSerializer
        queryset = ProductsEmora.objects.all()

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = ProductSerializer
        
        queryset = ProductsEmora.objects.all()


# All product filter by Owner_id
class ProductsListByUser(generics.ListCreateAPIView):
        serializer_class = ProductSerializer
        def get_queryset(self):
                queryset =ProductsEmora.objects.filter(owner_id=self.kwargs['owner_id'])
                return queryset
class ProductDetailByUser(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = ProductSerializer
        def get_queryset(self):
                queryset =ProductsEmora.objects.filter(owner_id=self.kwargs['owner_id'])
                return queryset

#sale order action
class CreateSaleOrder(generics.ListCreateAPIView):
        current_user_id =None
        serializer_class = SaleOrderSerializer
        def get_queryset(self):
                self.current_user_id = self.kwargs['owner_id']
                queryset =SaleOrderEmora.objects.filter(owner_id=self.kwargs['owner_id'])
                return queryset
        
class SaleOrderDetail(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = SaleOrderSerializer
        def get_queryset(self):
                queryset =SaleOrderEmora.objects.filter(owner_id=self.kwargs['owner_id'])
                return queryset


#Purchase action
class CreatePurchase(generics.ListCreateAPIView):
        serializer_class = PurchaseSerializer
        def get_queryset(self):
                queryset =PurchaseEmora.objects.filter(owner_id=self.kwargs['owner_id'])
                return queryset

class PurchaseDetail(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = PurchaseSerializer
        def get_queryset(self):
                queryset =PurchaseEmora.objects.filter(owner_id=self.kwargs['owner_id'])
                return queryset

