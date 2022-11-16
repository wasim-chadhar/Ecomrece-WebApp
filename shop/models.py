from distutils.command.upload import upload
from email.policy import default
from itertools import product
from django.db import models

# Create your models here.

# Model for Product listing to web:
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length= 50)
    product_catageory = models.CharField(max_length= 50, default="")
    sub_product_catageory = models.CharField(max_length= 50, default="")
    product_price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length= 700)
    pub_date = models.DateField()
    image = models.ImageField(upload_to ='shop/images', default="")

    def __str__(self):
        return self.product_name

# Model for Contact User to TEAM:
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 50)
    email = models.CharField(max_length= 70)
    query_desc = models.CharField(max_length= 700)
    

    def __str__(self):
        return self.name

# Model for BUYER_Order:
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    buyer_name = models.CharField(max_length=50)
    buyer_items_json = models.CharField(max_length=5000, default="")
    buyer_phone = models.IntegerField(default=0)
    buyer_email = models.CharField(max_length=115)
    buyer_adress = models.CharField(max_length=115)
    buyer_state = models.CharField(max_length=115)
    buyer_city = models.CharField(max_length=115)
    buyer_zipCode = models.CharField(max_length=10)

# Model for Item track:
class Order_track(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.update_desc[0:10] + '...'



