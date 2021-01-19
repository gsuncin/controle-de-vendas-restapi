from django.db import models
from django.conf import settings


class Lote(models.Model):
    identificador = models.IntegerField()
    data_fabricacao = models.DateField('Data de Fabricacao', null=False, blank=False)
    quantidade_fabricada = models.IntegerField()

    class Meta:
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'

    def __str__(self):
        return str(self.identificador)


class Produto(models.Model):
    identificador = models.IntegerField()
    nome = models.CharField('Nome', max_length=250, null=False, blank=False)
    numero_lote = models.ForeignKey(Lote, related_name='numero_lote', on_delete=models.CASCADE)
    valor = models.DecimalField('Valor', decimal_places=2, max_digits=12, null=False)
    cor = models.CharField('Cor', max_length=50, null=False, blank=False)
    descricao = models.TextField('Descricao', null=False, blank=False)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=250, null=False, blank=False)
    cpf = models.CharField('CPF', max_length=11, null=False, blank=False)
    data_nascimento = models.DateField('Data de nascimento', null=False, blank=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    STATUS_CHOICES = (
        (1, 'Ativo'),
        (2, 'Pendente'),
        (3, 'Concluido'),
        (4, 'Cancelado')

    )
    identificador = models.IntegerField()
    produtos = models.ManyToManyField(Produto, related_name="produtos", blank=True)
    status = models.SmallIntegerField('Status', choices=STATUS_CHOICES, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, related_name="cliente", on_delete=models.DO_NOTHING)
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="vendedor", on_delete=models.DO_NOTHING)
    valor_total = models.DecimalField('Valor Total', decimal_places=2, max_digits=12, null=False)
    data_compra = models.DateField('Data da Compra', auto_now=True, blank=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return str(self.identificador)
