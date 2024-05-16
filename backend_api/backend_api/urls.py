
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views

# http post http://127.0.0.1:8000/api/token/ username=admin password=admin
'''
http  http://127.0.0.1:8000/api/vendors/ "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1Nzc2NTk2LCJpYXQiOjE3MTU3NzYyOTYsImp0aSI6IjA1MGNjZmU0Mzc1MjQ0NDU5MDhjYWE4ZWYyZGM3Y2Q2IiwidXNlcl9pZCI6MX0.fM0ly9KTOIuC5dOQjmFbPwMBi1kDqJt-2Lc46_-t_vc"

http  http://127.0.0.1:8000/api/vendors/refresh/ refresh=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1Nzc2NTk2LCJpYXQiOjE3MTU3NzYyOTYsImp0aSI6IjA1MGNjZmU0Mzc1MjQ0NDU5MDhjYWE4ZWYyZGM3Y2Q2IiwidXNlcl9pZCI6MX0.fM0ly9KTOIuC5dOQjmFbPwMBi1kDqJt-2Lc46_-t_vc"

'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('main.urls')),
    path('api/token/',jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/',include('rest_framework.urls')),
    
]
