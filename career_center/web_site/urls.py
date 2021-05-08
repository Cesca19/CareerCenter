from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('offer', views.offer, name='offer'),
    path('offer/<str:companie_name>', views.detail, name='detail')
]
