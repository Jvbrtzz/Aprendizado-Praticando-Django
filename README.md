# 🚀 Iniciando um Projeto Django

Siga os passos abaixo para configurar e rodar seu projeto Django pela primeira vez.

## ✅ Passo a passo

## 1. Crie um ambiente virtual
## Dentro do diretório do projeto, execute:

python -m venv venv

### Ative o ambiente virtual:

venv/Scripts/activate

### Instale o Django:

pip install django==4.1

### Crie o projeto Django:

django-admin startproject setup .

### Crie uma app Django:

python manage.py startapp, seguido do nome app.

### Rode o servidor pela primeira vez:

python manage.py runserver

## Pronto! Agora você já subiu um servidor Django pela primeira vez.

## 2. Fluxo OIDC (OpenID Connect) com Django Allauth e GitHub

Este projeto implementa autenticação social via **GitHub** utilizando o padrão OIDC (OpenID Connect) através do pacote [django-allauth](https://django-allauth.readthedocs.io/).

### Como funciona o fluxo OIDC neste projeto?

1. **Usuário clica em "Login com Github":**  
   O usuário é redirecionado para a página de autenticação do GitHub.

2. **Permissão e autenticação:**  
   O usuário faz login no GitHub e autoriza o acesso do seu perfil à aplicação.

3. **Callback e troca de código:**  
   O GitHub redireciona de volta para sua aplicação Django, enviando um código de autorização.

4. **Validação e obtenção de dados:**  
   O django-allauth troca esse código por um token de acesso e busca os dados do perfil do usuário no GitHub.

5. **Criação/autenticação do usuário:**  
   Se o usuário já existe, ele é autenticado. Se não, um novo usuário é criado automaticamente no banco de dados.

6. **Acesso aos dados sociais:**  
   Os dados do perfil do GitHub ficam disponíveis em `social_data` (via context processor), podendo ser exibidos em qualquer template, como avatar, nome, login, bio, etc.

### Configuração

- O fluxo OIDC está habilitado graças à configuração do django-allauth no `settings.py` e ao registro do app GitHub no painel de desenvolvedor do GitHub.
- As credenciais (`client_id` e `secret`) são lidas do arquivo `.env`.
- O context processor `social_data` garante que os dados do GitHub estejam disponíveis em todos os templates.

### Exemplo de uso no template

```django
{% if social_data %}
    <img src="{{ social_data.avatar_url }}" alt="Avatar" width="40">
    <span>{{ social_data.name|default:social_data.login }}</span>
{% endif %}
```


