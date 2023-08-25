from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_trabajos, name='lista_trabajos'),
    path('<int:trabajo_id>/', views.detalle_trabajo, name='detalle_trabajo'),
]
