from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index), 
    path('administrador/', views.administrador), 
    path('registro/', auth.registro),
    path('login/', auth.login),
    path('logout/', auth.logout),
    path('mensaje', views.nuevo_mensaje),
    path('comentario/<int:mensaje_id>', views.nuevo_comentario)
]
