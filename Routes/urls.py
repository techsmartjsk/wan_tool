from django.urls import path
from . import views

urlpatterns = [
    path('', views.inputs, name='inputs'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('platform/', views.platform, name='platform'),
    path('circuit_data/', views.index, name='index'),
    path('transformer_data/', views.transformer_data, name='transformer_data'),
    path('load_data/', views.load_data, name='load_data'),
    path('ph_data/', views.ph_fault_data, name='ph_fault_data'),
    path('earth_data/', views.earth_fault_data, name='earth_fault_data'),
    path('inputs/', views.inputs, name='inputs'),
]
