from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm, PublicoForm, AreaForm

def cursos(request):
    lista_cursos = Curso.objects.all()

    context = {
        'cursos': lista_cursos,
    }

    return render(request, 'cursos.html', context)

def cadastrar_curso(request):
    form = CursoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('cursos')

    context = {
        'form_curso': form,
    }

    return render(request, 'curso_cadastrar.html', context)

def cadastrar_publico(request):
    form = PublicoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('cursos')

    context = {
        'form_publico': form,
    }

    return render(request, 'publico_cadastrar.html', context)

def cadastrar_area(request):
    form = AreaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('cursos')

    context = {
        'form_area': form,
    }

    return render(request, 'area_cadastrar.html', context)

def editar_curso(request, id):
    # pegar um curso pelo id
    curso = Curso.objects.get(pk=id)

    form = CursoForm(request.POST or None, instance=curso)

    if form.is_valid():
        form.save()
        return redirect('cursos')

    context = {
        'form_curso': form,
    }

    return render(request, 'curso_cadastrar.html', context)

def remover_curso(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()

    return redirect('cursos')