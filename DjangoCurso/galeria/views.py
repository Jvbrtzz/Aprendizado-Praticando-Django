from django.shortcuts import redirect, render, get_object_or_404
from galeria.models import Dados, Repositorio
from galeria.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    filtro = request.GET.get('filtro', '')
    if filtro:
        repositorio = Repositorio.objects.filter(nome__icontains=filtro)
    else:
        repositorio = Repositorio.objects.all()
    return render(request, 'index.html', {'repositorios': repositorio, 'filtro': filtro})

def segunda_pagina(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar esta página.')
        return redirect('login')
    galeria = Dados.objects.filter(genero='M')
    return render(request, 'segunda_pagina.html', {'dados': galeria})

@login_required
def github_page(request):
    # social_data já está disponível no template via context processor
    return render(request, 'githubpage/github_page.html')

def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            nome_login = form.cleaned_data.get('nome_login')
            senha = form.cleaned_data.get('senha')
            usuario = authenticate(request, username=nome_login, password=senha)
            if usuario is not None:
                auth_login(request, usuario)
                messages.success(request, 'Login realizado com sucesso.')
                return redirect('index')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
                form.add_error(None, 'Usuário ou senha inválidos.')
    return render(request, 'login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('senha_1') != form.cleaned_data.get('senha_2'):
                form.add_error('senha_2', 'As senhas não conferem.')
                return render(request, 'cadastro.html', {'form': form})
            nome = form.cleaned_data.get('nome_cadastro')
            email = form.cleaned_data.get('email')
            senha_1 = form.cleaned_data.get('senha_1')
            if User.objects.filter(username=nome).exists():
                form.add_error('nome_cadastro', 'Usuário já existe.')
                return render(request, 'cadastro.html', {'form': form})
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha_1
            )
            usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso.')
            return redirect('login')
    return render(request, 'cadastro.html', {'form': form})

def logout(request):
    auth_logout(request)
    messages.success(request, 'Logout realizado com sucesso.')
    return redirect('login')

@login_required
def repositorio(request):
    repositorios = Repositorio.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        linguagem = request.POST.get('linguagem')
        visibilidade = request.POST.get('visibilidade')
        repositorio = Repositorio(
            nome=nome,
            descricao=descricao,
            linguagem=linguagem,
            visibilidade=visibilidade,
        )
        repositorio.save()
        messages.success(request, 'Repositório criado com sucesso.')
        return redirect('repositorio')
    return render(request, 'githubpage/repositorio.html', {'repositorios': repositorios})

def excluir_repositorio(request, repo_id):
    if request.method == 'POST':
        repo = get_object_or_404(Repositorio, id=repo_id)
        repo.delete()
    return redirect('repositorio')  # ajuste para o nome correto da sua url de listagem
