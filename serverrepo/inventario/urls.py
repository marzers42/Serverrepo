from django.urls import path
from . import views
from . import views_auth

urlpatterns = [

    path("login/", views_auth.login_view, name="login"),
    path("logout/", views_auth.logout_view, name="logout"),
    path("virtuales/", views.lista_virtuales, name="lista_virtuales"),
    path("virtuales/agregar/", views.agregar_virtual, name="agregar_virtual"),
    path("virtuales/editar/<int:id>/", views.editar_virtual, name="editar_virtual"),
    path("virtuales/eliminar/<int:id>/", views.eliminar_virtual, name="eliminar_virtual"),
    #path('', views.lista_equipos, name='lista_equipos'),
    #path("agregar/", views.agregar_servidorvirtual, name="agregar_equipo"),
    #path("editar/<int:id>", views.editar_servidorvirtual, name="editar_equipo"),
    #path("eliminar/<int:id>", views.eliminar_servidorvirtual, name="eliminar_eqipo")
]
