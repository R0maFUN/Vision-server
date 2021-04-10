from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', views.auth, name='auth'),
    path('checkUsername/', views.checkLoginForDuplicating, name='checkLoginForDuplicating'),
    path('registration/', views.registration, name='registration'),
]