from .views import ProductDetailAPIView, ProductListCreateAPIView, ProductUpdateAPIView, ProductDestroyAPIView
from django.urls import path


urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view()),
    path('<int:pk>/update', ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete', ProductDestroyAPIView.as_view()),
    path('', ProductListCreateAPIView.as_view()),

]

 