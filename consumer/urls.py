from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FittingViewSet, ProfileViewSet,ScheduleFittingView,ProfileUpdateSet

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'fittings', FittingViewSet, basename='fittings')

urlpatterns = [
    path('', include(router.urls)),
    path('schedule-fitting', ScheduleFittingView.as_view(),name='schedule-fitting'),
    path('update-profile', ProfileUpdateSet.as_view(),name='schedule-fitting')
]