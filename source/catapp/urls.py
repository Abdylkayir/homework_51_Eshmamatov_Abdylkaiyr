from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('details/<str:cat_name>/', views.cat_details, name='cat_details'),
    path('details/<str:cat_name>/action/', views.cat_action, name='cat_action'),
]