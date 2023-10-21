from django.db import models

class Product(models.Model):
    pname = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

    def __str__(self):
        return self.pname


class Convo(models.Model):
    message = models.TextField()

    # class Meta:
    #     ordering = ('name',)
    #     verbose_name_plural = 'Converstaions'

    def __str__(self):
        return self.message

class Cart(models.Model):
    cartitem = models.ForeignKey(Product,on_delete= models.CASCADE)
    
    def __str__(self):
        return self.cartitem
    