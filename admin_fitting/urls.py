from django.urls import path,include
from rest_framework_simplejwt.views import  TokenRefreshView 
from .views import AdminFittingViewSet
from .views import CustomTokenObtainPairView
from rest_framework.routers import DefaultRouter
from consumer.views import ProfileViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('fittings/', AdminFittingViewSet.as_view({'get': 'list'}), name='fitting-list'),
    path('', include(router.urls)),
]
