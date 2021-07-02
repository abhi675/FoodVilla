from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('payment/<str:foodname>/<int:price>/<path:image>',views.payment,name='payment'),
   
]