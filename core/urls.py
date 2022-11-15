from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    path('vehiculo/create', views.create_vehiculo, name='create_vehiculo'),
    path('vehiculo/<int:vehiculo_id>', views.update_vehiculo, name='update_vehiculo'),
    path('vehiculo/<int:vehiculo_id>/delete', views.delete_vehiculo, name='delete_vehiculo'),
    path('vehiculos/', views.view_vehiculo, name='view_vehiculos'),
    path('propietarios/', views.view_propietarios, name='view_propietarios'),
    path('propietario/create', views.create_propietario, name='create_propietario'),
    path('propietario/<int:propietario_id>', views.update_propietario, name='update_propietario'),
    path('propietario/<int:propietario_id>/delete', views.delete_propietario, name='delete_propietario'),
    path('vehiculo_propietario/<int:propietario_id>', views.vehiculo_propietario, name='vehiculo_propietario'),
    path('ticket/<int:ticket_id>', views.view_ticket, name='view_ticket'),
    path('create/ticket/', views.create_ticket, name='ticket.create'),
    path('registrar_salida/ticket/<int:ticket_id>', views.registrar_salida, name='ticket_registrar')
]
