from django.urls import path,include
from rest_framework import routers 
from .views import *

router=routers.DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('reviews', ProductReview_ViewSet, basename='product-review')

urlpatterns = [
    path('', include(router.urls)),
    #path('api_auth/', include("rest_framework.urls")),
]