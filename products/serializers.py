from rest_framework import fields, serializers
from .models import Product


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'productName', 'productNum', 'unitPrice', 'casePrice', 'quantity',
                  'description', 'image', 'parentGroup', 'subParentGroup', 'parentProductCategory', 'subParentProductCategory']
