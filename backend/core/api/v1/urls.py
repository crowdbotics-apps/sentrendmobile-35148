
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import DataViewSet
router = DefaultRouter()
router.register('data', DataViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
