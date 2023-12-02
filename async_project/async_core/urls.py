from django.urls import path
from . import views


urlpatterns = [
    path('async_api/', views.AsyncView.as_view(), name='async_api'),
]
