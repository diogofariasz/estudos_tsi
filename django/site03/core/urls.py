from django.urls import path, include
from .views import home, cadastro, cadastro_resultado, login, sucesso

urlpatterns = [
    path('', home, name='nome'),
    path('cadastro/', cadastro, name='cadastro'),
    path('cadastro_resultado/', cadastro_resultado, name='cadastro_resultado'),
    path('login/', login, name='login'),
    path('sucesso/', sucesso, name='sucesso'),
]
