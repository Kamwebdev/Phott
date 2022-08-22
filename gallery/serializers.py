from rest_framework import serializers
from .models import Photo, Category

class PhotoSerializer(serializers.ModelSerializer):
    src = serializers.ImageField(source='thumb')

    class Meta:
        model = Photo
        fields = ('id', 'category', 'time_stamp', 'image', 'src', 'height','width')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')