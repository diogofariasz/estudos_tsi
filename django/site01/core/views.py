from django.shortcuts import render

def inicial(request):
    return render(request, "index.html")

def contato(request):
    return render(request, "contato.html")

def seila(request):
    return render(request, "seila.html")
