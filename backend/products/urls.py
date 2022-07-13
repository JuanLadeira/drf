from .views import ProductDetailAPIView, ProductCreateAPIView
from django.urls import path


urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view()),
    path('', ProductCreateAPIView.as_view())
]

