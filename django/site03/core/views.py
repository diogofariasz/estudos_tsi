from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def cadastro_resultado(request):
    nome = request.POST['nome']
    cpf = request.POST['cpf']

    context = {
        'nome_digitado': nome,
          'cpf_digitado':cpf,
    }

   
    return render(request, 'cadastro_resultado.html', context)

def login(request):
        return render(request, 'login.html', )
  
def sucesso(request):
    email = request.POST['email']
    senha = request.POST['senha']

    email_correto = 'admin@email.com'
    senha_correto = '123@ifrn'
    
    if email == email_correto and senha == senha_correto:
         return render(request, 'sucesso.html', )
    else:
        return render(request, 'login.html')
   
