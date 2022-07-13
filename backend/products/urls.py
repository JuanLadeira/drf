from .views import ProductDetailAPIView, ProductListCreateAPIView
from django.urls import path


urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view()),
    path('', ProductListCreateAPIView.as_view()),

]

