from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('lists/', views.lists_index, name='lists-index'),
    path('lists/<int:list_id>/', views.list_detail, name='list-detail'),
    path('lists/create/', views.ListCreate.as_view(), name='list-create'),


]
