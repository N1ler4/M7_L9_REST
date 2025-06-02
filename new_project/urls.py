from django.urls import path
from .views import WordViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'word', WordViewSet, basename='words')

urlpatterns = router.urls