from django.shortcuts import render, redirect
from .models import Curso, Area
from .forms import CursoForm, PublicoForm, AreaForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AreaSerializer

#----------------------------------Area de API----------------------------------------#

@api_view(['GET'])
def areaAPIlistar(request):
    areas = Area.objects.all()
    areas_serializers = AreaSerializer(areas, many=True)
    return Response(areas_serializers.data)

@api_view(['PUT'])
def areaAPIadicionar(request):
    area = AreaSerializer(data=request.data)
    if area.is_valid():
        area.save()
    return Response(area.data, 
            status=status.HTTP_201_CREATED)

@api_view(['POST'])
def areaAPIatualizar(request, id):
    area_bd = Area.objects.get(id=id)
    area = AreaSerializer(data=request.data, 
                            instance=area_bd)
    if area.is_valid():
        area.save()
        return Response(area.data, 
            status=status.HTTP_202_ACCEPTED)
    
@api_view(['DELETE'])
def areaAPIremover(request, id):
    area_bd = Area.objects.get(id=id)
    if area_bd:
        area_bd.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#----------------------------------Area de API------------------------------------------#

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