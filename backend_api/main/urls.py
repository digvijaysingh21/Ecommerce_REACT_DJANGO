
from django.urls import path,include
from . import views

urlpatterns = [
    path('vendors/', views.Vendorlist.as_view()),
]
