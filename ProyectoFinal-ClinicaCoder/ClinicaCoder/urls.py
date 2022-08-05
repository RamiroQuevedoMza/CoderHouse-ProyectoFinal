
from django.urls import path
from ClinicaCoder.views import inicio, registros, usuarios_registrados, MedicosLista, MedicosInformacion, CrearMedicos, EditarMedicos, BorrarMedicos

urlpatterns = [
    path('inicio/', inicio, name= "inicio"),
    path('registros/', registros, name= "registros"),
    path('lista_usuarios/', usuarios_registrados, name= "usuarios-registrados"),
    path("medicos/lista", MedicosLista.as_view(), name="lista_medicos"),
    path("medicos/<pk>/", MedicosInformacion.as_view(), name="info_medicos"),
    path("medicos/crear", CrearMedicos.as_view(), name="crear_medicos"),
    path("medicos/<pk>/editar", EditarMedicos.as_view(), name="editar_medicos"),
    path("medicos/<pk>/borrar", BorrarMedicos.as_view(), name="borrar_medicos"),

]
