from multiprocessing import context
from django.shortcuts import render

def nome(request):
    context = {"meu_nome":"Diogo",
        "idade":20,
        "curso":"TSI"
    }
    return render(request, 'nome.html', context)

def cadastro(request, nome, idade, curso):
    context = {
        "nome_url": nome,
        "idade_url": idade,
        "curso_url": curso
    }
    return render(request, 'cadastro.html', context)

def soma (request, numero1, numero2):
    context = {
        "numero_1": numero1,
        "numero_2": numero2,
        "resultado": numero1 + numero2,
    }
    return render(request, 'soma.html', context)

def subtracao (request, numero1, numero2):
    context = {
        "numero_1": numero1,
        "numero_2": numero2,
        "resultado": numero1 - numero2,
    }
    return render(request, 'subtracao.html', context)

def multiplicacao (request, numero1, numero2):
    context = {
        "numero_1": numero1,
        "numero_2": numero2,
        "resultado": numero1 * numero2,
    }
    return render(request, 'multiplicacao.html', context)

def divisao (request, numero1, numero2):
    context = {
        "numero_1": numero1,
        "numero_2": numero2,
        "resultado": numero1 / numero2,
    }
    return render(request, 'divisao.html', context)