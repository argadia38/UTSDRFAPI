from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, OrderViewSet, OrderDetailViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserDetailView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-details', OrderDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('user-detail/', UserDetailView.as_view(), name='user-detail'),
]
