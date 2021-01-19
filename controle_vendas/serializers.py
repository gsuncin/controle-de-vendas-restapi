from rest_framework import serializers
from .models import Cliente, Lote, Produto, Pedido
from django.contrib.auth.models import User


class ClienteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username']


class LoteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = "__all__"


class ProdutoModelSerializer(serializers.ModelSerializer):
    lote = LoteModelSerializer(source='numero_lote', many=False)

    class Meta:
        model = Produto
        fields = ['identificador', 'nome', 'lote', 'valor', 'cor', 'descricao']


class PedidoModelSerializer(serializers.ModelSerializer):
    produto = ProdutoModelSerializer(source='produtos', many=True)
    clientes = ClienteModelSerializer(source='cliente', many=False)
    vendedores = UserModelSerializer(source='vendedor', many=False)

    class Meta:
        model = Pedido
        fields = ['identificador', 'produto', 'status', 'clientes', 'vendedores', 'valor_total', 'data_compra']
