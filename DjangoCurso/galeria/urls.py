from django.urls import path
from galeria.views import index, segunda_pagina, login, cadastro, logout, github_page, repositorio, excluir_repositorio

urlpatterns = [
    path('', index, name='index'),
    path('segunda/', segunda_pagina, name='segunda_pagina'),
    path('github/', github_page, name='github_page'),
    path('repositorio/', repositorio, name='repositorio'),
    path('repositorio/excluir/<int:repo_id>/', excluir_repositorio, name='excluir_repositorio'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', logout, name='logout'),
]