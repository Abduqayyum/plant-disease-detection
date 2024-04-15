from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('images', views.ImageModelVS, basename='images')

urlpatterns = [
    path("predict/<int:pk>", views.PredictionView.as_view(), name="prediction-view"),
    path("", views.index),
    path("", include(router.urls)),
]
