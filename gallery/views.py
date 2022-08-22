from .models import Photo, Category
from .serializers import CategorySerializer, PhotoSerializer
from rest_framework import generics
import django_filters.rest_framework

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all().order_by("-id")
    serializer_class = CategorySerializer

class PhotoList(generics.ListAPIView):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        id = self.kwargs['category_id']
        return Photo.objects.filter(category=id).order_by("-id")

class TopPhotoList(generics.ListAPIView):
    queryset = Photo.objects.filter(top=True).order_by("-id")
    serializer_class = PhotoSerializer
