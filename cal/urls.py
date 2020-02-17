from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('base',views.base),
    path('add',views.add),
    path('cal1_1',views.cal1_1)  
] 
