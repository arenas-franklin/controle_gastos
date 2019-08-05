from django.shortcuts import render
from .models import Transacao
import datetime

# Create your views here.
def home(request):
    contexto = {}
    
    return render (request,'contas/home.html',contexto)

def listagem(request):
    contexto = {}
    contexto['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html',contexto)
