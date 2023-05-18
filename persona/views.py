from django.shortcuts import render,redirect, get_object_or_404
from persona.models import Persona
from django.http import HttpResponseRedirect
from persona.forms import PersonaForm

def agregar(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/mostrar")
            except:
                pass
    else:
        form = PersonaForm()
    return render(request, 'index.html', {'form':form})

    
def mostrar(request):
    personas = Persona.objects.all()
    return render(request, 'mostrar.html', {'personas': personas})

def editar(request,rut):
    persona = Persona.objects.get(rut=rut)
    return render(request, 'editar.html', {'persona': persona})

def actualizar(request, rut):
    persona = get_object_or_404(Persona, rut=rut)
    
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mostrar')
    else:
        form = PersonaForm(instance=persona)

    return render(request, 'editar.html', {'form': form, 'persona': persona})

def eliminar(request, rut):     
    persona = Persona.objects.get(rut=rut)
    persona.delete()
    return redirect ("/mostrar")