from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.

@login_required(login_url='/login/')
@permission_required('inv.change_marca', login_url='bases:sin_privilegios')
def prediccionSeleccion(request):
    template_name="inf/prediccion_seleccion.html"
    
    return render(request, template_name)