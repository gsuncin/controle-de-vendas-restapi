from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as dj_login
from .models import Produto, Pedido, Lote, Cliente
from .serializers import LoteModelSerializer, ClienteModelSerializer, ProdutoModelSerializer, PedidoModelSerializer
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class Pagination(LimitOffsetPagination):
    default_limit = 4
    max_limit = 5


class ProdutoView(ListAPIView):
    """
    GET para listar todos os Produtos
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoModelSerializer
    pagination_class = Pagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['nome', 'valor']


class PedidoView(ListAPIView):
    """
    GET para listar todos os Pedidos
    """
    queryset = Pedido.objects.all()
    serializer_class = PedidoModelSerializer
    pagination_class = Pagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['valor_total', 'data_compra']


@require_http_methods(['GET'])
@login_required
def detail_produtos(request, id):
    """
    Método para detalhar produto por ID
    """
    try:
        produto = Produto.objects.get(id=id)
    except ObjectDoesNotExist:
        response = {"Produto": "Produto inexistente"}
        return JsonResponse(response)

    status = 200 if not request.user.is_anonymous else 403
    try:
        response = {
            "id": produto.id,
            "identificador": produto.identificador,
            "nome": produto.nome,
            "numero_lote": model_to_dict(produto.numero_lote),
            "valor": produto.valor,
            "cor": produto.cor,
            "descricao": produto.descricao
        }
        return JsonResponse(response, status=status)
    except Exception:
        response = {"Produto": "Erro na requisição"}
        return JsonResponse(response, status=status)


@csrf_exempt
@require_http_methods(['POST'])
@login_required
def add_produtos(request):
    """
    Método para adicionar novos produtos
    """
    identificador = request.POST.get("identificador")
    nome = request.POST.get("nome")
    numero_lote_identificador = request.POST.get("numero_lote")
    valor = request.POST.get("valor")
    cor = request.POST.get("cor")
    descricao = request.POST.get("descricao")
    try:
        numero_lote = Lote.objects.get(identificador=numero_lote_identificador)
        Produto.objects.create(
            identificador=identificador,
            nome=nome,
            numero_lote=numero_lote,
            valor=valor,
            cor=cor,
            descricao=descricao
        )
        return JsonResponse(dict(message="Produto registrado com sucesso!"))
    except Exception:
        return JsonResponse(dict(message="Problema ao registrar novo produto"))


@require_http_methods(['GET'])
@login_required
def detail_pedidos(request, id):
    """
    Método para detalhar pedido por ID
    """
    try:
        pedido = Pedido.objects.get(id=id)
    except ObjectDoesNotExist:
        response = {"Pedido": "Pedido inexistente"}
        return JsonResponse(response)
    status = 200 if not request.user.is_anonymous else 403
    try:
        response = {
            "id": pedido.id,
            "identificador": pedido.identificador,
            "produtos": list(pedido.produtos.all().values()),
            "status": pedido.status,
            "cliente": model_to_dict(pedido.cliente),
            "vendedor": model_to_dict(pedido.vendedor),
            "valor_total": pedido.valor_total,
        }
        return JsonResponse(response, status=status)
    except Exception:
        response = {"Produto": "Erro na requisição"}
        return JsonResponse(response, status=status)


@csrf_exempt
@require_http_methods(['POST'])
@login_required
def add_pedidos(request):
    """
    Método para adicionar novos produtos
    """
    identificador = request.POST.get("identificador")
    produtos = request.POST.get("produtos")
    status = request.POST.get("status")
    cliente = request.POST.get("cliente")
    vendedor = request.POST.get("vendedor")
    valor_total = request.POST.get("valor_total")
    try:
        produtos_list = []
        produtos = produtos.split()
        for produto in produtos:
            produto = Produto.objects.get(identificador=produto)
            produtos_list.append(produto)
        cliente = Cliente.objects.get(nome=cliente)
        vendedor = User.objects.get(username=vendedor)
        pedido = Pedido.objects.create(
            identificador=identificador,
            status=status,
            cliente=cliente,
            vendedor=vendedor,
            valor_total=valor_total
        )
        for produto in produtos_list:
            pedido.produtos.add(produto)
        return JsonResponse(dict(message="Pedido registrado com sucesso!"))
    except Exception:
        return JsonResponse(dict(message="Problema ao registrar novo pedido"))


@require_http_methods(['GET'])
@login_required
def list_lotes(request):
    """
    Método para listar Lotes
    """
    lotes = Lote.objects.all().values()
    response = {}
    status = 200 if not request.user.is_anonymous else 403
    try:
        response = {'Lotes': list(lotes)}
    except Exception:
        reponse = {'Lote': 'Lotes não localizados'}
    return JsonResponse(response, status=status, safe=False)


@require_http_methods(['GET'])
@login_required
def detail_lotes(request, id):
    """
    Método para detalhar lotes por id
    Utilizei Model Serializer do Django RestFramework
    """
    try:
        lote = Lote.objects.get(id=id)
    except ObjectDoesNotExist:
        response = {"Lote": "Lote inexistente"}
        return JsonResponse(response)
    status = 200 if not request.user.is_anonymous else 403
    try:
        serializer = LoteModelSerializer(lote)
        response = {"Lote": serializer.data}
        return JsonResponse(response, status=status)
    except Exception:
        response = {"Produto": "Erro na requisição"}
        return JsonResponse(response, status=status)


@require_http_methods(['GET'])
@login_required
def list_clientes(request):
    """
    Método para listar Clientes
    """
    cliente = Cliente.objects.all().values()
    response = {}
    status = 200 if not request.user.is_anonymous else 403
    try:
        response = {'Clientes': list(cliente)}
    except Exception:
        reponse = {'Cliente': 'Clientes não localizados'}
    return JsonResponse(response, status=status, safe=False)


@require_http_methods(['GET'])
@login_required
def detail_clientes(request, id):
    """
    Método para detalhar lotes por id
    Utilizei Model Serializer do Django RestFramework
    """
    try:
        cliente = Cliente.objects.get(id=id)
    except ObjectDoesNotExist:
        response = {"Cliente": "Cliente inexistente"}
        return JsonResponse(response)
    status = 200 if not request.user.is_anonymous else 403
    try:
        serializer = ClienteModelSerializer(cliente)
        response = {"Cliente": serializer.data}
        return JsonResponse(response, status=status)
    except Exception:
        response = {"Produto": "Erro na requisição"}
        return JsonResponse(response, status=status)


@csrf_exempt
def api_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        if user.is_active:
            dj_login(request, user)
            return JsonResponse({"Login": f"Usuario '{username}' logado com sucesso"}, safe=False)
    else:
        return JsonResponse({"Login:": "Nome de usuário ou senha incorreta"})
