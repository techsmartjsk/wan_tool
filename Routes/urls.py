from django.urls import path
from . import views

urlpatterns = [
    path('', views.disclaimer, name='disclaimer'),
    path('platform/', views.platform, name='platform'),
    path('data/', views.index, name='index'),
    path('substation/<int:id>/', views.substation, name='substation'),
]
