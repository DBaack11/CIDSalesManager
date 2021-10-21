from django.db import models


class Product(models.Model):
    productName = models.CharField(max_length=200)
    productNum = models.CharField(max_length=100)
    unitPrice = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)
    casePrice = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)
    quantity = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/media/ProductImages/')
    parentGroup = models.CharField(max_length=100)
    subParentGroup = models.CharField(max_length=100)
    parentProductCategory = models.CharField(max_length=100)
    subParentProductCategory = models.CharField(
        null=True, blank=True, max_length=100)

    class Meta:
        ordering = ['-parentGroup', '-subParentGroup',
                    '-parentProductCategory']

    def __str__(self):
        return self.productName
