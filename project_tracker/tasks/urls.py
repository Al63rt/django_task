from django.urls import path, include
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('another/', views.another_page, name='another_page'),  # новый маршрут
]