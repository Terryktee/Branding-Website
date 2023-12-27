from django.db import models

# Product Model

class Product(models.Model):
    Product_Type=models.CharField(max_length=25)
    Product_Name=models.CharField(max_length=25)
    Product_Size=models.IntegerField(null=True)
    Product_Price=models.FloatField()

    def first_image(self):
        #code to determeni image
        return self.images.first() # type: ignore
    
    def __str__(self):
        return self.Product_Name

class Product_Image(models.Model):
    Product_name=models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    Product_Image=models.ImageField( upload_to="images/", max_length=None)
     
    def __img__(self):
        return self.Product_Image

class categories(models.Model):
    