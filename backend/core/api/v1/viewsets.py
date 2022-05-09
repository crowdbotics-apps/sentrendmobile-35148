from rest_framework import authentication
from core.models import Data
from .serializers import DataSerializer
from rest_framework import viewsets

class DataViewSet(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Data.objects.all()