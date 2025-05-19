from django.urls import path
from galeria.views import index, segunda_pagina, login, cadastro, logout

urlpatterns = [
    path('', index, name='index'),
    path('segunda/', segunda_pagina, name='segunda_pagina'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', logout, name='logout'),
]