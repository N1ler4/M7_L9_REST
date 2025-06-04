from django.urls import path
from . import views

urlpatterns = [
    path('', views.word_list, name='word-list'),          
    path('create/', views.word_create, name='word-create'), 
    path('<int:pk>/', views.word_detail, name='word-detail'), 
]
