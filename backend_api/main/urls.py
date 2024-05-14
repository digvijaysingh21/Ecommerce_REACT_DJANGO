
from django.urls import path,include
from . import views

urlpatterns = [
    path('vendors/', views.VendorList.as_view()),
    path('vendor/<int:pk>/', views.VendorDetail.as_view()),
]
