from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import *
from .serializers import *
from .permissions import *
from .pagination import *

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [AdminOrReadonly]
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #search filtering
    # filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    # search_fields = ['name', 'description']
    #order filtering
    #filter_backends = [filters.OrderingFilter]
    #ordering_fields = ['price']
    #pagination_class=ProductPagination
    # pagination_class=ProductLimitOffsetPagination
    pagination_class=ProductCursorPagination
    
class ProductReview_ViewSet(viewsets.ModelViewSet):
    #permission_classes = [ReviewerOrReadOnly]
    #permission_classes = [IsAuthenticatedOrReadOnly, ReviewerOrReadOnly]
    permission_classes = [ReviewerOrReadOnly]
    #permission_classes = [IsAuthenticated]
    queryset=ProductReview.objects.all()
    serializer_class=ProductReviewSerializer
    # def get_queryset(self):
    #     queryset = ProductReview.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is not None:
    #         queryset = queryset.filter(user__username__icontains=username) #icontains- avoid case sensitivity
    #     return queryset
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['rating']
    # #filter_backends = [DjangoFilterBackend]
    # # filterset_fields = ['user__username',]
    # #filterset_fields = ['rating','product']
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['rating']
    filterset_fields = ['user__username', 'rating', 'product']