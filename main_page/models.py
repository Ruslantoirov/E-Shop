from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=60)
    product_desc = models.CharField(max_length=240)
    product_price = models.FloatField()
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_amount = models.IntegerField()
    product_image = models.ImageField(upload_to='media')
    product_added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_product_quantity = models.IntegerField()
    user_add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)
