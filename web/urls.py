from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sobreNosotros', views.sobreNosotros, name="sobreNosotros"),
    path('stock', views.stock, name="stock"),
    path('productos', views.productos, name="productos"),
    path('detalle/<id>/', views.detalle, name='detalle'),
    path('modificar/<id>/', views.modificar, name="modificar"),
    path('eliminar/<id>/', views.eliminar, name="eliminar"),
    path('crear', views.crear, name="crear"),
    path('contacto', views.contacto, name="contacto"),
    path('articulos', views.articulos, name="articulos"),
    path('logout', views.cerrar, name="cerrar"),
    path('registration/login', views.login, name="login"),
    path('registration/registrar', views.registrar, name="registrar"),
    path('tienda/',views.tienda, name="tienda"),
    path('agregar/<id>', views.agregar_producto, name="agregar"),
    path('eliminar_producto/<id>', views.eliminar_producto, name="eliminar_producto"),
    path('restar/<id>', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_carrito, name="limpiar"),
    path('generarBoleta/', views.generarBoleta,name="generarBoleta"),
    path('perfil/', views.perfil, name='perfil'),
]