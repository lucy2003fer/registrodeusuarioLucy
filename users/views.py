from django.shortcuts import render, redirect
from .forms import PersonaForms

# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        forms = PersonaForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('ListarUsuario')
        
        else:
            forms = PersonaForms()
            
            
        return render(request,'registrarUsuario.html', {'forms':forms})