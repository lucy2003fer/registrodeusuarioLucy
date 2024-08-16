from django.shortcuts import render, redirect
from django.shortcuts import Persona
from .forms import PersonaForms

# Create your views here.

def regiaterUser(request):
    if request.method == 'POST':
        forms = PersonaForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('ListarUsuario')
        
        else:
            forms = PersonaForms()
            
            
        return render(request,
                      template_name='registrarUsuario.html', context={'forms':
                          forms})