from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('predict', views.predict),
    path('ping-test', views.ping_test),
]
