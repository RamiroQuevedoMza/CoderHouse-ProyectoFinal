from django.shortcuts import render
from django.http import HttpResponse
from ClinicaCoder.models import Usuarios, Medicos
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def inicio(request):
    return render(request, "ClinicaCoder/inicio.html")

def registros(request):
    context = {}
    if request.GET:
        context['nombre'] = request.GET["nombre"]
        context['segundo_nombre'] = request.GET["segundo_nombre"]
        context['apellido'] = request.GET["apellido"]   
         
    return render(request, "ClinicaCoder/registro-usuarios.html", context) 

def usuarios_registrados(request):
    context = {}
    context["usuarios"] = Usuarios.objects.all()

    return render(request, "ClinicaCoder/lista-usuarios.html", context)

class MedicosLista(ListView):
    model = Medicos
    template_name = "ClinicaCoder/lista_medicos.html"
    
class MedicosInformacion(DetailView):
    model = Medicos
    template_name = "ClinicaCoder/informacion_medicos.html"
    
class EditarMedicos(UpdateView):
    model = Medicos
    template_name = "ClinicaCoder/form_medicos.html"
    success_url = "/ClinicaCoder/medicos/lista"
    fields = ["nombre", "apellido", "edad", "especialidad"]

class CrearMedicos(CreateView):
    model = Medicos
    template_name = "ClinicaCoder/form_medicos.html"
    success_url = "/ClinicaCoder/medicos/lista"
    fields = ["nombre", "apellido", "edad", "especialidad"]

class BorrarMedicos(DeleteView):
    model = Medicos
    template_name = "ClinicaCoder/borrar_medicos.html"
    success_url = "/ClinicaCoder/medicos/lista"