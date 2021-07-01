from django.db import models

class UsersEmora(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    login = models.CharField(max_length=120)
    description = models.TextField()
    connected = models.BooleanField(default=False)
    type =  models.CharField(max_length=120)
    tel =  models.CharField(max_length=13)
    email =  models.CharField(max_length=120)
    password =  models.CharField(max_length=120)
    address =  models.CharField(max_length=130)
    avatar =  models.BinaryField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class ProductsEmora(models.Model):
    owner_id = models.ForeignKey(UsersEmora, related_name='user_owner_id', on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    description = models.TextField()
    priceUi =  models.DecimalField(max_digits=9, decimal_places=3)
    disponibilite =  models.BooleanField(default=False)
    state =  models.CharField(max_length=120)
    stock =  models.CharField(max_length=130)
    images =  models.BinaryField()
    
    def __str__(self):
        return "{} - {}".format(self.name, self.category)

class SaleOrderEmora(models.Model):
    owner_id = models.ForeignKey(UsersEmora, related_name='user_order_id', on_delete=models.CASCADE)
    ref = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    description = models.TextField()
    disponibilite =  models.BooleanField(default=False)
    state =  models.CharField(max_length=120)
    amount_total =  models.DecimalField(max_digits=9, decimal_places=3)
    product_ids = models.ManyToManyField(ProductsEmora, related_name="products_list", blank=True)
    
    def __str__(self):
        return "{} - {}".format(self.ref, self.category)

class PurchaseEmora(models.Model):
    owner_id = models.ForeignKey(UsersEmora, related_name='user_owner_cart_id', on_delete=models.CASCADE)
    ref = models.CharField(max_length=120)
    purchase_id =  models.ForeignKey(UsersEmora, related_name='user_purchase_id', on_delete=models.CASCADE, default=None)
    category = models.CharField(max_length=120)
    state =  models.CharField(max_length=120)
    amount_total =  models.DecimalField(max_digits=9, decimal_places=3)
    product_ids = models.ManyToManyField(ProductsEmora, related_name="products_list_cart", blank=True)
    
    def __str__(self):
        return "{} - {}".format(self.ref, self.owner_id)

