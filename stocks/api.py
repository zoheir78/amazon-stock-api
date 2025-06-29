from rest_framework import generics, viewsets
from .models import StockPrice, Annotation
from .serializers import StockPriceSerializer, AnnotationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .filters import StockPriceFilter


class StockPriceListView(generics.ListAPIView):
    queryset = StockPrice.objects.all()
    serializer_class = StockPriceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StockPriceFilter


# Retrieve: GET / instead of RetrieveUpdateDestroyAPIView
class StockPriceDetailView(generics.RetrieveAPIView):
    queryset = StockPrice.objects.all()
    serializer_class = StockPriceSerializer


#  POST endpoint: Add annotation
class AnnotationCreateView(generics.CreateAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer


#  GET endpoint: List annotations
class AnnotationListView(generics.ListAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer


# DELETE endpoint: Delete annotation by ID
class AnnotationDeleteView(generics.DestroyAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer


# PUT / PATCH  endpoint: Update annotation by ID
class AnnotationUpdateView(generics.UpdateAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
