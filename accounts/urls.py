from django.urls import path
from .views import signup , activate , dashboard


urlpatterns = [
    path('signup' , signup),
    path('<str:username>/activate' , activate),
    path('dashboard' , dashboard),
]