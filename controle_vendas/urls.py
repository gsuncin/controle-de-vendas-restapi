"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import list_lotes, list_clientes
from .views import detail_pedidos, detail_produtos, detail_lotes, detail_clientes
from .views import add_produtos, add_pedidos
from .views import PedidoView, ProdutoView
from .views import api_login
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Produtos
    path('list-produtos/', ProdutoView.as_view(), name='list_produtos'),
    path('detail-produtos/<int:id>', detail_produtos, name='detail_produtos'),
    path('add-produtos/', add_produtos, name='add_produtos'),

    # Pedidos
    path('list-pedidos/', PedidoView.as_view(), name='list_pedidos'),
    path('detail-pedidos/<int:id>', detail_pedidos, name='detail_pedidos'),
    path('add-pedidos/', add_pedidos, name='add_pedidos'),

    # Lotes
    path('list-lotes/', list_lotes, name='list_lotes'),
    path('detail-lotes/<int:id>', detail_lotes, name='list_lotes'),

    # Clientes
    path('list-clientes/', list_clientes, name='list_clientes'),
    path('detail-clientes/<int:id>', detail_clientes, name='list_clientes'),

    # Auth
    path('login/', api_login, name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),
]
