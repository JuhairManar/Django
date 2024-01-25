from rest_framework import serializers,viewsets
from .models import Product,ProductReview
from django.contrib.auth.models import User

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'