from django.shortcuts import render, redirect
from .models import Transacao
from .form import TransacaoForm
import datetime

# Create your views here.
def home(request):
    contexto = {}
    
    return render (request,'contas/home.html',contexto)

def listagem(request):
    contexto = {}
    contexto['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html',contexto)

def nova_transacao(request):
    contexto = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    contexto['form'] = form 
    return render(request, 'contas/form.html', contexto)

def update(request, pk):
    contexto = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    
    contexto['form'] = form
    contexto['transacao'] = transacao
    return render(request, 'contas/form.html', contexto)

def delete(request, pk):
    contexto = {}
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')