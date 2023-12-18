from django.urls import path
from . import views

urlpatterns = [

    path('',views.index, name='index'),
    path('Request1',views.Request1, name='Request1'),
    path('Request2_1', views.Request2_1, name='Request2_1'),
    path('Request2_2', views.Request2_2, name='Request2_2'),
    path('Request3', views.Request3, name='Request3'),
    path('Request4', views.Request4, name='Request4'),
    path('Request5', views.Request5, name='Request5'),
    path('Request6_1', views.Request6_1, name='Request6_1'),
    path('Request6_2', views.Request6_2, name='Request6_2'),
    path('Request7', views.Request7, name='Request7'),
    path('form1',views.form1, name='form1'),
    path('about',views.about, name='about'),
    path('F',views.F, name='F')
]