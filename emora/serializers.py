from rest_framework import serializers

from .models import UsersEmora, ProductsEmora, SaleOrderEmora, PurchaseEmora

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersEmora
        fields = (
            'id',
            'pk',
            'first_name',
            'last_name', 
            'login', 
            'email',   
            'tel',
            'address',
            'avatar', 
            'connected', 
            'password',
            'type',
            )
        extra_kwargs = {
            'last_name': {'required': False}
            }

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsEmora
        fields = (
            'id',
            'pk',
            'owner_id',
            'name', 
            'category', 
            'description',   
            'priceUi',
            'disponibilite',
            'stock', 
            )
        extra_kwargs = {
            'last_name': {'required': False}
            }
        unique_together = ['owner_id', 'id']
        ordering = ['id']

class SaleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrderEmora
        fields = [
            'id',
            'pk',
            'ref', 
            'owner_id',
            'category', 
            'description',   
            'amount_total',
            'disponibilite',
            'product_ids', 
            'state'
        ]


class PurchaseSerializer(serializers.ModelSerializer):
    user_owner_cart_id = UsersSerializer(many=True, read_only=True)
    class Meta:
        model = PurchaseEmora
        fields = [
            'id',
            'pk',
            'ref', 
            'owner_id',
            'category', 
            'purchase_id', 
            'user_owner_cart_id',  
            'amount_total',
            'product_ids', 
            'state'
        ]

        
        
    