from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('beer', views.beer, name='beer'),
    path('coffee', views.coffee, name='coffee'),
    path('catering', views.catering, name='catering'),
    path('application', views.application, name='application'),
    path('store', views.store, name='store'),
]