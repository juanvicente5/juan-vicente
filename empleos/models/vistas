from django.shortcuts import render, get_object_or_404
from .models import Trabajo

def lista_trabajos(request):
    trabajos = Trabajo.objects.all()
    return render(request, 'empleos/lista_trabajos.html', {'trabajos': trabajos})

def detalle_trabajo(request, trabajo_id):
    trabajo = get_object_or_404(Trabajo, pk=trabajo_id)
    return render(request, 'empleos/detalle_trabajo.html', {'trabajo': trabajo})
