from django.urls import path
from . import views

urlpatterns = [
    path('api/categories/', views.CategoryList.as_view()),
    path('api/photos/<category_id>/', views.PhotoList.as_view()),
    path('api/top/', views.TopPhotoList.as_view()),
]