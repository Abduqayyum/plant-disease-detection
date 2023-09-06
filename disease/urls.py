from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('images', views.ImageModelVS, basename='images')

urlpatterns = [
    path("predict/<int:pk>", views.PredictionView.as_view(), name="prediction-view"),
    path("", include(router.urls)),
    # path("upload/", views.ImageView.as_view(), name="upload-view"),
    # path("upload/", views.image_view, name="image-view"),
    path("index/", views.index, name="home-view"),
]